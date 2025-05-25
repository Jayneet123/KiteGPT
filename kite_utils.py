from pymongo import MongoClient
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import os
import json
import logging
from kiteconnect import KiteConnect
from datetime import datetime

TOKEN_FILE = "kite_token.json"

load_dotenv()

api_key = os.getenv("KITE_API")
api_secret = os.getenv("KITE_API_SECRET")

def save_token(data):
    with open(TOKEN_FILE, "w") as f:
        json.dump({
            "access_token": data["access_token"],
            "timestamp": datetime.now().isoformat()
        }, f)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return json.load(f)
    return None

def initialize_kite():
    kite = KiteConnect(api_key=api_key)
    
    # Try to reuse token
    token_data = load_token()
    if token_data:
        kite.set_access_token(token_data["access_token"])
        try:
            # Test if token works by calling a harmless endpoint
            kite.profile()
            print("✅ Reused existing access_token")
            return kite
        except Exception as e:
            print("⚠️ Token expired or invalid. Login required.")
    
    # Token doesn't exist or is invalid → Ask user to login
    login_url = kite.login_url()
    print("🔗 Login here:", login_url)
    request_token = input("Paste request_token from URL: ").strip()

    # Exchange token
    try:
        session = kite.generate_session(request_token, api_secret=api_secret)
        kite.set_access_token(session["access_token"])
        save_token(session)
        print("✅ New token saved successfully.")
        return kite
    except Exception as e:
        print("❌ Token generation failed:", e)
        return None

