# Setup

+ Install PostgreSQL:

  `brew install postgresql`

+ View installed location:

  `which postgres`

+ Check if postgres service is running:

  `pg_ctl -D /usr/local/var/postgres status`

+ Manually start (or stop) services:

  `pg_ctl -D /usr/local/var/postgres start (or stop)`

  **NOTE:** Postgres can also be started automatically:

  `brew services start postgresql`

+ Create role postgres (service needs to be running):

  `/usr/local/opt/postgres/bin/createuser -s postgres`

+ Login to psql as root user (postgres):

  `psql -U postgres`

  OR

  `psql -U postgres -h localhost`

+ Create new user:

  `CREATE USER reddit_admin WITH PASSWORD 'admin123';`

+ Create database:

  `CREATE DATABASE redditdb;`

+ Grant access on database to user:

  `GRANT ALL PRIVILEGES ON DATABASE redditdb TO reddit_admin;`

+ To be able to run test cases, the user must have permission to create a database

  `ALTER USER reddit_admin CREATEDB;`

+ Exit `psql`

  `\q`

+ Relogin as root user

  `psql -U postgres`

+ Verify new user (this will list all roles of existing postgres users)

  `\du`

+ Verify database (this will give details of all databases like owner, privileges, etc.)

  `\l`

+ Connect to database as authorized user

  `\c redditdb reddit_admin`

# Test

The below commands test interaction between SQLAlchemy and Postgres

User (Accounts)

```
# Database interface
from app import db

# Create table using SQLAlchemy
db.create_all()

# 'User' class will be used to create DB column values
from app.models import User

# User object data
user1 = User(name='Saurabh', email='saurab.mish@gmail.com')

# Add user object to session
db.session.add(user1)

# Persist data to database
db.session.commit()

# Get all data objects
User.query.all()

# Get first data object 
User.query.first()

# Get all users having name 'Saurabh' (better use case would be location since username is unique)
User.query.filter_by(name='Saurabh').all()

# get user with ID 1
User.query.get(1)
```