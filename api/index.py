from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # Sportzfy এর পাবলিক মিরর এপিআই লিঙ্ক
    url = "https://raw.githubusercontent.com/swadhin-it/Sportzfy-API/main/live.json"
    
    headers = {
        "User-Agent": "SportzfyApp/2.1",
        "Accept": "application/json"
    }
    
    matches = []
    
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # Sportzfy ডাটা ফরম্যাট অনুযায়ী লিস্ট নেওয়া হচ্ছে
            matches = data if isinstance(data, list) else data.get('data', [])
            
    except Exception as e:
        # যদি মেইন লিঙ্ক কাজ না করে তবে ব্যাকআপ
        try:
            r2 = requests.get("https://raw.githubusercontent.com/Cricfy/Cricfy-API/main/live.json")
            matches = r2.json()
        except:
            matches = []
            
    return render_template('index.html', matches=matches)
