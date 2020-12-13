'''
The factory module is imported at the bottom, and not at the top. Bottom
imports are a workaround for circular imports, a common problem with Flask
applications.

Since the factory module needs to import the app variable defined here,
putting the reciprocal import at the bottom avoids the error that results
from the mutual references between these two files.
'''

from flask import Flask

app = Flask(__name__)

from app import factory
