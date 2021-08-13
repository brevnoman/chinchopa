from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5



@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    avatar_link = db.Column(db.String, default="https://secure.gravatar.com/avatar/36772dde715344ba399b9e7b032a1066")

    posts = db.relationship('Posts', backref=db.backref('author'), lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        return self.avatar_link+f"?d=identicon&s={size}"

    def __repr__(self):
        return '<User {}, email{}, password {}>'.format(self.username, self.email, self.password_hash)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.String, index=True, default=str(datetime.utcnow()))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return '<Post {}>'.format(self.body)
