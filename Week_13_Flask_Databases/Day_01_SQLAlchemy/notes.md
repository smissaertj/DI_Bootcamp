https://www.sqlalchemy.org/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/


```shell
$ pip install -U Flask-SQLAlchemy
```

# Database Object
```shell
import flask
import flask_sqlalchemy
import flask_migrate
import os 

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
```

# Database Model
```shell
db      = flask_sqlalchemy.SQLAlchemy(app)

class MyModel(db.Model):

    field1 = db.Column(db.String(64))
    field2 = db.Column(db.Integer)
```

## Field Arguments
```shell
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(64), index=True)
time = db.Column(db.DateTime, default=datetime.now)
```

# Managing the database
* `$ flask db init`, the first command that you need to run, it creates the database, you need to run it when it’s the first time you use this database.
* `$ flask db migrate`, every time you make changes in the database structure, you need to migrate it, flask creates a file of changes in the database, the database will later use it to update its structure.
* `$ flask db upgrade`, this time, flask update your changes and change the actual database structure

# Adding Objects
```shell
model1 = MyModel(field1="HelloWorld", field2=1000)
db.session.add(model1)
db.session.commit()
db.session.rollback()
db.delete(obj)
```

# Retrieving Objects
```shell
MyModel.query.all() 
MyModel.query.get(1)
User.query.filter_by(username="Eyal")
User.query.order_by(User.username.desc())
MyModel.query.with_entities(MyModel.column).distinct()
```

# Complete Code

### models.py
```shell
from app import db

class Book(db.Model):

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Book: {self.title}>'
```

### routes.py
```shell
from app import app
from app.models import Book

@app.route('/')
def index():
    books = ', '.join([book.title for book in Book.query.all()])
    return books
```

### __init__.py
```shell
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

# Database Connection
db_info = {'host': 'localhost',
           'database': 'bookstore',
           'psw': '1234',
           'user': 'postgres',
           'port': ''}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import models, routes
```

# Using PostgreSQL with Flask

```shell
> psql
CREATE DATABASE database_name

> pip install psycopg2
...
> export DATABASE_URL="postgresql://url/to/database"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
```

```shell
> psql
\c database_name
\dt 
\d table_name
```

### PostgreSQL JSON
```shell
from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'results'

    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    meta = db.Column(JSON)
```

