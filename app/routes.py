from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrea'}
    posts = [
        {
            'author': {'username': 'user1'},
            'body': 'lovely day'
        },
        {
            'author': {'username': 'user2'},
            'body': 'indeed'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)