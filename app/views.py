__author__ = 'Syn'
from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Tim'}
    posts = [{'author': {'nickname': 'John'}, 'body': 'Stuff!'}, {'author': {'nickname': 'Susan'},
                                                                  'body': 'Stuff is awesome'}]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

