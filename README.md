![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Noughts and Crosses is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Noughts and Crosses (or tic-tac-toe in American English) is traditionally a paper-and-pencil game for 2 players who take turns marking the spaces in a 3x3 grid with an O or X (Noughts or Crosses).

The player who succeeds in placing 3 of their marks in a row (horizontally, vertically or diagonally) is the winner. It is a solved game, with a forced draw assuming best play from both players. You can read more about it on Wikipedia (https://en.wikipedia.org/wiki/Tic-tac-toe)

# Table of Content

+ UX
    + Site Purpose
    + User Demographic
    + User Goals
        + First time player
        + Frequent player
+ Design
+ Features
    + Existing Features
        + Premier League Logo and Heading
        + Quiz Area
        + Score Area
        + Prize Area
        + Features Left to Implement
+ Technologies Used
+ Testing
    + Validator Testing
    + Unfixed Bugs
+ Deployment
+ Credits
    + Content
    + Media

# UX

## Site Purpose

To allow players to participate in a quick, enjoyable game against an AI opponent.

## User Demographics

Anyone that is interested in playing the game.

## User Goals

### First time player

- As a first time player, I want to learn more about the game.
- As a first time player, I want to improve my knowledge of basic strategy.
- As a first time player, I want to be guided on how to play the game.
- As a first time player, I want to input my name and receive customised messages.
- As a first time player, I want to exit the game upon completion.
- As a first time player, I want the opportunity to play again without restarting the App.

### Frequent player

- As a frequent player, I want to keep playing to increase my knowledge.
- As a frequent player, I want to be tested by the AI to improve my ability.
- As a frequent player, I want to see how I am getting on vs the AI.
- As a frequent player, I want to test my ability against another Human player.

# Features

## Existing Features

### Landing screen:

### Game start:

### First move:

### Completed game:

### New game:

### Name validation:

### Move validation:

### Game validation:

## Features left to implement:

- Randomise starting order - Switching between the player and the computer would improve the user experience/difficulty.

- Increase AI intelligence - Code the AI to have some knowledge of basic strategy.

- Difficulty levels - Linked to AI knowing basic strategy, it would be fantastic to offer different difficulty levels to the player. This would increase their experience whilst allowing them to improve their ability.

- Record the score - Letting the player keep track of the score would help with immersion.

- Ability to play with 2 user players - Allowing multiple players to participate would add depth to the game and increase user adoption.

# Testing

## Terminal compatibility:

I tested the App in the IDE and on the deployed App’s terminal.
Confirmed that the App worked as expected.

## Application features:

I tested all features, including entering the inputs.
Confirmed that the App worked as expected without any errors.

## Validation:

I tested the incorrect input and associated error messages.
Confirmed that the appropriate error messages displayed when invalid data was entered.

## Conclusion:

The testing confirmed that the Noughts and Crosses game functions as expected, providing a simple, enjoyable experience to the player.



This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
