import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from zoneinfo import ZoneInfo
from aiogram import types

from db import transactions
from inline import report_menu


# Folder for storing PDFs
RESOURCES_DIR = "resources"
os.makedirs(RESOURCES_DIR, exist_ok=True)   # Create folder if not exists


def generate_pdf_report(user_id, period="monthly"):
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    # ----- Determine Report Period -----
    if period == "monthly":
        start = datetime(now.year, now.month, 1, tzinfo=ZoneInfo("Asia/Kolkata"))
        filename = f"report_{user_id}_{now.year}_{now.month}.pdf"
        title = f"Monthly Report - {now.strftime('%B %Y')}"
    else:
        start = datetime(now.year, 1, 1, tzinfo=ZoneInfo("Asia/Kolkata"))
        filename = f"report_{user_id}_{now.year}.pdf"
        title = f"Yearly Report - {now.year}"

    # Full file path inside "resources/"
    file_path = os.path.join(RESOURCES_DIR, filename)

    # ----- Fetch user transactions -----
    data = list(transactions.find({
        "user_id": user_id,
        "date": {"$gte": start}
    }).sort("date", 1))

    # ----- Create PDF -----
    pdf = canvas.Canvas(file_path, pagesize=letter)
    pdf.setTitle(title)

    # Header
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(200, 750, "Finance Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 730, f"User ID: {user_id}")
    pdf.drawString(50, 715, f"Report: {title}")
    pdf.drawString(50, 700, f"Generated: {now.strftime('%d-%m-%Y %H:%M')}")

    # Table headers
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 670, "Date")
    pdf.drawString(150, 670, "Type")
    pdf.drawString(250, 670, "Amount")
    pdf.drawString(350, 670, "Category")

    y = 650
    total_expense = 0
    total_saving = 0

    pdf.setFont("Helvetica", 12)

    # ----- Add each transaction -----
    for r in data:
        date_local = r["date"].astimezone(ZoneInfo("Asia/Kolkata"))
        d = date_local.strftime("%d-%m-%Y")

        if r["type"] == "expense":
            total_expense += r["amount"]
        else:
            total_saving += r["amount"]

        pdf.drawString(50, y, d)
        pdf.drawString(150, y, r["type"])
        pdf.drawString(250, y, str(r["amount"]))
        pdf.drawString(350, y, r.get("category", "-"))

        y -= 20
        if y < 50:
            pdf.showPage()
            y = 750

    # ----- Summary Section -----
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y - 20, "Summary:")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y - 40, f"Total Savings: ₹{total_saving}")
    pdf.drawString(50, y - 55, f"Total Expenses: ₹{total_expense}")
    pdf.drawString(50, y - 70, f"Net Balance: ₹{total_saving - total_expense}")

    pdf.save()
    return file_path


async def pdf_report(msg: types.Message):
    await msg.reply("Choose report type:", reply_markup=report_menu())
