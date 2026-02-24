from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    movies = []
    # আপনার দেওয়া এমবি সার্ভার লিঙ্ক
    base_url = "http://103.111.120.114:8096"
    
    try:
        # পাবলিক আইটেম এক্সেস করার লিঙ্ক
        api_url = f"{base_url}/emby/Items?Recursive=True&IncludeItemTypes=Movie&Fields=PrimaryImageAspectRatio,CanDownload&Limit=50"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            items = response.json().get('Items', [])
            for item in items:
                m_id = item.get('Id')
                movies.append({
                    "title": item.get('Name'),
                    "poster": f"{base_url}/emby/Items/{m_id}/Images/Primary",
                    "stream_url": f"{base_url}/emby/videos/{m_id}/stream.mp4",
                    "download_url": f"{base_url}/emby/Items/{m_id}/Download"
                })
    except Exception as e:
        print(f"Error: {e}")

    return render_template('movies.html', movies=movies)
