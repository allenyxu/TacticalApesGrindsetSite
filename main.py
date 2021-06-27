from flask import Flask, render_template
import random

app = Flask(__name__)

backgrounds = ["https://cdn.discordapp.com/attachments/593331093130838016/858477082550730762/x0t55697o4z61_1.jpeg", "https://cdn.discordapp.com/attachments/593331093130838016/858477132388237329/x0t55697o4z61.jpeg"]

@app.route('/')
def index():
    background = random.choice(backgrounds)
    return render_template("home.html", background=background)
if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5000")