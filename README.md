
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

# Telegram Expense Tracker Bot

A powerful and user-friendly Telegram bot that helps users manage their daily expenses, savings, and financial reports.  
Built using Python, Aiogram, and MongoDB, the bot also supports PDF monthly & yearly financial reports.

---

## 🚀 Features

### 🧾 Expense & Savings Management
- Add daily expenses  
- Add savings  
- View all past records  
- Auto-store user data by Telegram User ID  

### 📅 Financial Reports
- Monthly PDF report  
- Yearly PDF report
- Auto-generated & downloadable  
- Clean and professional PDF layout  

### 📈 Summary Dashboard
- Total expenses  
- Total savings  
- Balance  
- Category-wise summary  


---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Bot Framework | Aiogram 3 |
| Language | Python 3 |
| Database | MongoDB |
| PDF Generator | ReportLab |
| Deployment | Local / VPS / Render / Railway |

---

## Installation


```bash
git clone https://github.com/Aadishranjan/Personal-Finance-Tracker-Bot.git
cd Personal-Finance-Tracker-Bot
pip install -r requirements.txt
```

Create a .env file add the following environment variables::
```bash
BOT_TOKEN=your_telegram_bot_token
MONGO_URI=your_mongodb_connection_string
DB_NAME=finance_bot
```

Run the bot 
```bash
python bot.py
```

### Bot Commands

| Command    | Description           |
| ---------- | --------------------- |
| `/start`   | Start bot & show menu |
| `/expense` | Add expense           |
| `/saving`  | Add savings           |
| `/summary` | View balance summary  |
| `/records` | Show all records      |
| `/report`  | Generate PDF report   |
