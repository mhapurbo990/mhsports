from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # নতুন এবং বিকল্প শক্তিশালী API সোর্স
    api_url = "https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json"
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    
    all_matches = []
    
    try:
        r = requests.get(api_url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # ডাটা ফরম্যাট অনুযায়ী লিস্টটি নেওয়া হচ্ছে
            all_matches = data.get('data', []) if isinstance(data, dict) else data
            
    except Exception as e:
        print(f"New API Error: {e}")
        all_matches = []
    
    # যদি ডাটা পাওয়া যায় তবেই সাইটে দেখাবে, নতুবা আগের সেই সিস্টেম চেক দেখাবে
    if not all_matches:
        all_matches = [
            {
                "title": "Searching New Source...",
                "team_a": "Server",
                "team_b": "Connecting",
                "team_a_img": "https://via.placeholder.com/100",
                "team_b_img": "https://via.placeholder.com/100",
                "is_live": "0",
                "date": "Please Wait",
                "stream_url": "#"
            }
        ]
    
    return render_template('index.html', matches=all_matches)
