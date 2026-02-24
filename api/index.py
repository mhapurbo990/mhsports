from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # সরাসরি Cricfy এর পাবলিক API লিঙ্ক
    api_url = "https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json"
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    
    all_matches = []
    
    try:
        r = requests.get(api_url, headers=headers, timeout=8)
        if r.status_code == 200:
            data = r.json()
            all_matches = data if isinstance(data, list) else data.get('data', [])
    except:
        all_matches = []

    # যদি উপরের API কাজ না করে, তবে নিচের এই ম্যাচগুলো আপনার সাইটে দেখাবেই (গ্যারান্টিড)
    if not all_matches:
        all_matches = [
            {
                "title": "API Connection Error - Showing Demo",
                "team_a": "System",
                "team_b": "Active",
                "team_a_img": "https://via.placeholder.com/100",
                "team_b_img": "https://via.placeholder.com/100",
                "is_live": "1",
                "date": "Checking Fix",
                "stream_url": "#"
            },
            {
                "title": "Upcoming Feature",
                "team_a": "MH",
                "team_b": "Sports",
                "team_a_img": "https://via.placeholder.com/100",
                "team_b_img": "https://via.placeholder.com/100",
                "is_live": "0",
                "date": "Coming Soon",
                "stream_url": "#"
            }
        ]
    
    return render_template('index.html', matches=all_matches)
