import random

from airport_dictionary import iata, hints

code_list = list(iata.keys())
chosen_airport = random.choice(code_list)
final_anwser = iata[chosen_airport]
hint = hints[chosen_airport]
guess = ''

#print(chosen_airport)

letter_correct = '🟢'
letter_in_code = '🟡'
letter_blank = '⬜️'

def check_guess(airport_code, players_guess):
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
    print(clue)

    return airport_code == players_guess

num_of_guesses = 1
guessed_correctly = False
print(f"Can you guess the code of this airport \n located in {hint} \n ")

while num_of_guesses < 6 and not guessed_correctly:
    user_guess = input("Type a 3-letter code and press enter:\n").upper()
    if len(user_guess) != 3:
        print(f"{user_guess} is not a 3-letter code")
    elif not user_guess.isalpha():
        print(f"{user_guess} type only letters")
    else:
        guess = user_guess
        print(f"You have guessed:\n{guess}.")
        num_of_guesses += 1
    guessed_correctly = check_guess(chosen_airport, guess)

tries = num_of_guesses - 1

if guessed_correctly:
    if tries < 2:
        print(
            f"Congratulations! You are a true airport geek and got the correct code on your first try! \n {chosen_airport} is the IATA code for the {final_anwser}"
        )
    if tries >= 2:
        print(
            f"Congratulations! You guessed the correct airport code in {num_of_guesses -1} tries! \n {chosen_airport} is the IATA code for the {final_anwser}"
        )
else:
    print(
        f"Sorry, you may have missed your flight! \n The IATA code is {chosen_airport}, for the {final_anwser}"
    )