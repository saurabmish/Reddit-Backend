from datetime import datetime
from app import db

class User(db.Model):
    """Table Structure

    There is a one-to-many relationship between user and post, i.e., a
    post cannot exist without a user.
    'backref' is similar to adding another column to Post. It is used
    get the user who created the post. 'lazy' will load the data as
    necessary

    Objects of this class will be represented with their database
    columns (created by this model).
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    karma = db.Column(db.Integer, default=1, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.email}', '{self.karma}')"

class Post(db.Model):
    """Table Structure

    UTC is the most commonly used time format in databases. This
    function will be passed as an argument and NOT be evaluated.

    Objects of this class will be represented with their database
    columns (created by this model).
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    community = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.text}', '{self.published}', '{self.community}')"
