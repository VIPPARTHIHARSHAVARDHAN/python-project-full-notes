CREATED FOLDER in main folder
FastAPi,React
in Fastapi created 3 files they are database.py,main.py,models.py
added code in database.py
              from sqlalchemy import create_engine
               from sqlalchemy.orm import sessionmaker
              from sqlalchemy.ext.declarative import declarative_base
              
              URL_DATABASE = "sqlite:///./finance.db"

              engine = create_engine(
                  URL_DATABASE,
                  connect_args={"check_same_thread": False}
              )

              SessionLocal = sessionmaker(
                  autocommit=False,
                  autoflush=False,
                  bind=engine
              )

              Base = declarative_base()

Let's understand it line by line.

What is database.py?

Think of it as the bridge between FastAPI and the database.

FastAPI

↓

database.py

↓

SQLite Database

Whenever FastAPI wants to store or retrieve data, it goes through this file.

Line 1
from sqlalchemy import create_engine
What is create_engine()?

Engine means connection to the database.

Example:

Suppose you want to talk to MySQL.

First you need a connection.

Similarly,

create_engine()

creates a connection object.

Think of it like:

Python
   │
create_engine()
   │
SQLite Database
Line 2
from sqlalchemy.orm import sessionmaker

What is a Session?

Imagine a bank.

Before you deposit or withdraw money,

you open a session.

Open Session

↓

Do Work

↓

Close Session

Database also works like that.

Session is used to

Insert data
Update data
Delete data
Read data

without directly talking to SQLite every time.

Line 3
from sqlalchemy.ext.declarative import declarative_base

This is one of the most important concepts.

Suppose you create

class User:

Python thinks it is a normal class.

But we want SQLAlchemy to understand

This class represents a database table.

That's why we use

Base = declarative_base()

Now every model becomes

class User(Base):

instead of

class User:

Now SQLAlchemy knows

"User" is a database table.

Line 5
URL_DATABASE = "sqlite:///./finance.db"

This tells SQLAlchemy

Which database should I connect to?

Here

sqlite:///

means

Use SQLite.

finance.db

means

Database file name.

After running,

this file gets created.

finance.db

Think of it like

MySQL

↓

database name

↓

employees

Here

SQLite

↓

finance.db
Line 7
engine = create_engine(
    URL_DATABASE,
    connect_args={"check_same_thread": False}
)

This actually creates the connection.

Imagine

Python

↓

Engine

↓

SQLite

Now Python can communicate with SQLite.

What is
check_same_thread=False

SQLite normally allows only one thread.

FastAPI handles multiple requests.

User1

↓

User2

↓

User3

To avoid errors,

SQLite needs

check_same_thread=False

For PostgreSQL later,

this line won't be needed.

Line 9
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

This creates a Session Factory.

Think like this.

Session Factory

↓

Session 1

↓

Session 2

↓

Session 3

Whenever FastAPI needs the database,

it asks

SessionLocal()

which creates a new session.

autocommit=False

Suppose

INSERT Employee

Immediately saving is risky.

Instead

Insert

↓

Update

↓

Delete

↓

Commit

If everything succeeds,

then save.

So

autocommit=False

means

Don't save automatically.

autoflush=False

Flush means

Send changes to the database.

Here

FastAPI decides

when to flush.

bind=engine

This simply means

Session

↓

uses

↓

Engine

↓

SQLite
Last Line
Base = declarative_base()

This creates the parent class.

Later you'll write

class Expense(Base):

or

class User(Base):

Now SQLAlchemy automatically creates tables from these classes.
 
