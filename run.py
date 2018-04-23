from flask import Flask, render_template, redirect, request, url_for, flash
import os
import json
import random
from datetime import datetime
from operator import itemgetter
from natsort import natsorted

app = Flask(__name__)
app.secret_key = 'some_secret_key'

riddles_data = []
online_users = []
wrong_answers = []

# Load data from riddles.json
with open('data/riddles.json', 'r') as json_data:
    riddles_data = json.load(json_data)

def check_if_username_already_exists(selected_username):
    # Check if username already exists
    with open('data/users.txt', 'r') as users_file:
        users_list = [line.rstrip() for line in users_file]        
        return True if selected_username in users_list else False

def save_results(username, scores):
    # Save results to a file
    timestamp = datetime.now().strftime('%d-%m-%Y')
    user_result = "{0} {1} {2}\n".format(scores, username.title(), timestamp)
    with open('data/results.txt', 'a') as results_file:
        results_file.writelines(user_result)
        
def get_top_scores():
    # Get top results, sorted by top score
    top_scores = []
    with open('data/results.txt', 'r') as results_file:
        lines = [line.split(' ') for line in results_file]
    for line in natsorted(lines, key=itemgetter(0), reverse=True):
        top_scores.append(line)
    return top_scores
                
def add_to_wrong_answers(username, riddle_index, answer):
    # Store wrong answer with username and riddle number
    riddle_number = riddle_index + 1
    riddle_answer = (riddle_number, username.title(), answer)
    wrong_answers.append(riddle_answer)

def answer_to_lowercase(answer):
    return answer.lower()

def answer_is_a_word(answer):
    return True if answer.isalpha() else False

@app.route('/')
def index():
    top_scores = get_top_scores()
    return render_template('index.html', top_scores=top_scores)

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
            # Add user to online users
            online_users.append(selected_username)
            return redirect(selected_username)         
    return render_template('register.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login_user():  
    if request.method == 'POST':
        selected_username = request.form['username']
        if check_if_username_already_exists(selected_username):
            # Add user to online users
            online_users.append(selected_username)
            # Redirect to game if username OK
            return redirect(selected_username)
        else:
            # Display message for wrong username
            error_wrong_username = 'Wrong username, please try again'
            return render_template('login.html', message=error_wrong_username)
    return render_template('login.html')

@app.route('/<username>', methods=['GET', 'POST'])
def user_play_game(username):      
    riddle_index = 0
    riddle_number = 1
    all_scores = len(riddles_data)
    scores = 0
    
    if request.method == 'POST':
        answer = answer_to_lowercase(request.form['answer'])
        # Get current index from template
        riddle_index = int(request.form['riddle_index'])
        riddle_number = riddle_index + 1
        # Get current scores from template
        scores = int(request.form['scores'])
        # If correct answer and not the last riddle, go to next riddle
        if answer == answer_to_lowercase(riddles_data[riddle_index]['answer']):
            if riddle_index < len(riddles_data) - 1:
                riddle_index += 1
                riddle_number += 1
                scores += 1
            else:
                scores += 1
                # After last riddle go to page with results and save user result
                save_results(username, scores)
                return redirect(url_for('game_results', username=username, scores=scores))
        # Pass this riddle and go to next one
        elif 'btn_pass' in request.form:         
            if riddle_index < len(riddles_data) - 1:
                riddle_index += 1
                riddle_number += 1
            else:
                # If last riddle go to page with results and save user result
                save_results(username, scores)
                return redirect(url_for('game_results', username=username, scores=scores))
        else:
            # Add answer to wrong answers if answer is a word
            if answer_is_a_word(answer):
                add_to_wrong_answers(username, riddle_index, answer)  
            else:
                flash('This answer is not a word, try again')       
    return render_template('game.html', username=username, online_users=online_users, riddles=riddles_data, riddle_index=riddle_index, riddle_number=riddle_number, wrong_answers=wrong_answers, scores=scores, all_scores=all_scores)

@app.route('/results/<username>/<scores>')
def game_results(username, scores):
    top_scores = get_top_scores()    
    return render_template('end_game_results.html', username=username, scores=scores, top_scores=top_scores)

@app.route('/logout/<username>')
def logout_user(username):
    # Remove user from online users and redirect to home page
    online_users.remove(username)
    return redirect('/')
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)