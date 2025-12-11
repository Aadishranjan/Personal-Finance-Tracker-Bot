from aiogram import types
from db import add_user

# -----------------------------
# Start command
# -----------------------------

async def start(msg: types.Message):
    # Save user to database
    add_user(msg.from_user.id, msg.from_user.first_name, msg.from_user.username)

    # Send image first
    await msg.answer_photo(
        photo="https://i.ibb.co/spBqv7qX/Budgely.png",
        caption="👋 Welcome to *Budgely* — Your Personal Finance Tracker Bot!",
        parse_mode="Markdown"
    )

    # Then send instructions
    await msg.reply(
        "Use these commands:\n\n"
        "💸 Add Expense → /expense 500 food\n"
        "💰 Add Saving → /save 1000\n"
        "📊 Monthly Summary → /summary\n"
        "📒 View Records → /records\n"
    )
