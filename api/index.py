from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # Cricfy-এর আসল API লিঙ্ক
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://cricfys.one/"
    }
    
    all_matches = []
    
    try:
        # মেইন সার্ভার থেকে ডাটা নেওয়ার চেষ্টা
        r = requests.get(api_url, headers=headers, timeout=10)
        if r.status_code == 200:
            all_matches = r.json().get('data', [])
        
        # যদি মেইন সার্ভার খালি থাকে, তবে ব্যাকআপ লিঙ্ক চেক করবে
        if not all_matches:
            backup_url = "https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json"
            r2 = requests.get(backup_url, timeout=5)
            data2 = r2.json()
            all_matches = data2.get('data', []) if isinstance(data2, dict) else data2
            
    except Exception as e:
        print(f"API Error: {e}")
        all_matches = []
    
    # সব ডাটা (Live + Upcoming) একসাথে পাঠিয়ে দিবে
    return render_template('index.html', matches=all_matches)
