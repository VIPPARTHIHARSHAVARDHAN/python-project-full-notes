Interview Questions
1. What is the purpose of database.py?

It centralizes the database configuration by creating the database connection (Engine), Session Factory, and Base class required for SQLAlchemy ORM.

2. What is an Engine?

An Engine is the connection object that allows Python to communicate with the database.

3. Why do we use Session?

A Session is used to perform database operations such as Create, Read, Update, and Delete.

4. Why do models inherit from Base?

Models inherit from Base so SQLAlchemy recognizes them as database tables and maps the class structure to the database schema.

5. Why is autocommit=False used?

It ensures that changes are not saved automatically. The application explicitly commits changes only after all operations complete successfully.

This style is much more professional for GitHub because it explains purpose → workflow → code → interview questions, which is how developers usually document concepts.
