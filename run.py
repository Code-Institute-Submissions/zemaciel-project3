import random

from airport_dictionary import iata, hints
code_list = list(iata.keys())
chosen_airport = random.choice(code_list)
final_anwser = iata[chosen_airport]
hint = hints[chosen_airport]
guess = ''

print(chosen_airport)

letter_correct = 'G'
letter_in_code = 'Y'
letter_blank = '_'

def processGuess(theAnswer, theGuess):
    position = 0
    clue = ""
    for letter in theGuess:
        if letter == theAnswer[position]:
            clue += letter_correct
        elif letter in theAnswer:
            clue += letter_in_code
        else:
            clue += letter_blank
    position += 1
    print(clue)

    return theAnswer == theGuess

num_of_guesses = 1
guessed_correctly = False
print(f"Can you guess which is the code of this airport \n located in {hint} \n ")

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
    guessed_correctly = processGuess(chosen_airport, guess)

if guessed_correctly:
    print(f"Congratulations! You guessed the correct airport code in {num_of_guesses -1}, times! \n {chosen_airport} is the IATA code for the {final_anwser}")
else:
    print(f"Sorry, you may have missed your flight! \n The code is, {chosen_airport}, for the {final_anwser}")