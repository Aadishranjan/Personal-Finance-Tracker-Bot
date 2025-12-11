from aiogram import types
from handlers.pdfReport import generate_pdf_report
import os

# -----------------------------
# inline button handler
# -----------------------------

async def report_month(call: types.CallbackQuery):
    await call.answer()

    path = generate_pdf_report(call.from_user.id, "monthly")
    await call.message.answer_document(open(path, "rb"))

    os.remove(path)   # delete after sending


async def report_year(call: types.CallbackQuery):
    await call.answer()

    path = generate_pdf_report(call.from_user.id, "yearly")
    await call.message.answer_document(open(path, "rb"))

    os.remove(path)
