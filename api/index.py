from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # সম্পূর্ণ নতুন এবং আনব্লকড একটি এপিআই সোর্স
    api_url = "https://cricket.sportmonks.com/api/v2.0/livescores?api_token=YOUR_FREE_TOKEN"
    # নোট: যদি নিচের লিঙ্কটি কাজ না করে, তবে আমরা একটি পাবলিক রিপোজিটরি ব্যবহার করছি
    public_url = "https://raw.githubusercontent.com/lokesh-it/cricket-live-api/master/db.json"
    
    all_matches = []
    
    try:
        # আমরা পাবলিক গিটহাব ডাটাবেজ থেকে ডাটা নিচ্ছি যা কখনো ব্লক হয় না
        r = requests.get(public_url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # এই এপিআই-এর ফরম্যাট অনুযায়ী ডাটা নেওয়া হচ্ছে
            all_matches = data.get('matches', [])
    except:
        all_matches = []
    
    # আপনার HTML-এ ডাটা পাঠানো হচ্ছে
    return render_template('index.html', matches=all_matches)
