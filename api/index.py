from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # Cricfy অ্যাপের আসল ইন্টারনাল এপিআই লিঙ্ক
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    
    # অ্যাপের মতো লুক তৈরি করা (Headers)
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Build/SD1A.210817.036)",
        "Host": "api.cricfys.one",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    all_matches = []
    
    try:
        # সরাসরি অ্যাপের সার্ভারে রিকোয়েস্ট পাঠানো হচ্ছে
        response = requests.get(api_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            json_data = response.json()
            # অ্যাপ থেকে আসা সব লাইভ ও আপকামিং ম্যাচ
            all_matches = json_data.get('data', [])
    except Exception as e:
        print(f"Error: {e}")
        all_matches = []
    
    # আপনার HTML ডিজাইনে ডাটা পাঠানো হচ্ছে
    return render_template('index.html', matches=all_matches)
