from os import abort

from flask import Flask, request

app = Flask(__name__)

from tictactoe import *


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        row = request.form["row"]
        column = request.form["column"]
        piece = request.form["piece"]
        app.logger.info("Placing the move in %s, %s and piece %s", row, column, piece)
        try:
            placeMove(row, column, piece)
        except:
            print("Invalid move")
    return '''
<html>
    <head>
        <titleTic tac toe</title>
    </head>
    <body>
        <div>
        ''' + getBoard() + '''
        </div>
        <form action="/" method="post">
          <label for="row">Row:</label><br>
          <input type="text" id="row" name="row"><br>
          <label for="column">Column:</label><br>
          <input type="text" id="column" name="column">
          <input type="text" id="piece" name="piece">
          <input type="submit" value="send movement">
        </form>
    </body>
</html>'''
