from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # সরাসরি Cricfy অ্যাপের সোর্স লিঙ্ক
    api_url = "https://cricfys.one/api/v2/live_matches"
    
    headers = {
        "User-Agent": "CricfyApp/1.2",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive"
    }
    
    all_matches = []
    
    try:
        # সরাসরি রিকোয়েস্ট পাঠানো হচ্ছে
        r = requests.get(api_url, headers=headers, timeout=10)
        if r.status_code == 200:
            json_data = r.json()
            all_matches = json_data.get('data', [])
    except:
        # যদি মেইন লিঙ্ক কাজ না করে তবে বিকল্প ৩য় সোর্স
        try:
            r2 = requests.get("https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json", timeout=5)
            all_matches = r2.json()
            if isinstance(all_matches, dict):
                all_matches = all_matches.get('data', [])
        except:
            all_matches = []
    
    # যদি কোনো সোর্স থেকেই ডাটা না আসে, তবে আমরা অন্তত ইউজারকে "Loading" মেসেজ দেখাবো
    if not all_matches:
        all_matches = [
            {
                "title": "Server Syncing with Cricfy App...",
                "team_a": "Cricfy",
                "team_b": "App",
                "team_a_img": "https://via.placeholder.com/100",
                "team_b_img": "https://via.placeholder.com/100",
                "is_live": "0",
                "date": "Checking Live Feed",
                "stream_url": "#"
            }
        ]
    
    return render_template('index.html', matches=all_matches)
