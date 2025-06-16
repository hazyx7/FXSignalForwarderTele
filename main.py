import json
import asyncio
import re
import logging
import requests
from telethon import TelegramClient, events
from colorama import init, Fore, Style

# === Initialize Colorama ===
init(autoreset=True)

# === Load Configuration ===
with open("info.json", "r") as f:
    config = json.load(f)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
SOURCE_CHAT_IDS = config["source_chat_ids"]
TARGET_CHAT_IDS = config["target_chat_ids"]
TWELVE_DATA_API_KEY = config["twelve_data_api_key"]
SESSION_NAME = config["session_name"]

# === Logging Setup ===
logging.basicConfig(
    level=logging.INFO,
    filename="bot_log.txt",
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# === Create Telegram Client ===
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# === Get XAUUSD Current Price ===
def get_xauusd_price():
    try:
        response = requests.get(
            f"https://api.twelvedata.com/price?symbol=XAU/USD&apikey={TWELVE_DATA_API_KEY}"
        )
        data = response.json()
        return data.get("price", "Unavailable")
    except Exception as e:
        logging.error(f"Price API Error: {e}")
        return "Unavailable"

# === Format Signal ===
def format_signal(text):
    lines = text.splitlines()
    cleaned = []
    tp_count = 1
    found_buy_sell = False
    found_tp = False

    price = get_xauusd_price()

    for line in lines:
        line = line.strip()
        if not line or "money management" in line.lower():
            continue

        # Buy/Sell
        if re.search(r'\bbuy\b|\bsell\b', line, re.IGNORECASE):
            line = re.sub(r'\bgold\b', 'XAUUSD', line, flags=re.IGNORECASE)
            cleaned.append(f"📉 XAUUSD Current Price: {price}\n\n{line}")
            found_buy_sell = True

        # SL
        elif re.search(r'\bsl\b|stop loss', line, re.IGNORECASE):
            sl_val = re.search(r'\d+\.?\d*', line)
            if sl_val:
                cleaned.append(f"\n🛑 Stop Loss: {sl_val.group(0)}")

        # TP
        elif 'tp' in line.lower():
            match = re.search(r'(tp\s*\d*):?\s*(open|\d+\.?\d*)', line, re.IGNORECASE)
            if match:
                tp_val = match.group(2)
                cleaned.append(f"🎯 Take Profit {tp_count}: {tp_val}")
                tp_count += 1
                found_tp = True

        # Entry Zone
        elif re.search(r'\d+\.\d+\s*-\s*\d+\.\d+', line):
            cleaned.append(f"📍 Entry Zone: {line}")

    if found_buy_sell and found_tp:
        return "\n".join(cleaned)
    return None

# === Handle New Messages ===
@client.on(events.NewMessage(chats=SOURCE_CHAT_IDS))
async def handler(event):
    signal = format_signal(event.raw_text)
    if signal:
        for target in TARGET_CHAT_IDS:
            try:
                await client.send_message(target, signal)
                print(Fore.GREEN + f"[✓] Forwarded to {target}")
            except Exception as e:
                logging.error(f"Sending Error to {target}: {e}")
                print(Fore.RED + f"[✗] Error sending to {target}")
    else:
        print(Fore.YELLOW + "[~] Skipped message (not valid signal)")

# === Main Loop ===
async def main():
    print(Fore.CYAN + Style.BRIGHT + "\n🚀 XAUUSD Signal Forwarder is running...\n")
    try:
        await client.run_until_disconnected()
    except Exception as e:
        logging.error(f"Main Loop Error: {e}")
        print(Fore.RED + f"[✗] Unexpected error: {e}")
        await asyncio.sleep(10)

# === Start Script ===
if __name__ == "__main__":
    client.start()
    asyncio.get_event_loop().run_until_complete(main())
