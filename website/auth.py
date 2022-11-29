from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"