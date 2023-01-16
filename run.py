import random
import os
from arts_and_rules import logo, intro, rules, game_over
from airport_dictionary import iata, hints

"""
Global Variables
"""
guess = ""
user_guess = ""
num_of_guesses = 0
guessed_correctly = False
clue = ""
hint = ""
final_anwser = ""
chosen_airport = ""


def check_guess(airport_code, players_guess):
    """
    Check if letters in input and IATA code mattch and update clue. 
    """
    global clue
    letter_correct = '🟢'
    letter_in_code = '🟡'
    letter_blank = '⬜️'
    position = 0
    clue = ""
    for letter in players_guess:
        if letter == airport_code[position]:
            clue += letter_correct
        elif letter in airport_code:
            clue += letter_in_code
        else:
            clue += letter_blank
        position += 1
    return airport_code == players_guess
    return clue


def select_random_airport():
    '''
    Get aiport details
    '''
    global hint
    global final_anwser
    global chosen_airport
    code_list = list(iata.keys())
    chosen_airport = random.choice(code_list)
    final_anwser = iata[chosen_airport]
    hint = hints[chosen_airport]
    return hint
    return chosen_airport
    return final_anwser


def get_user_input():
    """
    Ask the user for input and verify if it is valid.
    When valid, return guess and increase guess count.
    """
    global user_guess
    global guess
    global num_of_guesses
    user_guess = input("Type a 3-letter code and press enter:\n").upper()
    if len(user_guess) != 3:
        print(f"⚠️ {user_guess} is not a 3-letter code")
        get_user_input()
    if not user_guess.isalpha():
        print(f"⚠️ {user_guess} type only letters")
        get_user_input()
    else:
        guess = user_guess
        num_of_guesses += 1
    return num_of_guesses
    return guess


def play_game():
    global clue
    get_user_input()
    check_guess(chosen_airport, guess)
    print(f'''You guessed 
{guess}''')
    print(clue)
    print(f"This is your guess number {num_of_guesses}")
    check_end_game()


def check_end_game():
    guessed_correctly = check_guess(chosen_airport, guess)
    while num_of_guesses < 3 and not guessed_correctly:
        play_game()
    if num_of_guesses == 3:
        print(f'''Sorry, you may have missed your flight!
The IATA code is {chosen_airport}, for the
{final_anwser}''')
        print(game_over)
        menu()
    if guessed_correctly and num_of_guesses < 2:
        print(f'''
Congratulations!
You are a true airport geek and got the
correct code on your first try!
{chosen_airport} is the IATA code for the
{final_anwser}''')
        menu()
    if guessed_correctly and num_of_guesses >= 2:
        print(f'''
Well done!
You guessed the correct airport code in
{num_of_guesses} tries!
{chosen_airport} is the IATA code for the
{final_anwser}''')
        menu()


def start_game():
    global num_of_guesses
    select_random_airport()
    num_of_guesses = 0
    print(f'''
✈️ Ready to take off? ✈️
Can you guess the code of this airport
located in {hint} \n ''')
    play_game()

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


def menu():
    menu_choice = 0
    print('''
    Game Menu:
    ( N ) - New Game
    ( R ) - Rules
    ( Q ) - Quit
    ''')
    menu_choice = input("Type on number from the menu:\n").upper()
    if len(menu_choice) != 1:
        print("Invalid option")
        menu()
    if not menu_choice.isalpha():
        print("Invalid option")
        menu()
    if menu_choice == "N":
        start_game()
        screen_clear()
    if menu_choice == "R":
        print(rules)
        menu()
    if menu_choice == "Q":
        print("bye-bye")
        quit()


def intial_screen():
    print(logo)
    print(intro)
    menu()


intial_screen()
