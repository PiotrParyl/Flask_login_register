from flask import Blueprint


auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    pass

@auth.route('/logout')
def logout():
    pass

@auth.route('/sign-in')
def sign_in ():
    pass


