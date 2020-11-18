# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
#from app import db

# Define a base model for other database tables to inherit
#class Base(db.Model):


# Define a User model
class User():

    __tablename__ = 'auth_user'

    # User Name
    name    = "jej"

    # Identification Data: email & password
    email    = "keke"
    password = "keke"

    # Authorisation Data: role & status
    role     = "mee"
    status   = "lele"

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
