# import flask and render template
from flask import Flask, render_template

# create instance of flask
app = Flask(__name__)

# specify url --> localhost:5000
@app.route('/')
def index():
    # return the index.html template
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
