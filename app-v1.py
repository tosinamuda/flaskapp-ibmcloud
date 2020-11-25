import os
from os import environ 
from flask import Flask, render_template ,redirect, url_for, request
from flask_db2 import DB2
from jinja2 import Template
from dotenv import load_dotenv
import itertools
load_dotenv()


todos = [ 
    {"ID": 1, "TEXT": "Deploy Code"},
    {"ID": 2, "TEXT": "Attend Meetup"},
    {"ID": 3, "TEXT": "Write Text"},
    {"ID": 4, "TEXT": "Complete Python Course"},
    {"ID": 5, "TEXT": "Refctor Code"},
    {"ID": 6, "TEXT": "Sprint Planning"},
]
app = Flask(__name__)
app.config['DB2_DATABASE'] = environ.get('DB2_DATABASE')
app.config['DB2_HOSTNAME'] = environ.get('DB2_HOSTNAME')
app.config['DB2_PORT'] = environ.get('DB2_PORT')
app.config['DB2_PROTOCOL'] = environ.get('DB2_PROTOCOL')
app.config['DB2_USER'] = environ.get('DB2_USER')
app.config['DB2_PASSWORD'] = environ.get('DB2_PASSWORD')
port = int(os.getenv('PORT', 8000))
db = DB2(app)


@app.route("/", methods = ['GET', 'POST'])
def home():
    cursor = db.connection.cursor()
    if request.method == 'POST':
        todoItem = request.form.get('todoText')
        todos.append({"ID": 4, "TEXT": todoItem })
        return redirect(url_for('home'), todos=todos)  
    else: 
        return render_template("todo.html", todos=todos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)