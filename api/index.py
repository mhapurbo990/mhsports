from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # CricHD ebong professional source theke automated channel list
    # Ei link-ti block hoy na ebong auto-update hoy
    api_url = "https://raw.githubusercontent.com/Mohd-Tauseef-khan/CricHD/refs/heads/main/crichd.m3u"
    
    channels = []
    try:
        r = requests.get(api_url, timeout=10)
        if r.status_code == 200:
            lines = r.text.split('\n')
            for i in range(len(lines)):
                if lines[i].startswith('#EXTINF'):
                    # Logo ebong Name ber korar logic
                    name = lines[i].split(',')[-1].strip()
                    logo = ""
                    if 'tvg-logo="' in lines[i]:
                        logo = lines[i].split('tvg-logo="')[1].split('"')[0]
                    
                    # Streaming link (Next line)
                    stream_link = lines[i+1].strip() if (i+1) < len(lines) else "#"
                    
                    if name and stream_link.startswith('http'):
                        channels.append({
                            "title": name,
                            "team_a": "Live",
                            "team_b": "Sports",
                            "team_a_img": logo if logo else "https://via.placeholder.com/100",
                            "team_b_img": logo if logo else "https://via.placeholder.com/100",
                            "is_live": "1",
                            "date": "24/7 Live",
                            "stream_url": stream_link
                        })
    except:
        channels = []

    # Jodi API fail kore, tobe top 5 channels backup hishebe thakbe
    if not channels:
        channels = [
            {"title": "Star Sports 1", "team_a
