from datetime import datetime
from app import db

class Post(db.Model):
    """Table Structure

    UTC is the most commonly used time format in databases. This
    function will be passed as an argument and NOT be evaluated.

    Objects of this class will be represented with their database
    columns (created by this model).
    """
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    community = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.text}', '{self.published}', '{self.community}')"
