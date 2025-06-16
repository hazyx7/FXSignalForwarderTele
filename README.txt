===================================================
🔁 TELEGRAM SIGNAL FORWARDER BOT
===================================================

This bot reads trading signals from specified Telegram groups or channels,
formats the message (e.g., Buy/Sell XAUUSD), fetches live XAUUSD price 
from Twelve Data, and forwards the cleaned message to another Telegram group.

---------------------------------------------------
🛠 REQUIREMENTS
---------------------------------------------------
- Python
- Install required modules by opening cmd in the folder and pasting this:

    pip install telethon aiohttp colorama

---------------------------------------------------
⚙️ SETUP INSTRUCTIONS
---------------------------------------------------

1. GET YOUR TELEGRAM API CREDENTIALS
   - Go to https://my.telegram.org/auth
   - Log in with your Telegram number
   - Click "API Development Tools"
   - Fill in the form and save your "API ID" and "API Hash"

2. GET YOUR TWELVE DATA API KEY (for live XAUUSD price)
   - Sign up at: https://twelvedata.com/signup
   - Copy your API key

3. EDIT THE `info.json` FILE
   - Open `info.json` and update your credentials like this:

    {
      "api_id": YOUR_API_ID,
      "api_hash": "YOUR_API_HASH",
      "source_chat_ids": [-1001234567890],
      "target_chat_ids": [-1009876543210],
      "twelve_data_api_key": "YOUR_TWELVE_DATA_API_KEY",
      "session_name": "forwarder_session"
    }

   - To find your chat IDs, run the helper script below.

---------------------------------------------------
🔍 FINDING TELEGRAM CHAT/GROUP IDs
---------------------------------------------------
1. Open the folder and run:
      chat_id_grabber.py

3. The chat ID will appear in your terminal.
4. Copy it
---------------------------------------------------
🚀 RUNNING THE BOT
---------------------------------------------------
1. Double-click `run.py`
2. On first run, it will ask for your phone number or bot token.
3. It saves your session so next time it runs automatically.
4. The bot will start listening for signals and forward them
   to the specified group with real-time XAUUSD price.

---------------------------------------------------
📦 SIGNAL EXAMPLE
---------------------------------------------------
Incoming Message:
    gold buy now @ 3416.50 - 3413
    sl: 3310
    tp: 3425
    tp: 3435

Forwarded Message:
    📈 XAUUSD Current Price: 3416.50

    Buy XAUUSD: 3416.50 - 3413

    Stop Loss: 3310

    Take Profit 1: 3425
    Take Profit 2: 3435

---------------------------------------------------
✅ TIPS
---------------------------------------------------
- Edit only the `info.json` file to update settings.
- Logs are saved in `bot_log.txt`
- To run multiple bots, just use different `session_name`s.
- Don't share your API credentials publicly.

---------------------------------------------------
🤝 CREDITS
---------------------------------------------------
- Built by (https://t.me/hazyx777)
- Built using Telethon (https://github.com/LonamiWebs/Telethon)
- Real-time price (https://twelvedata.com)

===================================================
