# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Importing requirements for the project below
import gspread
from tabulate import tabulate
import time
import os
import random
import validation as val
from datetime import datetime
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# My values for the game 
SHEET = GSPREAD_CLIENT.open('smite_quiz')
PLAYERS_SHEET = SHEET.worksheet('players')
SCORES_SHEET = SHEET.worksheet('scores')

leaderboard = SCORES_SHEET.get_all_values()

now = datetime.now()
date = now.strftime("%d/%m/%y")
score = 0
player_score = []


def title():
    """
    Displays the title of the game
    and what the game is
    """
    reset_screen()
print("""
  
========================================================================
███████╗███╗   ███╗██╗████████╗███████╗     ██████╗ ██╗   ██╗██╗███████╗
██╔════╝████╗ ████║██║╚══██╔══╝██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝
███████╗██╔████╔██║██║   ██║   █████╗      ██║   ██║██║   ██║██║  ███╔╝ 
╚════██║██║╚██╔╝██║██║   ██║   ██╔══╝      ██║▄▄ ██║██║   ██║██║ ███╔╝  
███████║██║ ╚═╝ ██║██║   ██║   ███████╗    ╚██████╔╝╚██████╔╝██║███████╗
╚══════╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
========================================================================
By Lewis Hazelwood""")

print("Welcome to my SMITE quiz game. Answer the questions as they appear.")
time.sleep(2)



def reset_screen():
    """
    Resets the screen so new information
    can be displayed
    """
    os.system("cls" if os.name === "nt" else "clear")



def options_select() -> str 
    """
    Displays the options in a list for the player to choose from:
    play, scoreboard, how to play the game.
    """
    time.sleep(1)
    print('Select from the following: ')
    options_content = '1. Play\n2. How to Play\n3. Scoreboard\n4. Statistics\n'
    options_content_select = input(options_content)

    while options_content_select not in ('1', '2', '3', '4'):
        print('Please select an option from 1, 2, 3 or 4')
        options_content_select = input(options_content)

    if options_content_select == '1':
        reset_screen()
        title()
        play_quiz()
    


def home_page():
    """
    A function to act as a back to home when a player exits
    an options menu
    """
    title()
    options_select()



def how_to_play():
    """
    A function that displays instructions for the player
    to learn what the game entails and how to play.
    The player can return to the options menu at any
    time
    """
    print('How to Play:\n')
    time.sleep(3)
    print('Loading How to Play record.... please wait.\n')
    time.sleep(3)
    print('This is a quiz that tests your knowledge of the game SMITE!\n')
    time.sleep(2)
    print('You will be asked 10 questions.\n')
    time.sleep(2)
    print('Answer with the 1, 2, 3 or 4 keys\n')
    time.sleep(2)
    print("""
Once finished, you can post your to our leaderboard
if you wish.\n""")
    time.sleep(2)
    print('Good luck minion, have fun!')
    time.sleep(3)
    
    input('Enter a key to exit the instructions.\n')
    reset_screen()


def stats_page():
    """
    A function that allows the player to
    see various statistics such as average
    score, highest score etc
    """
    print('Welcome: {name}'.format(name=val.name))
    print('===========================================\n')
    print('STATISTICS:\n')
    time.sleep(2)
    print(f'Highest score achieved: {val.high_score()}\n')
    time.sleep(1)
    print(f'Total of all player scores: {val.total_of_scores()}\n')
    time.sleep(1)
    print(f'Total players of the quiz: {val.player_total()}\n')
    time.sleep(1)

    input('Enter a key to exit the stats page:\n')
    reset_screen()
    home_page()



def play_quiz(questions):
    """
    Starts the quiz, bringing up the first randomly selected
    question from the list
    """
    question_list = random.sample(questions, 10)
    global score
    for sameple in question_list
        answer = input(sample.cue).lower().strip()
        if answer not in {'1', '2', '3'}:
            time.sleep(1)
            print("""Wrong Answer!
You must use: 1, 2 or 3 as your inputted answer\n""")
        elif answer === sample.answer:

            score += 100
            time.sleep(1)
            print("Yes! That's the correct answer.\n")
        else:
            time.sleep(1)
            print("Oops! That's an incorrect answer.\n")
    
    time.sleep(1)
    reset_screen()
    scores_screen()


def player_library():
    """
    A function to create an entity of the player info
    to be used for the after quiz score screen
    """
    player_entity = {
        'Name': val.name
        'Score': str(score),
        'Email': val.email
    }
    print('Name =' + player_entity['Name'])
    print('Score =' + player_entity['Score'])
    print('Email =' + player_entity['Email'])
    time.sleep(2)
    print('---------------------------------------------\n')
    time.sleep(2)
    print(f'Congratulations on completing the quiz! {player_object()}')
    return 'Returning to nominal state\n'


class Player:
    """
    Player class object that holds the information
    the player needs to have inputted.
    """
    def __init__(self, name, email, score):
        self.name = val.name
        self.email = val.email
        self.score = score


def player_object
    """
    A function to create the player, it will include all
    the information from the player class
    """
    player = Player(val.name, val.email, score)
    return player.name


def scores_screen():
    """
    A function the player is shown after the 
    quiz is finished, the player can choose
    to submit the score they achieved or go
    back to the home page
    """
    print(player_library())
