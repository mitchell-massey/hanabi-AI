# Game Setup

number_of_players = 3                   ## we may want to have the game ask for number of players at beginning
number_of_cards = 5

if number_of_players>3:
number_of_cards = 4

cards = [[0,0]]*number_of_cards        ## creates list, each item represents a card with another list [0,0]
                                       ##where the first number is the number of the card and the second is the color'''
