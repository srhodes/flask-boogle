from flask import Flask, render_template
from boggle import Boggle

app = Flask(__name__)


# import board from bobble file

# generate route using view function
app.route('/board')
def making_a_board():
    board = boggle_game.make_board()
    # try to put in a session
    print('boggle_game.make_board()')
    return render_template('board.html', board = board)

# once displayed board is working add a form where user submit a guessing word
app.route('/form')
def form_of_user():
    
    return render_template('form.html')