from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # এটি একটি ওপেন স্পোর্টস এপিআই যা কখনো ব্লক হয় না
    url = "https://raw.githubusercontent.com/lokesh-it/cricket-live-api/master/db.json"
    
    matches = []
    
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # তারা ডাটাকে 'matches' কি-এর মধ্যে রাখে
            raw_matches = data.get('matches', [])
            
            # আপনার ডিজাইনের সাথে ম্যাচ করানোর জন্য ডাটা ফরম্যাট করা হচ্ছে
            for m in raw_matches:
                matches.append({
                    "title": m.get('series_name', 'Cricket Match'),
                    "team_a": m.get('team1', 'Team A'),
                    "team_b": m.get('team2', 'Team B'),
                    "team_a_img": "https://p.nomics.com/wp-content/uploads/2018/11/n-logo.png",
                    "team_b_img": "https://p.nomics.com/wp-content/uploads/2018/11/n-logo.png",
                    "is_live": "1" if m.get('is_live') else "0",
                    "date": m.get('match_date', 'Today'),
                    "stream_url": "#"
                })
    except:
        matches = []
        
    return render_template('index.html', matches=matches)
