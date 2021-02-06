'''
The factory module is imported at the bottom, and not at the top. Bottom
imports are a workaround for circular imports, a common problem with Flask
applications.

Since the factory module needs to import the app variable defined here,
putting the reciprocal import at the bottom avoids the error that results
from the mutual references between these two files.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Application 
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# URI Format: dialect + driver + "://" + username + ":" + password + "@" + host + ":" + str(port) + "/" + database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://reddit_admin:admin123@localhost:5432/redditdb'
db = SQLAlchemy(app)

from app import factory, accounts, posts, models
