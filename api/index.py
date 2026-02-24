from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    
    # ব্রাউজার হিসেবে পরিচয় দেওয়ার জন্য হেডার
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # হেডারসহ রিকোয়েস্ট পাঠানো হচ্ছে
        response = requests.get(api_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            json_data = response.json()
            all_matches = json_data.get('data', [])
        else:
            all_matches = []
            
    except Exception as e:
        print(f"Error: {e}")
        all_matches = []
    
    return render_template('index.html', matches=all_matches)
