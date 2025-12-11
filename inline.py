from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# -----------------------------
# inline button
# -----------------------------

def report_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📅 Monthly Report", callback_data="report_month"),
        InlineKeyboardButton("📆 Yearly Report", callback_data="report_year")
    )
    return kb
