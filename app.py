# load packages
import os
import sqlite3
from flask import Flask, render_template, url_for, request
from contextlib import closing

# init app
app = Flask(__name__)

#routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            con = sqlite3.connect("database.db")
            try:
                date = request.form['date']
                vocation = request.form['vocation']
                cur = con.cursor()
                cur.execute("INSERT INTO schedule (date, vocation) values (?,?)", (date, vocation) )
                con.commit()
                state = 0
            except Exception as e: 
                con.rollback()
                state = 1
        except Exception as e: 
            state = 1
        finally:
            return render_template("index.html", state = state)
    else:
        print(request.form['date'])

if __name__ == '__main__':
    app.run(debug=True)