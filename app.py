# load packages
from flask import Flask, render_template

# init app
app = Flask(__name__)

#routes
@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submited.html')
def submited():
    return "hej"