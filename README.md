# RIDDLE-ME-THIS GAME

A web application game that asks players to guess the answer to a text-based riddle.

This is a milestone project for Practical Python, part of the Full-Stack Web Developer program @ Code Institute.

## Introduction

A web application game that asks players to guess the answer to a text-based riddle.
Users have to login or register to play a game. There is a list of all online users.
If a player guesses correctly, they are redirected to the next riddle, else their incorrect guess is stored and printed below that riddle.
Multiple players can play an instance of the game at the same time.
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

5. Run tests
~~~~
python -m unittest
~~~~

## Testing

I used Python's unit testing framework - unittest.
I created a testcase, a class that inherits from unittest.TestCase. Each test is defined with method and name of this method starts with test_ as required by naming convention. 
I tested checking if username already exists and if top scores are sorted correctly. Code example:

```python
class TestRiddle(unittest.TestCase):
    def test_check_username_already_exists(self):
        check1 = run.check_if_username_already_exists('username')
        check2 = run.check_if_username_already_exists('hgfsjkdgf')
        self.assertEqual(check1, True)
        self.assertEqual(check2, False)
```

Most of the tests were done manually and with help of a print function for each new functionality. There were some bugs during developement, for example the list of top results was sorted only by the first number. I found natsort module to sort two digit numbers to get results displayed correctly. 

I didn't use any templates to style this app so I had to find a trick to test updated template style by adding dynamic variable to a static link.

~~~~
href="/static/css/style.css?q=1535"
~~~~
Testing for responsive layout was done in Chrome and also on different devices. Final check was done with [this application](http://browsershots.org/).

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