from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # Cricfy-এর সবচেয়ে লেটেস্ট এবং ফাস্ট API
    api_url = "https://api.cricfys.one/api/v3/live_matches"
    
    headers = {
        "User-Agent": "Cricfy-App/3.0",
        "Referer": "https://cricfys.one/",
        "Origin": "https://cricfys.one"
    }
    
    try:
        # এখানে আমরা v3 ব্যবহার করছি যা সরাসরি ডাটা দিবেই
        r = requests.get(api_url, headers=headers, timeout=10)
        json_data = r.json()
        matches = json_data.get('data', [])
        
        # যদি ডাটা খালি আসে তবে v2 ট্রাই করবে
        if not matches:
            r2 = requests.get("https://api.cricfys.one/api/v2/live_matches", headers=headers, timeout=5)
            matches = r2.json().get('data', [])
            
    except:
        matches = []
    
    return render_template('index.html', matches=matches)
