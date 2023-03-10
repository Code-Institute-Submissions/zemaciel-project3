# Airport Codes Game

![](assets/airport_codes_game.png)
<br>
Live site at [https://airport-codes-game.herokuapp.com/](https://airport-codes-game.herokuapp.com/)
<br>
<br>

# Table of Content
<!-- TOC start -->
- [Description ](#description)
- [Logic](#logic)
- [Features](#features)
  * [Introduction, menu and rules](#introduction-menu-and-rules)
  * [Hints and Airports](#hints-and-airports)
  * [Clues](#clues)
  * [End-of-game feedback](#end-of-game-feedback)
  * [Input validation](#input-validation)
- [Testing](#testing)
  * [PEP8 Validator Testing](#pep8-validator-testing)
  * [Manual Testing](#manual-testing)
  * [Unfixed bugs](#unfixed-bugs)
- [Technologies ](#technologies)
  * [Python Modules](#python-modules)
  * [Deployment ](#deployment)
- [Credits](#credits)
<!-- TOC end -->

# Description 
The "Airport Codes Game" is inspired by the well-known web-based game [Wordle](https://en.wikipedia.org/wiki/Wordle), where the players have six tries to guess a five-letter word, with feedback given for each guess in the form of coloured tiles indicating when letters match or occupy the correct position. 

If you still haven't played Wordle, you can play it for free at [The New York Times website](https://www.nytimes.com/games/wordle/index.html).

As a Wordle fan and an aviation geek, I decided to try programing the "Airport Codes Game" similar to Wordle, where the players have six attempts to guess the three-letter [IATA code](https://en.wikipedia.org/wiki/IATA_airport_code) for an airport.


# Logic
![](assets/flowchart.png)

# Features
## Introduction, menu and rules
![](assets/intro.png)
<br>
At the start of every new game, the player is greeted with an [ASCII art](https://en.wikipedia.org/wiki/ASCII) and, introduction text and a menu where they can choose to read the rules, play a new game, read the game credits or quit. 

The menu is also displayed at the end of the games. 

The introduction, ASCII art, rules and credits are stored in a separate python file.

## Hints and Airports
Some IATA codes are the initials of the name of the airport they represent (e.g. JFK for John Fitzgerald Kennedy, New York) or abbreviations of the city where they are located (e.g. DUB for Dublin Airport). However, in many cases, there is no clear association between the airport and its code (e.g. YYZ for Toronto Pearson International Airport). 

Also,  asking the players to guess any three-letter code could lead to frustration. They could spend all their six attempts before getting any clue.   

Instead, a hint about the airport's location is displayed at the start of every new game to make the game easier to play. Also, the list of airports is limited to the one-hundred busiest airports in Europe and North America. 

![](assets/hint.png)

The list of airports and hints are in two different dictionaries in a separate python file. 

## Clues
The game displays a line below the player's guess with [Emojis](https://en.wikipedia.org/wiki/Emoji) symbols to provide feedback if the letters in the player's input match the ones in the airport code: 

- ???? The green circle indicates that the letter is in the code and the correct position.
- ???? The yellow circle means the letter is in the code but not in the right place.
- ?????? The grey square indicates that the letter is not part of the code.

All the player's attempts remain visible on the screen until the game is reset. 

## End-of-game feedback
The game ends when the player uses all their six tries or when they correctly guess the three letters of the airport code in their correct positions. 
There are three different feedback given according to the outcome: 

1 - The players guess correctly on the first try:<br>

![](assets/end_game_1.png)

2 - The players guess correctly using more than one try:<br>

![](assets/end_game_2.png)

3 - The players use all their tries and don't guess correctly:<br>

![](assets/end_game_3.png)

In all cases, the feedback presents the correct IATA code with the airport name and location, followed by the game menu. 

## Input validation
Every time the user inputs a value, the game checks if it is a valid three-letter code, and converts the letters to uppercase to match the IATA code standards. 
 In case of an invalid input the player will get one of the following messages: <br>
 * The player's guess has lenth different than three letters:<br>
 ![](assets/invalid_lengh.png)

 * The player's guess contains numbers or symblos: <br>
 ![](assets/invalid_not_alpha.png) 



# Testing
## PEP8 Validator Testing
The game has been tested by running it through the [CI Python Linter](https://pep8ci.herokuapp.com/).

The final version of the run.py and the aiport_dictionary.py have no issues. 

The file containing the ASCII art presents errors due to trailing whitespaces or "invalid escape sequence '\_' ".


## Manual Testing
The game has been tested on Google Chrome and Firefox for desktop and mobile with no significant issues. 

## Unfixed bugs
There is a problem when the game loads for the first time: the introduction screen, with the ASCII, is not displayed entirely.  

Also, when a player enters a guess with repeated letters, if the letter is just in the airport code, the feedback will be green for the letter in the correct place and yellow for the repeated, letter because it is in the guess code. 

For example: If the IATA code is "DUB", and the user enters "UUU", the clue will be "Yellow-Green-Yellow". It could be better to indicate that if the letter had already been guessed, the repeated occurrences should be marked as not in the airport code.<br>
![](assets/bug.png)

I could not fix these issues, but they only affected a little game experience. 


# Technologies 
* [Python programming language](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [CI Python Linter](https://pep8ci.herokuapp.com/)

## Python Modules

* random - Allow a random word to be chosen.
* os - Allow clear function to clear terminal.

## Deployment 
This site was deployed with the Code Institute template for Heroku. 
The steps to deploy are:
* At Heroku dashboard,  click "new" and "create new app". 
* Than, set the build packs to Python and jsnode in this order. 
* In the deploy tab connect the github repository and click on enable automatic deploy.

The deployed app can be found here: [https://airport-codes-game.herokuapp.com/](https://airport-codes-game.herokuapp.com/)

# Credits
I started this project following a tutorial on the YouTube channel ["CompSci with Dr. Victor"](https://www.youtube.com/@CompSciwithDrVictor), under the title ["Text-Based Wordle in Python under 15 Minutes!"](https://www.youtube.com/watch?v=J6h7D2iQmBU). The code from the video is available [here](https://replit.com/@DrVictor/TextBasedWordle).
* The list of airports for this game is from the web page ["Top 100 busiest airports in the world"](https://gettocenter.com/airports/top-100-airports-in-world). <br>For this game there are only airports from North America and Europe.
* The function to clear the screen was extracted from the project of a Code Institute collegue, [James Fitzpatrick's Hangman](https://github.com/James-Fitz/hangman_python)
* Code Institute [Python Template](https://github.com/Code-Institute-Org/python-essentials-template)
* ASCII art created with [Patorjk.com](https://patorjk.com/software/taag)
* Adobe Illustrator for the flow chart.

I would like to thank my mentor Martina Terlevic for her help in this project and the Code Institute Student Care team. 