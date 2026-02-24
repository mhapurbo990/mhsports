from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # সরাসরি এবং সবচেয়ে নির্ভরযোগ্য লিঙ্ক
    url = "https://api.cricfys.one/api/v2/live_matches"
    
    try:
        # কোনো জটিল হেডার বা ফিল্টার ছাড়া সরাসরি রিকোয়েস্ট
        r = requests.get(url, timeout=10)
        data = r.json()
        
        # 'data' কি এর ভেতর থেকে সব ম্যাচ (Live + Upcoming) নিচ্ছে
        all_matches = data.get('data', [])
        
    except:
        all_matches = []
    
    # সব ম্যাচ আপনার HTML ডিজাইনে পাঠিয়ে দিচ্ছে
    return render_template('index.html', matches=all_matches)
