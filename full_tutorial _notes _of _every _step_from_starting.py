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

📌 Understanding database.py in FastAPI
Purpose

database.py is responsible for connecting the FastAPI application with the database.

It creates everything required to communicate with the database:

Database Connection (Engine)
Database Session
Base Class for Models

Without this file, FastAPI cannot perform any database operations.

Overall Workflow
FastAPI Application
        │
        ▼
database.py
        │
        ├── Engine (Database Connection)
        ├── Session (Database Operations)
        └── Base (Parent Class for Models)
        │
        ▼
SQLite Database

Whenever FastAPI wants to Create, Read, Update, or Delete data, it first goes through database.py.

Complete Code
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
Line 1
from sqlalchemy import create_engine
Purpose

Imports the create_engine() function.

What is Engine?

Engine is the database connection object.

Think of it as a bridge between Python and the database.

Python
   │
   ▼
Engine
   │
   ▼
SQLite Database

Without an Engine, Python cannot communicate with the database.

Line 2
from sqlalchemy.orm import sessionmaker
Purpose

Imports sessionmaker, which is used to create database sessions.

What is a Session?

A Session represents one interaction with the database.

Example:

Open Session
      │
      ▼
Insert Data

Update Data

Delete Data

Read Data
      │
      ▼
Close Session

Every database operation is performed through a Session.

Line 3
from sqlalchemy.ext.declarative import declarative_base
Purpose

Imports declarative_base().

It creates a parent class that all database models inherit from.

Example:

Without Base

class User:

Python treats it as a normal class.

With Base

class User(Base):

Now SQLAlchemy understands that User represents a database table.

Database URL
URL_DATABASE = "sqlite:///./finance.db"
Purpose

Specifies which database SQLAlchemy should connect to.

sqlite:///
        │
        ▼
Use SQLite Database

finance.db
        │
        ▼
Database File Name

When the application runs, finance.db is created automatically if it doesn't already exist.

Creating the Engine
engine = create_engine(
    URL_DATABASE,
    connect_args={"check_same_thread": False}
)
Purpose

Creates the connection between FastAPI and SQLite.

Workflow

FastAPI
    │
    ▼
Engine
    │
    ▼
SQLite Database
Why check_same_thread=False?

SQLite allows only one thread by default.

FastAPI can handle multiple requests simultaneously.

User 1
User 2
User 3
      │
      ▼
FastAPI

check_same_thread=False allows SQLite to work correctly with FastAPI's request handling.

Note: This option is specific to SQLite and is generally not required when using databases like PostgreSQL or MySQL.

Creating the Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Purpose

Creates a Session Factory.

Whenever FastAPI needs to interact with the database, it creates a new Session using:

SessionLocal()

Workflow

Session Factory
      │
      ├── Session 1
      ├── Session 2
      └── Session 3
autocommit=False

Changes are not saved automatically.

Example

Insert Employee

↓

Update Salary

↓

Delete Record

↓

Commit

If everything succeeds, the changes are committed.

This helps maintain data consistency.

autoflush=False

Flush means sending pending changes to the database before committing.

With autoflush=False, SQLAlchemy waits until the application explicitly decides when to send those changes.

bind=engine
Session

↓

Engine

↓

SQLite Database

It tells every Session which database connection (Engine) to use.

Creating Base
Base = declarative_base()
Purpose

Creates the parent class for all database models.

Example

class User(Base):
class Employee(Base):
class Pipeline(Base):

Every model that inherits from Base becomes a database table.

Complete Execution Flow
FastAPI Starts
      │
      ▼
database.py Executes
      │
      ├── Create Engine
      ├── Create Session Factory
      └── Create Base Class
      │
      ▼
Models inherit Base
      │
      ▼
FastAPI creates Sessions
      │
      ▼
Database Operations
      │
      ▼
SQLite Database
Key Concepts to Remember
Object	Purpose
create_engine()	Creates the database connection
engine	Stores the database connection
sessionmaker()	Creates database sessions
SessionLocal()	Creates a new session whenever needed
declarative_base()	Creates the parent class for all models
Base	Parent class inherited by every database model
