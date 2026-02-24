from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # সরাসরি আপনার রিপোজিটরির ডাটা ফাইল (এটি ব্লক হওয়া অসম্ভব)
    # আপনার ইউজারনেম এবং রিপোজিটরি নাম অনুযায়ী লিঙ্কটি হবে
    url = "https://raw.githubusercontent.com/আপনার-ইউজারনেম/আপনার-রিপো-নাম/main/matches.json"
    
    try:
        r = requests.get(url, timeout=5)
        all_matches = r.json()
    except:
        all_matches = []
        
    return render_template('index.html', matches=all_matches)
