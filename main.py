from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__ = 'user'

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))


db.drop_all()
db.create_all()

user = UserModel(pk=1, first_name='Ivan', last_name='Petrov')
user1 = UserModel(pk=2, first_name='Roman', last_name='Romanov')

db.session.add(user1)
db.session.commit()

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8000, debug=True)
