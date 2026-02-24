from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # সরাসরি Cricfy-এর আসল API লিঙ্ক
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://cricfys.one/"
    }
    
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        # যদি API কাজ না করে তবে বিকল্প ট্রাই করবে
        data = r.json().get('data', [])
    except:
        data = []
        
    return render_template('index.html', matches=data)
