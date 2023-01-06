# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

airport_list = ["DUB", "SNN", "NOC", "KIR", "ORC", "BFS"]

import random

chosen_airport = random.choice(airport_list)
print(f"The AirportCode Selected is {chosen_airport}")

guess = input("Type a 3-letter code and press enter:\n").upper()

for letter in chosen_airport:
    if letter == guess:
        print("🟢")
    else:
        print("🔴")

