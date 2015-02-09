# Game Setup

number_of_players = 3                   ## we may want to have the game ask for number of players at beginning
number_of_cards = 5

if number_of_players>3:
    number_of_cards = 4

unknown_card = [[True]*5,[True]*5]                      ## A card is represented by a list containing two lists of five boolean
                                                        ## values each where true means that the card is possibly that value:
                                                        ## [[1,2,3,4,5],[Blue,Green,Red,White,Yellow]]

hand_of_cards = [unknown_card]*number_of_cards          ## creates the Simon's hand which is a list of cards
                                                                                               


table = [0,0,0,0,0]                                     ## shows value of top card for each firework: [Blue,Green,Red,White,Yellow] 
known_card_properties = [[0,0],[0,0],[0,0],[0,0],[0,0]] ## represents known number and then color of any cards


def known_cards_check:                                  ##checks if any cards are known
    for x in hand_of_cards:
        for y in x:
            if y.count(True) == 1:
                known_card_properties[x] = y.index(True)

            
def check_for_play():                                   ##checks to see if a card in hand is playable
    

    

def play_card():
    


def discard_card(cards_temp):
    discarded = cards_temp.pop(0)               ## takes card at index 0 out of hand_of_cards and names it discarded
    cards_temp.append(unknown_card)             ## Adds new card to index 4 in the unknown state(all values are true)
    return cards_temp, discarded
