from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # এটি Cricfy-এর একটি বিকল্প সিক্রেট লিঙ্ক যা সরাসরি ব্লক হয় না
    url = "https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer": "https://cricfys.one/",
        "Origin": "https://cricfys.one"
    }
    
    matches = []
    
    try:
        # মেইন লিঙ্ক থেকে ট্রাই করা হচ্ছে
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            matches = data.get('data', []) if isinstance(data, dict) else data
            
        # যদি প্রথম লিঙ্কে ডাটা না থাকে, তবে ২য় একটি সরাসরি লিঙ্ক ট্রাই করবে
        if not matches:
            r2 = requests.get("https://api.cricfys.one/api/v2/live_matches", headers=headers, timeout=5)
            matches = r2.json().get('data', [])
            
    except:
        matches = []
    
    # যদি ডাটা পাওয়া যায় তবেই সাইটে দেখাবে, খালি দেখাবে না
    return render_template('index.html', matches=matches)
