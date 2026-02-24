from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    live_matches = []
    upcoming_matches = []
    
    try:
        r = requests.get(api_url, timeout=10)
        data = r.json().get('data', [])
        
        # লাইভ এবং আপকামিং ম্যাচ আলাদা করা
        for m in data:
            if m.get('is_live') == "1":
                live_matches.append(m)
            elif m.get('is_live') == "0":
                upcoming_matches.append(m)
    except:
        pass
    
    return render_template('index.html', live=live_matches, upcoming=upcoming_matches)
