from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # সরাসরি API কাজ না করলে আমরা অল্টারনেট প্রক্সি ব্যবহার করছি
    api_url = "https://api.allorigins.win/get?url=" + requests.utils.quote("https://api.cricfys.one/api/v2/live_matches")
    
    try:
        r = requests.get(api_url, timeout=15)
        if r.status_code == 200:
            # AllOrigins ডাটা 'contents' এর ভেতরে স্ট্রিং হিসেবে পাঠায়
            contents = r.json().get('contents')
            import json
            data = json.loads(contents)
            matches = data.get('data', [])
        else:
            matches = []
    except:
        matches = []
    
    return render_template('index.html', matches=matches)
