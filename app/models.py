from . import db
from datetime import datetime
# from flask_login import UserMixin


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer)
    comment_content = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String)
    pitch_category=db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_comment = db.Column(db.String)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls, category):
        pitch = Pitch.query.filter_by(category=category).all()
        return pitch

    # def get_pitch(cls, id):
    #     pitch = Pitch.query.filter_by(pitch_id=id).all()
    #     return pitch

        # return pitch

    # def __repr__(self):
    #     return f'User {self.pitch_content}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'



def get_pitch(category):
    pitch = Pitch.query.filter_by(pitch_category=category).all()
    return pitch


def get_comments(id):
    comments = Comment.query.filter_by(id=id).all()