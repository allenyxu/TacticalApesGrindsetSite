from flask import Flask, render_template
import random, requests

app = Flask(__name__)

backgrounds = ["https://cdn.discordapp.com/attachments/593331093130838016/858477082550730762/x0t55697o4z61_1.jpeg", "https://cdn.discordapp.com/attachments/593331093130838016/858477132388237329/x0t55697o4z61.jpeg"]
monkeybackgrounds = ["https://i.pinimg.com/originals/1b/46/1a/1b461ad3fe0034b06138b88299d842dd.jpg", "https://thumbs.dreamstime.com/b/cute-cartoon-baby-monkey-banana-hugging-kawaii-character-drawing-isolated-vector-clip-art-illustration-142243904.jpg"]
@app.route('/')
def index():
    #response = requests.get('https://nekos.life/api/v2/img/wallpaper')
    #background = response.json()['url']
    background = random.choice(monkeybackgrounds)
    return render_template("home.html", background=background)

@app.route('/dino')
def dino():
    background = random.choice(backgrounds)
    return render_template("dino.html", background=background)
if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5000")