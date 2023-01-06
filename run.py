
airport_list = ['DUB', 'SNN', 'NOC', 'KIR']

import random

airport = random.choice(airport_list)
print(f'The AirportCode Selected is {airport}')

position = 0
end_of_game = False

#display = ['⬜️', '⬜️', '⬜️',]
display = []
guess = input("Type a 3-letter code and press enter:\n").upper()
for letter in guess:
    if letter == airport[position]:
        display += '🟢'
    elif letter in airport:
        display += '🟡'
    else:
        display += '⬜️'
    position += 1
guess = guess.split()
print(f"You guessed:\n {guess}")
print(display)



# while not end_of_game:


# for position in range(0,2):
#     letter = airport[position]
#     # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter

# print(display)























