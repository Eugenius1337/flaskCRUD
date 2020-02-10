# import flask and render template
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create instance of flask
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<Grocery %r>' % self.name

# specify url --> localhost:5000
@app.route('/')
def index():
    # return the index.html template
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
