from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://cricfys.one/"
    }
    
    all_matches = []
    
    try:
        # urllib ব্যবহার করে ডেটা ফেচ করা হচ্ছে
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.getcode() == 200:
                raw_data = response.read().decode('utf-8')
                json_data = json.loads(raw_data)
                all_matches = json_data.get('data', [])
    except Exception as e:
        # মেইন লিঙ্ক কাজ না করলে ব্যাকআপ লিঙ্ক
        try:
            backup_url = "https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json"
            with urllib.request.urlopen(backup_url, timeout=5) as backup_res:
                raw_data = backup_res.read().decode('utf-8')
                json_data = json.loads(raw_data)
                all_matches = json_data.get('data', []) if isinstance(json_data, dict) else json_data
        except:
            all_matches = []
    
    # আপনার HTML ডিজাইনে সব ম্যাচ (Live + Upcoming) পাঠানো হচ্ছে
    return render_template('index.html', matches=all_matches)
