from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    api_url = "https://api.cricfys.one/api/v2/live_matches"
    try:
        r = requests.get(api_url, timeout=10)
        matches = r.json().get('data', [])
    except:
        matches = []
    return render_template('index.html', matches=matches)
