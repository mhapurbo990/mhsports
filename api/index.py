from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # এটি একটি ওপেন সোর্স ক্রিকেট এপিআই যা কখনো ব্লক হয় না
    url = "https://cricket-live-data.vercel.app/matches" 
    
    matches = []
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        raw_matches = data.get('matches', [])
        
        for m in raw_matches:
            matches.append({
                "title": m.get('event', 'Cricket Match'),
                "team_a": m.get('team1', 'TBA'),
                "team_b": m.get('team2', 'TBA'),
                "team_a_img": "https://p.nomics.com/wp-content/uploads/2018/11/n-logo.png",
                "team_b_img": "https://p.nomics.com/wp-content/uploads/2018/11/n-logo.png",
                "is_live": "1" if m.get('status') == 'live' else "0",
                "date": m.get('date', 'Today'),
                "stream_url": "#" 
            })
    except:
        matches = []
        
    return render_template('index.html', matches=matches)
