from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # এটি একটি ওপেন সোর্স এপিআই যা ক্রিকএইচডি বা স্পোর্টজফাইয়ের মতো ডেটা দেয়
    api_url = "https://raw.githubusercontent.com/the-m9/sport-api/main/data.json"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    matches = []
    
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # ডাটা প্রসেসিং
            raw_data = data.get('matches', []) if isinstance(data, dict) else data
            
            for m in raw_data:
                matches.append({
                    "title": m.get('series_name') or m.get('title') or "Cricket Match",
                    "team_a": m.get('team_a') or m.get('team1') or "Team A",
                    "team_b": m.get('team_b') or m.get('team2') or "Team B",
                    "team_a_img": m.get('team_a_img') or "https://via.placeholder.com/100",
                    "team_b_img": m.get('team_b_img') or "https://via.placeholder.com/100",
                    "is_live": "1" if str(m.get('is_live')) == "1" or m.get('status') == 'live' else "0",
                    "date": m.get('time') or m.get('date') or "Live Now",
                    "stream_url": m.get('url') or "#"
                })
    except:
        matches = []
    
    return render_template('index.html', matches=matches)
