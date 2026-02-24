from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # CricHD এর লেটেস্ট অটোমেটেড এপিআই সোর্স
    url = "https://raw.githubusercontent.com/sabbiriptv/CricHD/main/crichd.m3u"
    
    channels = []
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            lines = r.text.split('\n')
            for i in range(len(lines)):
                if lines[i].startswith('#EXTINF'):
                    # নাম এবং লোগো বের করার নিখুঁত লজিক
                    name = lines[i].split(',')[-1].strip()
                    logo = ""
                    if 'tvg-logo="' in lines[i]:
                        logo = lines[i].split('tvg-logo="')[1].split('"')[0]
                    
                    stream_link = lines[i+1].strip() if (i+1) < len(lines) else "#"
                    
                    if name and stream_link.startswith('http'):
                        channels.append({
                            "title": name,
                            "logo": logo if logo else "https://via.placeholder.com/150",
                            "stream_url": stream_link
                        })
    except:
        channels = []
        
    return render_template('index.html', matches=channels)
