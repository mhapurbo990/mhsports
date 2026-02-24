from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    url = "https://api.cricfys.one/api/v2/live_matches"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        r = requests.get(url, headers=headers, timeout=10)
        all_matches = r.json().get('data', [])
    except:
        all_matches = []
        
    # যদি API একদমই কাজ না করে, তবে এই নিচের অংশটি সাইট খালি রাখবে না
    if not all_matches:
        all_matches = [
            {
                "title": "System Check - API Syncing",
                "team_a": "Cricfy App",
                "team_b": "Your Web",
                "team_a_img": "https://via.placeholder.com/100",
                "team_b_img": "https://via.placeholder.com/100",
                "is_live": "0",
                "date": "Waiting for Data",
                "stream_url": "#"
            }
        ]
    
    return render_template('index.html', matches=all_matches)
