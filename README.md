
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

## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) [2025] [Aadish ranjan]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.