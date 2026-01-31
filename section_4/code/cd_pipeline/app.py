from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media.tenor.com/iALgQGVcpz4AAAAj/scemer-staring-cat.gif",
   "https://media.tenor.com/KwvyrFpeFcwAAAAi/bongo-cat-sweet.gif",
   "https://media.tenor.com/vnkvXD3l-vgAAAAi/happy-cat.gif",
   "https://media1.tenor.com/m/WsWej1C3ePYAAAAC/yippee-cat-kitty.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
