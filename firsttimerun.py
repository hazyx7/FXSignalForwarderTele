import os
import subprocess
import sys

REQUIRED_PACKAGES = [
    "telethon",
    "requests",
    "colorama"
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    print("Installing required Python packages...\n")

    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
            print(f"[✓] Already installed: {package}")
        except ImportError:
            print(f"[...] Installing: {package}")
            try:
                install(package)
                print(f"[+] Successfully installed: {package}")
            except Exception as e:
                print(f"[✗] Failed to install {package}: {e}")

    print("\n====== ✅ SETUP COMPLETE ======")
    print(" ")
    print("📘 Guide Below:")
    print("1. 🔑 Get your Telegram API credentials:")
    print("   👉 https://my.telegram.org/auth")
    print("   → Log in, go to 'API Development Tools'")
    print("   → Create an app to get your api_id and api_hash")
    print(" ")
    print("2. 📊 Get your FREE Twelve Data API key:")
    print("   👉 https://twelvedata.com/signup")
    print("   → Sign up, then copy your API key from the dashboard")
    print(" ")
    print("3. ✏️ Edit your credentials inside 'info.json'")
    print("4. 🚀 Double-click run.py to start the bot")
    print("===============================")


    # Pause at the end
    try:
        input("\nPress Enter to exit...")
    except:
        os.system("pause")  # Fallback for Windows cmd

if __name__ == "__main__":
    main()
