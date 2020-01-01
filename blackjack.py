# By Benjamin Ombeni
# 12/31/2019

# This is a simplified version on the Casino BlackJack game using OOP in Python.

import random

class Player:
    '''
    INPUT: funds(int)
    '''
    def __init__(self, funds = 0):
        self.funds = funds

    def bet(self, amount):
        '''
        INPUT: amount(int)
        Extracts the amount from the total funds and returns it.
        '''
        if amount > self.funds:
            print("Not enough funds")
            return 0
        else:
            self.funds -= amount
            return amount

    def add_funds(self, amount):
            try:
                self.funds += amount
                return True
            except:
                print('Invalid Input!')
                return False

    def __str__(self):
        return (f'Funds: ${self.funds}')

class Cards:
    '''
    INPUT: None
    This class simply build a standard deck of 52 Cards excluding jokers
    '''
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

    def shuffle(self):
        '''
        INPUT: None
        This method simply shuffles the deck of cards.
        '''
        return random.shuffle(self.Deck)

    def __str__(self):
        '''
        RETURN: The number of cards in the deck
        '''
        return(f"{len(self.Deck)}")

    def draw_a_card(self):
        '''
        INPUT: None
        OUTPUT: A valid card value in BlackJack
        '''
        return self.Deck.pop(random.randint(0, len(self.Deck)))

class Game:

    def __init__(self):
        pass

    def hit(self):
        pass

    def stand(self):
        pass

    def payout(self):
        pass

    def clearTable(self):
        pass


# Test Cases
'''
player = Player(250)

print(f'\nRight after creating the player --> {player}')
bet = player.bet(100)
print(f'Right after betting ${bet} --> {player}\n')

print(player.add_funds('2'))
print(f'Right after adding $500 --> {player}\n')

cards = Cards()
cards.shuffle()
print(cards)

cards = Cards()
card, value = cards.draw_a_card()
print(f'After drawing a {card}, there are now {cards} cards left')
card, value = cards.draw_a_card()
print(f'After drawing a {card}, there are now {cards} cards left')
'''

# A few things to think about next:
'''
1. Verify what happenes if by any chance all the cards end up being drawn (Write a resetDeck() or something).
2. Think about when the cards should be shuffled (look up rules for that or come up with something fair).
3. Move on to emplementing the game methods.
'''
