# By Benjamin

import random

class Cards:
    '''
    INPUT: None
    This class simply build a standard deck of 52 Cards excluding jokers
    '''

    # ----------------------------------
    def __init__(self):
        self.Deck = [('A',(1,11)), ('A',(1,11)), ('A',(1,11)), ('A',(1,11)),
                     ('2',2), ('2',2), ('2',2), ('2',2),
                     ('3',3), ('3',3), ('3',3), ('3',3),
                     ('4',4), ('4',4), ('4',4), ('4',4),
                     ('5',5), ('5',5), ('5',5), ('5',5),
                     ('6',6), ('6',6), ('6',6), ('6',6),
                     ('7',7), ('7',7), ('7',7), ('7',7),
                     ('8',8), ('8',8), ('8',8), ('8',8),
                     ('9',9), ('9',9), ('9',9), ('9',9),
                     ('10',10), ('10',10), ('10',10), ('10',10),
                     ('J',10), ('J',10), ('J',10), ('J',10),
                     ('Q',10), ('Q',10), ('Q',10), ('Q',10),
                     ('K',10), ('K',10), ('K',10), ('K',10)]

    # -----------------------------------
    def shuffle(self):
        '''
        INPUT: None
        This method simply shuffles the deck of cards.
        '''
        return random.shuffle(self.Deck)

    # -----------------------------------
    def __str__(self):
        '''
        RETURN: The number of cards in the deck
        '''
        return(f"{len(self.Deck)}")

    # -----------------------------------
    def draw_a_card(self, card_List = []):
        '''
        INPUT: None
        OUTPUT: A valid card value in BlackJack as a tuple
        '''
        card, value = self.Deck.pop(random.randint(0, len(self.Deck) - 1))
        if card == 'A':
            value = self.determine_Ace_value(card_List)
        
        return (card, value)

    # --------------------------------
    def determine_Ace_value(self, card_list):
        '''
        INPUT: list of card values
        Return: value of Ace (1 or 11)
        '''
        try:
            print(f'Current List: {card_list}')    
            if sum(card_list) + 11 <= 21:
                return 11
            else:
                return 1
        except:
            print(f'Error in determine_Ace_value()     Current List: {card_list}')

