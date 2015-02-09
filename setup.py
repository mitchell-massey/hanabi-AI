# Game Setup

number_of_players = 3                   ## we may want to have the game ask for number of players at beginning
total_cards = 50

if number_of_players > 3:
	hand_count = 4


numbers = [1,1,1,2,2,3,3,4,4,5] 
colors = ["blue", "green", "pink", "white", "yellow"]     
deck = [[[j,i] for j in numbers] for i in colors]


from random import shuffle

shuffle(deck)

print(deck)

def deal():





	

