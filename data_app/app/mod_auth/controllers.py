# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
#from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
#from app import db

# Import module forms
#from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.forms import Login as login

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():

    #h = Login.watson_normal();
    #login = Login()
    h ="f"
    result = login.watson_normal()

    print(result)
    return render_template("auth/signin.html")
