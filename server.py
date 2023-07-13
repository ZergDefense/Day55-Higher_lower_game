import random
from flask import Flask

number_to_guess = random.randint(0, 9)
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1 style="text-align: left">Guess a number between 0 and 9!</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200</img>'


@app.route('/<int:guess>')
def check_guess(guess):
    if int(guess) == number_to_guess:
        return '<h1 style="text-align: left, color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200</img>'
    elif int(guess) < number_to_guess:
        return '<h1 style="text-align: left, color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200</img>'
    else:
        return '<h1 style="text-align: left, color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200</img>'


if __name__ == "__main__":
    app.run(debug=True)
