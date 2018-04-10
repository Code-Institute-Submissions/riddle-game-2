from flask import Flask, render_template, redirect, request
import os
# import json
# from datetime import datetime

app = Flask(__name__)
app.secret_key = 'some_secret_key'


def check_if_username_already_exists(selected_username):
    # Check if username already exists
    # NEED FIX: PARTIAL WORDS
    with open('data/users.txt', 'r') as users_file:
        if selected_username in users_file.read():
            return True
        else:
            return False

@app.route('/')
def index():        
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        selected_username = request.form['username']
        if check_if_username_already_exists(selected_username):
            # Display message if username already exists
            error_user_exists = 'Username already exists'
            return render_template('register.html', message=error_user_exists)
        else:
            # Add username to users.txt and redirect to game
            with open('data/users.txt', 'a') as users:
                users.write(selected_username + '\n')
            return redirect(selected_username)         
    return render_template('register.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login_user():  
    if request.method == 'POST':
        selected_username = request.form['username']
        if check_if_username_already_exists(selected_username):
            # Redirect to game if username OK
            return redirect(selected_username)
        else:
            # Display message for wrong username
            error_wrong_username = 'Wrong username, please try again'
            return render_template('login.html', message=error_wrong_username)
        
    return render_template('login.html')

@app.route('/<username>')
def user_play_game(username):
    return render_template('game.html', username=username)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)