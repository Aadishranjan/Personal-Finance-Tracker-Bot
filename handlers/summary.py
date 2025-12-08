from aiogram import types
from db import transactions
from datetime import datetime
from zoneinfo import ZoneInfo

# -----------------------------
# Monthly Summary
# -----------------------------
async def summary(msg: types.Message):
    user = msg.from_user.id
    today = datetime.now()

    first_day = datetime(today.year, today.month, 1)

    expenses = list(transactions.find({
        "user_id": user,
        "type": "expense",
        "date": {"$gte": first_day}
    }))

    savings = list(transactions.find({
        "user_id": user,
        "type": "saving",
        "date": {"$gte": first_day}
    }))

    total_expense = sum(i["amount"] for i in expenses)
    total_saving = sum(i["amount"] for i in savings)

    await msg.reply(
        f"📊 *{today.strftime('%B %Y')} Summary*\n\n"
        f"💸 Total Spent: ₹{total_expense}\n"
        f"💰 Total Saved: ₹{total_saving}\n"
        f"🧾 Records: {len(expenses)} expenses, {len(savings)} savings",
        parse_mode="Markdown"
    )




# -----------------------------
# View All Records
# -----------------------------
async def show_records(msg: types.Message):
    user = msg.from_user.id
    data = transactions.find({"user_id": user}).sort("date", -1)

    text = "📒 *Your Finance Records:*\n\n"
    empty = True
    for r in data:
        empty = False

        # r['date'] should be tz-aware UTC if using tz_aware=True.
        # If it's naive UTC, replace .astimezone with .replace(tzinfo=timezone.utc).astimezone(...)
        dt = r['date']
        try:
            india_time = dt.astimezone(ZoneInfo("Asia/Kolkata"))
        except Exception:
            # fallback if dt is naive: treat it as UTC then convert
            from datetime import timezone
            india_time = dt.replace(tzinfo=timezone.utc).astimezone(ZoneInfo("Asia/Kolkata"))

        date_str = india_time.strftime("%d-%m-%Y %H:%M")

        if r["type"] == "expense":
            text += f"💸 Expense ₹{r['amount']} — {r['category']} — {date_str}\n"
        else:
            text += f"💰 Saving ₹{r['amount']} — {date_str}\n"

    if empty:
        text = "❗ No records found."

    await msg.reply(text, parse_mode="Markdown")

