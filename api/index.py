from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='../templates')

# Emby Server URL
BASE_URL = "http://103.111.120.114:8096"

@app.route('/')
def get_movies():
    movies = []
    try:
        # Emby-r public access point use kore movie fetch kora
        # Ekhane amra 'UserId' pathachchi na karon Guest access chalu ache
        search_url = f"{BASE_URL}/emby/Items?Recursive=True&IncludeItemTypes=Movie&Fields=PrimaryImageAspectRatio,CanDownload,Path&Limit=100"
        
        r = requests.get(search_url, timeout=15)
        
        if r.status_code == 200:
            data = r.json()
            items = data.get('Items', [])
            for item in items:
                m_id = item.get('Id')
                movies.append({
                    "title": item.get('Name'),
                    "poster": f"{BASE_URL}/emby/Items/{m_id}/Images/Primary",
                    "stream_url": f"{BASE_URL}/emby/videos/{m_id}/stream.mp4",
                    "download_url": f"{BASE_URL}/emby/Items/{m_id}/Download"
                })
        else:
            print(f"Server error: {r.status_code}")
    except Exception as e:
        print(f"Request failed: {e}")

    return render_template('movies.html', movies=movies)
