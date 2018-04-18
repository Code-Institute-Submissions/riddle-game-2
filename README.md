# RIDDLE-ME-THIS GAME

A web application game that asks players to guess the answer to a text-based riddle.

This is a milestone project for Practical Python, part of the Full-Stack Web Developer program @ Code Institute.

## Introduction

A web application game that asks players to guess the answer to a text-based riddle.
If a player guesses correctly, they are redirected to the next riddle, else their incorrect guess is stored and printed below that riddle.
Multiple players can play an instance of the game at the same time. Users are identified by a unique username.
There is also a leaderboard that ranks top scores for top 5 and top 10 results.

This Project is deployed on [Heroku](https://riddle-game.herokuapp.com/)

Source code is availible on [GitHub](https://github.com/tjasajan/riddle-game)

## Build with

+ [Python 3](https://www.python.org/)
+ [Flask Framework](http://flask.pocoo.org/)

## Other technologies used

+ Visual Studio Code editor
+ Virtual environment
+ Pylint
+ pip
+ unittest
+ HTML5, CSS3
+ Chrome DevTools

## Installation

1. Download files
2. Install [Python](https://www.python.org/downloads/)
3. Install Flask and other requirements 
~~~~
pip install -r requirements.txt
~~~~
4. Run application
~~~~
python run.py
~~~~
In VS Code I get TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'.
In run.py there are two lines for PORT:
~~~~
port=os.environ.get('PORT')
port=int(os.environ.get('PORT'))
~~~~
Comment out the second one and remove comment for the first one. For code deployment, do the opposite.

5. Run tests
~~~~
python -m unittest
~~~~

## Testing

I used Python's unit testing framework - unittest.
I created a testcase, a class that inherits from unittest.TestCase. Each test is defined with method and name of this method starts with test_ as required by naming convention. The aim is to clean and refactor the code in run.py and to check for possible errors. 



## Deployment

Output installed packages for dependency management:
~~~~
pip freeze --local > requirements.txt
~~~~
Create Procfile needed for Heroku deployment:
~~~~
echo web: python run.py > Procfile
~~~~
Add to Heroku app repository:
~~~~
heroku git:remote -a riddle-game
~~~~
Configure app:
~~~~
heroku ps:scale web=1
~~~~
On Heroku site add settings for IP (0.0.0.0) and PORT (5000) and restart all dynos.