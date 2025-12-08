from aiogram import Bot, Dispatcher, types, executor
from pymongo import MongoClient
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz
from datetime import datetime
import os
import config

# -----------------------------
# CONFIG
# -----------------------------
BOT_TOKEN = "YOUR_BOT_TOKEN"
MONGO_URL = "mongodb://localhost:27017"  # or your MongoDB Atlas link

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

client = MongoClient(config.MONGO_URL)
db = client.financebot
transactions = db.transactions


# -----------------------------
# Start command
# -----------------------------
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    # Check if user already exists
    user = db.users.find_one({"user_id": msg.from_user.id})
    if not user:
        # Save user in database
        db.users.insert_one({
            "user_id": msg.from_user.id,
            "first_name": msg.from_user.first_name,
            "username": msg.from_user.username
        })

    await msg.reply(
        "👋 Welcome to Personal Finance Tracker Bot!\n\n"
        "Use these commands:\n"
        "💸 Add Expense → /expense 500 food\n"
        "💰 Add Saving → /save 1000\n"
        "📊 Monthly Summary → /summary\n"
        "📒 View Records → /records\n"
    )


# -----------------------------
# Add Expense
# -----------------------------
@dp.message_handler(commands=['expense'])
async def add_expense(msg: types.Message):
    try:
        _, amount, category = msg.text.split(maxsplit=2)
        amount = float(amount)

        transactions.insert_one({
            "user_id": msg.from_user.id,
            "type": "expense",
            "amount": amount,
            "category": category,
            "date": datetime.now()
        })

        await msg.reply(f"💸 Added Expense: ₹{amount} for {category}")

    except:
        await msg.reply("❗ Correct format:\n/expense 500 food")


# -----------------------------
# Add Saving
# -----------------------------
@dp.message_handler(commands=['save'])
async def add_saving(msg: types.Message):
    try:
        _, amount = msg.text.split()
        amount = float(amount)

        transactions.insert_one({
            "user_id": msg.from_user.id,
            "type": "saving",
            "amount": amount,
            "date": datetime.now()
        })

        await msg.reply(f"💰 Saving Added: ₹{amount}")

    except:
        await msg.reply("❗ Correct format:\n/save 1000")


# -----------------------------
# Monthly Summary
# -----------------------------
@dp.message_handler(commands=['summary'])
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
@dp.message_handler(commands=['records'])
async def show_records(msg: types.Message):
    user = msg.from_user.id
    data = transactions.find({"user_id": user}).sort("date", -1)

    text = "📒 *Your Finance Records:*\n\n"
    empty = True

    for r in data:
        empty = False
        date = r['date'].strftime("%d-%m-%Y %H:%M")
        if r["type"] == "expense":
            text += f"💸 Expense ₹{r['amount']} — {r['category']} — {date}\n"
        else:
            text += f"💰 Saving ₹{r['amount']} — {date}\n"

    if empty:
        text = "❗ No records found."

    await msg.reply(text, parse_mode="Markdown")

# -----------------------------
# inline button handler
# -----------------------------
@dp.callback_query_handler(lambda c: c.data == "add_expense_now")
async def process_add_expense(callback):
    await callback.answer()  # remove loading state

    await callback.message.answer(
        "💸 Please enter your expense.\nExample:\n`/expense 250 food`",
        parse_mode="Markdown"
    )


# -----------------------------
# Schedule the daily reminder
# -----------------------------

async def send_daily_reminder():
    users = db.users.find()

    # Inline Button
    btn = InlineKeyboardMarkup().add(
        InlineKeyboardButton("➕ Add Expense Now", callback_data="add_expense_now")
    )

    for user in users:
        try:
            await bot.send_message(
                user['user_id'],
                "⏰ *Reminder!*\nPlease enter today’s expenses 💸",
                reply_markup=btn,
                parse_mode="Markdown"
            )
        except Exception as e:
            print(f"Reminder error for {user['user_id']}: {e}")



async def on_startup(dp):
    scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
    scheduler.add_job(send_daily_reminder, "cron", hour=16, minute=6)  
    scheduler.start()
    print("Scheduler started!")


# -----------------------------
# Run bot
# -----------------------------
executor.start_polling(dp, on_startup=on_startup)

