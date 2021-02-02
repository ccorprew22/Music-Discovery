from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port = int(os.getenv('PORT', 5000)),
            host = os.getenv('IP', '0.0.0.0'),
            debug = True
            )
