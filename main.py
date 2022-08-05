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

    def __repr__(self):
        return f'{self.pk}, {self.first_name}'


class PhoneModel(db.Model):
    __tablename__ = 'phone'

    pk = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.pk}, {self.number}'


db.drop_all()
db.create_all()

user = UserModel(pk=1, first_name='Ivan', last_name='Petrov')
user1 = UserModel(pk=2, first_name='Roman', last_name='Romanov')
# super_user = [user, user1]

phone = PhoneModel(pk=1, number='1234567890')

db.session.add_all([user, user1, phone])
db.session.commit()


user_from_db = db.session.query(UserModel).get(1)
phone_from_db = db.session.query(PhoneModel).get(1)
print(user_from_db)
print(type(phone_from_db))

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8000, debug=True)
