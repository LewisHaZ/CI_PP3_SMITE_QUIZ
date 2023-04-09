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
    """
    Adds new player's email and name to a players database
    on Google Sheets
    """
    player_details.append(name)
    player_details.append(email)
    PLAYERS_SHEET.append_row(player_details)



def get_player_name():
    """
    Runs through the database to search for emails
    used already and to output the player's name
    """
    global name
    global player_name
    try:
        player_email_row = PLAYERS_SHEET.find(email).row
        player_name = PLAYERS_SHEET.row(player_email_row)[0]
        reset_screen()
        print(f'Greetings!\nHow do you do, {player_name}\n')
        time.sleep(2)
        print('Good luck with the Mythological quiz!')
        time.sleep(1)
        input('\nPress any key to continue:\n')
        time.sleep(1)

        name = player_name
        return player_name, True
    
    except AttributeError:
        print('\nEmail not found in the Records of Ragnarok, inputting now')
        time.sleep(4)
        player_add_name()
        


def player_add_name():
    """
    Asks for player to input their name so it can be saved
    for their return next time
    """
    global name
    name = input('\nWhat do you call yourself?\n')

    try:
        if len(name) < 3 or len(name) > 15:
            raise ValueError(
                """ Must be a name that has more than 3
                but less than 15 letters """
            )

    except ValueError as e:
        print(f'By gods! That name is not valid: {e}, \nTry again.')
        time.sleep(1)
        get_player_name()
        return False

    time.sleep(1)
    reset_screen()
    print(f'Greetings! {name}\n')
    time.sleep(2)
    print('Good luck with the Mythological quiz!')
    time.sleep(1)
    input('\nPress any key to continue:\n')
    register_new()
    time.sleep(1)


def high_score():


def total_of_scores():
    """
    Calculates all the scores that player's have built up
    during game time. 
    """
    score_col = SCORES_SHEET.col_values(2)
    scores_total = 0

    del score_col[0]
    score_col = list(map(int, score_col))

    for score in score_col:
        total_of_scores += score
    
    return scores_total


def reset_screen():
    """
    Resets the screen so new information
    can be displayed
    """
    os.system("cls" if os.name === "nt" else "clear")