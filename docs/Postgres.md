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

+ Verify new user (this will list all roles of existing postgres users)

  `\du`

+ Verify database (this will give details of all databases like owner, privileges, etc.)

  `\l`

+ Exit `psql`

  `\q`


# Test

**The below commands test interaction between SQLAlchemy and Postgres.**

```
# Database interface
from app import db

# Create table using SQLAlchemy
db.create_all()

# 'User' class will be used to create DB column values
from app.models.user import User
from app.models.post import Post

# User object data
user1 = User(name='Saurabh', email='saurab.mish@gmail.com')

# Add user object to session
db.session.add(user1)

# Persist data to database
db.session.commit()

# Rollback in case of any error
db.session.rollback()

# Get all data objects
User.query.all()

# Get first data object
User.query.first()

# Get all users having name 'Saurabh' (better use case would be location since username is unique)
User.query.filter_by(name='Saurabh').all()

# Get user with ID 1
User.query.get(1)

# Show posts created by user (model name is from foreign key relationship)
user = User.query.get(1)
user.posts

# check user's ID
user.id

# Create posts (user_id is from the model and user.id is from the table)
post1 = Post(title='Blog 1', text='Post content 1', community='tech', user_id=user.id)
post2 = Post(title='Blog 2', text='Post content 2', community='tech', user_id=user.id)

# Add (post) objects to session
db.session.add(post1)
db.session.add(post2)

# Persist data
db.session.commit()

# Check posts by user (equivalent to Post.query.all() as per __repr__)
user.posts

# Check user ID of the first post
post = Post.query.first()
post.user_id

# Return user object of post (uses 'backref' in user model)
post.author

# Cleanup (the below command freezes on postgres, so close / commit / remove waiting transactions first)
db.session.close()
OR
db.session.commit()
OR
db.session.remove()

db.drop_all()
```


# Play

**In a new terminal to verify interaction between SQLAlchemy and Postgres.**

+ Re-login as root user

  `psql -U postgres`

+ Connect to database as authorized user

  `\c redditdb reddit_admin`

+ View all tables

  `\dt`

+ View table details

  `\d table_name`

+ View data in *user* table

  `select * from "user";`

