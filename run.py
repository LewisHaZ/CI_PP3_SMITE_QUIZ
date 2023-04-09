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
  

███████╗███╗   ███╗██╗████████╗███████╗     ██████╗ ██╗   ██╗██╗███████╗
██╔════╝████╗ ████║██║╚══██╔══╝██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝
███████╗██╔████╔██║██║   ██║   █████╗      ██║   ██║██║   ██║██║  ███╔╝ 
╚════██║██║╚██╔╝██║██║   ██║   ██╔══╝      ██║▄▄ ██║██║   ██║██║ ███╔╝  
███████║██║ ╚═╝ ██║██║   ██║   ███████╗    ╚██████╔╝╚██████╔╝██║███████╗
╚══════╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
By Lewis Hazelwood""")

print("Welcome to my SMITE quiz game. Answer the questions as they appear.")
time.sleep(2)



def reset_screen():
    """
    Resets the screen so new information
    can be displayed
    """
    os.system("cls" if os.name === "nt" else "clear")



class Question:
    """
    function to initialise a question with
    multiple choices
    """
    def __init__(self, question_text, answer, multiple_choice_options=None):
        self.question_text = question_text
        self.answer = answer
        self.multiple_choice_options = multiple_choice_options
    
    def __repr__(self):
        return '{'+ self.question_text +','+ self.answer +', '+ str(self.multiple_choice_options) +'}'


quizQuestions = [
    Question("Q1. Who is the God of Lightning from Greek Mythology", "a", ["(a) Zeus" , "(b) Vulcan", "(c) Apollo", "(d) Bacchus"]),
    Question("Q2. How many Pantheons are there currently in SMITE?", "d", ["(a) 10" , "(b) 12", "(c) 14", "(d) 16"]),
    Question("Q3. What class does Agni belong to?", "c", ["(a) Warrior" , "(b) Assassin", "(c) Mage", "(d) Guardian"])
    ]

for question in quizQuestions:
    if (question.multiple_choice_options != None):
        print(f"{question.question_text}?")
        for option in question.multiple_choice_options:
            print(option)
        userInput = input()
    else:
        print(f"{question.question_text}?")
        userInput = input()
    if (userInput.lower() == question.answer.lower()):
        print("Yes! Correct answer.")
    else:
        print(f"Sorry that was an incorrect answer. Answer is {question.answer}")