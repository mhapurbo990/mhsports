from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    all_matches = []
    
    try:
        # সরাসরি API কল করে সব ডেটা নিয়ে আসবে
        r = requests.get(api_url, timeout=10)
        json_data = r.json()
        
        # API এর ভেতরে 'data' লিস্টে যা আছে সব নিয়ে নিবে
        all_matches = json_data.get('data', [])
        
    except Exception as e:
        print(f"Error: {e}")
        all_matches = []
    
    # কোনো ভাগাভাগি নেই, সব ম্যাচ একসাথে পাঠিয়ে দিবে
    return render_template('index.html', matches=all_matches)
