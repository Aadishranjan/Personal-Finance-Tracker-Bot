from aiogram import types
from db import add_user

# -----------------------------
# Start command
# -----------------------------
async def start(msg: types.Message):
    # Check if user already exists
    add_user(msg.from_user.id, msg.from_user.first_name, msg.from_user.username)

    await msg.reply(
        "👋 Welcome to Personal Finance Tracker Bot!\n\n"
        "Use these commands:\n"
        "💸 Add Expense → /expense 500 food\n"
        "💰 Add Saving → /save 1000\n"
        "📊 Monthly Summary → /summary\n"
        "📒 View Records → /records\n"
    )
