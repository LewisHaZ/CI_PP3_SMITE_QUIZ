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


def check_first_visit() -> str:
    """
    Checks to see if the player has played
    the game before
    """
    time.sleep(1)
    print('Greetings! Are you new here?\n')
    response = '1. Yep \n2. Nope\n'
    responded = input(response).lower()

    while responded not in ('1', 'y', '2', 'n'):
        print('Please choose an appropriate response: ')
        responded = input(response).lower()
        time.sleep(1)
    
    if responded in ('1', 'y'):
        print('You answered yes\n')
        time.sleep(2)
        email_prompt()
        time.sleep(1)
        print(f'Your email is {email}\n')
        time.sleep(1)
        login_prompt()
        register_new()
        return True

    elif responded in ('2', 'n'):
        print('You answered no\n')
        time.sleep(2)
        email_prompt()
        validate_email_address(email)
        get_player_name()
        return False

def email_prompt():
    """
    Asks player for their email input
    """
    global email
    email = input('Please enter your email address.\n')
    time.sleep(1)
    validate_email_address(email)
    return email, True


def validate_email_address(email: str):
    """
    Validates the player's email address.
    """
    try:
        validate_email(email)
        return True
    
    except EmailNotValidError as e:
        print("\n" + str(e))
        print("Email format incorrect, try again.\n")
        email_prompt()
        return False


def register_new():

        
        