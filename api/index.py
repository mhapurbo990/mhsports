from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # CricHD এর জিপ ফাইলে থাকা চ্যানেলের লিস্ট (Automated Source)
    channels = [
        {"title": "Star Sports 1 Hindi", "id": "starhindi", "img": "https://i.imgur.com/82Nt8Dw.jpg"},
        {"title": "PTV Sports", "id": "ptvpk", "img": "https://is1-ssl.mzstatic.com/image/thumb/Purple114/v4/c2/9b/0a/c29b0adf-875f-37b0-3e08-7ee9b62b8b02/AppIcon-1x_U007emarketing-85-220-0-8.jpeg/1024x1024bb.png"},
        {"title": "Ten Sports", "id": "tenspk", "img": "https://gumlet.assettype.com/afaqs%2Fimport%2Fall%2Fnews%2Fimages%2Fnews_story_grfx%2F2015%2F44872_1_home_big.jpg"},
        {"title": "Willow HD", "id": "willowusa", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmzGuSDh0BzfQs_d_lUEuPBB3Bblbu-PhtvQ&usqp=CAU"},
        {"title": "Sky Sports Main Event", "id": "skysme", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Sky-sports-main-event.jpg"}
    ]
    
    matches = []
    for ch in channels:
        matches.append({
            "title": ch['title'],
            "team_a": "Live",
            "team_b": "Sports",
            "team_a_img": ch['img'],
            "team_b_img": ch['img'],
            "is_live": "1",
            "date": "24/7 Live",
            "stream_url": f"https://mhsports-streaming.vercel.app/play.php?cricid={ch['id']}" # এটি একটি উদাহরণ লিঙ্ক
        })
        
    return render_template('index.html', matches=matches)
