import os
from os import environ 
from flask import Flask, render_template ,redirect, url_for, request
from flask_db2 import DB2
from jinja2 import Template
from dotenv import load_dotenv
import itertools
load_dotenv()


todos = [ 
    {"id": 1, "text": "Deploy Code"},
    {"id": 2, "text": "Attend Meetup"},
    {"id": 3, "text": "Write Text"},
    {"id": 4, "text": "Complete Python Course"},
    {"id": 5, "text": "Refctor Code"},
    {"id": 6, "text": "Sprint Planning"},
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
        sql = '''INSERT INTO  "VKG09605"."to-dos" ("ID","TEXT") VALUES (?, ?)'''
        val = (1, todoItem)
        cursor.execute(sql, val )
        db.connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()
        return redirect(url_for('home'))    # I'm just making this up
    else: 
        query = '''SELECT "ID", "TEXT" FROM "VKG09605"."to-dos";'''
        cursor.execute(query)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row))  
            for row in cursor.fetchall()]
        print(data);
        cursor.close()
        return render_template("todo.html", todos=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)