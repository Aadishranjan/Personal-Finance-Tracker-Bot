from aiogram import types
from db import expense, saving


# -----------------------------
# Add Expense
# -----------------------------
async def add_expense(msg: types.Message):
    try:
        _, amount, category = msg.text.split(maxsplit=2)
        amount = float(amount)
        
        expense(msg.from_user.id, amount, category)
        await msg.reply(f"💸 Added Expense: ₹{amount} for {category}")

    except:
        await msg.reply("❗ Correct format:\n/expense 500 food")


# -----------------------------
# Add Saving
# -----------------------------
async def add_saving(msg: types.Message):
    try:
        _, amount = msg.text.split(" ", 1)
        amount = float(amount)
        saving(msg.from_user.id, amount)
        await msg.reply(f"💰 Saving Added: ₹{amount}")
    except:
        await msg.reply("❗ Correct format:\n/save 1000")
    


