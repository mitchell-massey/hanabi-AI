# Game Setup

number_of_players = 3                   ## we may want to have the game ask for number of players at beginning
number_of_cards = 5

if number_of_players>3:
    number_of_cards = 4

unknown_card = [[True]*5,[True]*5]                      ## A card is represented by a list containing two lists of five boolean values each where true means that the card is possibly that value: [[1,2,3,4,5],[Blue,Green,Red,White,Yellow]]
hand_of_cards = [unknown_card]*number_of_cards       ## creates a hand which is a list of cards
                                                                                               

def discard_card(cards_temp):
    discarded = cards_temp.pop(0)               ## takes card at index 0 out of hand_of_cards and names it discarded
                             ## Adds new card to index 4 in the unknown state(all values are true)
    return cards_temp, discarded
