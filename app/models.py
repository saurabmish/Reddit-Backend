from datetime import datetime
from app import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    karma = db.Column(db.Integer, default=1, nullable=False)

    # For Postgres and ORM
    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.email}', '{self.karma}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    community = db.Column(db.String(20), nullable=False)
    
    # For Postgres and ORM
    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.text}', '{self.published}', '{self.community}')"
