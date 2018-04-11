from flask import Flask, render_template, redirect, request, url_for
import os
import json
import random
# from datetime import datetime

app = Flask(__name__)
app.secret_key = 'some_secret_key'

online_users = []
wrong_answers = []

# random_index_list = []
# def get_random_index_list():
#     # Get list with random numbers for riddle index
#     numbers_in_range = list(range(0, 20))
#     random_number_list = random.sample(numbers_in_range, 20)
#     for number in random_number_list:
#         random_index_list.append(number)


def check_if_username_already_exists(selected_username):
    # Check if username already exists
    with open('data/users.txt', 'r') as users_file:
        users_list = [line.rstrip() for line in users_file]
        if selected_username in users_list:
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
    riddles_data = []
    # Load data from riddles.json
    with open('data/riddles.json', 'r') as json_data:
        riddles_data = json.load(json_data)
    
    riddle_index = 0
    all_scores = len(riddles_data)
    scores = 0
    
    if request.method == 'POST':
        answer = request.form['answer'].lower()
        # Get current index from template
        riddle_index = int(request.form['riddle_index'])
        # Get current scores from template
        scores = int(request.form['scores'])
        # If correct answer and not the last riddle, go to next riddle
        if answer == riddles_data[riddle_index]['answer'].lower():
            if riddle_index < len(riddles_data) - 1:
                riddle_index += 1
                scores += 1
            else:
                # After last riddle go to page with results
                return redirect(url_for('game_results', username=username, scores=scores))
        # Pass this riddle and go to next one
        elif 'btn_pass' in request.form:
            
            if riddle_index < len(riddles_data) - 1:
                riddle_index += 1
            else:
                # If last riddle go to page with results
                return redirect(url_for('game_results', username=username, scores=scores))
        else:
            # Add answer to wrong answers
            wrong_answers.append(answer)
         
    return render_template('game.html', username=username, online_users=online_users, riddles=riddles_data, riddle_index=riddle_index, wrong_answers=wrong_answers, scores=scores, all_scores=all_scores)

@app.route('/results/<username>/<scores>')
def game_results(username, scores):
    
    return render_template('end_game_results.html', username=username, scores=scores)

@app.route('/logout/<username>')
def logout_user(username):
    # Remove user from online users and redirect to home page
    online_users.remove(username)
    return redirect('/')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)