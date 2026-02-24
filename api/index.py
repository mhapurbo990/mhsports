from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    # Ami nijei 3-ta channel manually pathachchi check korar jonno
    test_channels = [
        {"title": "PTV Sports", "logo": "https://i.imgur.com/82Nt8Dw.jpg", "url": "http://62.210.138.11:8000/play/ptvsports/index.m3u8"},
        {"title": "Star Sports 1", "logo": "https://i.imgur.com/NU0XdZv.jpg", "url": "http://62.210.138.11:8000/play/star1/index.m3u8"},
        {"title": "Willow HD", "logo": "https://i.imgur.com/TmzGuSD.jpg", "url": "http://62.210.138.11:8000/play/willow/index.m3u8"}
    ]
    return render_template('index.html', channels=test_channels)
