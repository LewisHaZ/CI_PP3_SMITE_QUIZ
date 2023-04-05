# Imports for the project requirements
import time
import gspread
import os
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError

# Scope and variables as shown in love_sandwiches project from CI
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

player_details = []
name = ''
email = ''

def check_first() -> str:
    """
    Checks to see if the player has played
    the game before
    """
    time.sleep(1)
    print('Greetings! Are you new here?\n')
    response = '1. Yep \n2. Nope\n'
    responded = input(response).lower()

    while responded not in ('1','y', '2', 'n'):
        print('Please choose an appropriate response: ')
        responded = input(response).lower()
        time.sleep(1)