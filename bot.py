from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.expense import add_saving, add_expense
from handlers.summary import summary, show_records
from handlers.start import start
from db import get_all_users
import pytz
from datetime import datetime
import os
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


# -----------------------------
# Register commands
# -----------------------------

dp.register_message_handler(start, commands=['start'])
dp.register_message_handler(add_expense, commands=['expense'])
dp.register_message_handler(add_saving, commands=['save'])
dp.register_message_handler(summary, commands=['summary'])
dp.register_message_handler(show_records, commands=['records'])

# dp.register_callback_query_handler(process_add_expense, lambda c: c.data == "add_expense_now")

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
    users = get_all_users()

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
    scheduler.add_job(send_daily_reminder, "cron", hour=20, minute=0)  # 8 PM IST
    scheduler.start()
    print("Scheduler started!")


# -----------------------------
# Run bot
# -----------------------------
executor.start_polling(dp, on_startup=on_startup)

