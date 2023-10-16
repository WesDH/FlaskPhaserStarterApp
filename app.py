from flask import Flask, render_template

app = Flask(__name__)

# Based off of http://phaser.io/tutorials/making-your-first-phaser-3-game/
@app.route('/')
def first_game():  # put application's code here
    return render_template("first_game.html")

if __name__ == '__main__':
    app.run(debug=True)