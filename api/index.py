from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # Cricfy-এর মেইন এবং বিকল্প API লিঙ্ক
    api_url = "https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json"
    
    headers = {
        "User-Agent": "CricfyApp/1.0",
        "Accept": "*/*"
    }
    
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        # যদি এই লিঙ্কে ডেটা সরাসরি লিস্ট আকারে থাকে
        matches = r.json()
        
        # যদি ডেটা 'data' কি-এর ভেতরে থাকে
        if isinstance(matches, dict):
            matches = matches.get('data', [])
            
    except:
        matches = []
    
    return render_template('index.html', matches=matches)
