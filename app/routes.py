"""
Routes module containing routes (different URLs that the application implements) and handlers (aka view functions)
"""

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Het Dok'}
    posts = [
        {
            'author': {'username': 'Claire'},
            'body': 'Beautiful day in Scotland'
        },
        {
            'author': {'username': 'Jenny'},
            'body': 'I made dumplings!!'
        },
        {
            'author': {'username': 'Gaby'},
            'body': 'Nap time :D'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)