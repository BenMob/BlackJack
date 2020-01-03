# By Benjamin Ombeni
# 12/31/2019

# This is a simplified version on the Casino BlackJack game using OOP in Python.

import random
import os

class Dealer:
    '''
    INPUT: None
    This is the dealer's class. 
    '''
    def __init__(self):
        self.cards = [] # Place holder for the dealer's cards

# ======================================================================
class Player:
    '''
    INPUT: funds(int)
    '''
    
    # --------------------------------------
    def __init__(self, username = '', funds = 0):
        self.username = username 
        self.funds = funds
        self.cards = [] # Place holder for the player's cards

    # --------------------------------
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

    # ---------------------------------
    def add_funds(self, amount):
        '''
        INPUT: amount (int)
        Adds amount to the player's funds.
        '''
        try:
            self.funds += amount
            return True 
        except:
             print('Invalid Input!')
             return False

    # ---------------------------------
    def __str__(self):
        '''
        Prints the player's user name and their current total funds
        '''
        return (f'{self.username}: ${self.funds}')

# ======================================================================
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
        return self.Deck.pop(random.randint(0, len(self.Deck) - 1))

# ==================================================
class Game:
    '''
    INPUT: An object of the class player
    '''
    # ---------------------------------
    def __init__(self, player):    
        self.player = player
        self.dealer = Dealer()
        self.deck = Cards()

    # ---------------------------------
    def distribute_cards(self):
        '''
        INPUT: None
        This method handles card distrubution in the game
        '''
        # Shuffle cards
        self.deck.shuffle()

        while len(self.player.cards) != 2 and len(self.dealer.cards) != 2:

            # Drawing player's card
            card, value = self.deck.draw_a_card()
            if card == 'A':
                value = self.determine_Ace_value(self.player.cards)
            self.player.cards.append(value)

            # Drawing dealer's card
            card, value = self.deck.draw_a_card()
            if card == 'A':
                value = self.determine_Ace_value(self.dealer.cards)
            self.dealer.cards.append(value)
        

        return (sum(self.player.cards), sum(self.dealer.cards))
    # --------------------------------
    def hit(self):
        pass

    # -------------------------------- 
    def stand(self):
        pass

    # --------------------------------
    def payout(self):
        pass
    
    def print_table(self):
        '''
        INPUT: None
        '''
        self.clearTable()
        print(f'\n\t\t\t\t\t\t\t\t\t\t\tYou: {self.player.cards}{sum(self.player.cards)} \t\t\t Dealer: {self.dealer.cards}{sum(self.dealer.cards)}')
        print(self.deck)

        # INCOMPLETE    

    # --------------------------------
    def determine_Ace_value(self, card_list):
        '''
        INPUT list of card values
        '''
        if sum(card_list) + 11 <= 21:
            return 11
        else:
            return 1

    # --------------------------------
    def clearTable(self):
        '''
        INPUT: None
        This method clears the OS screen
        '''
        # Windows OS name
        windows = 'nt'

        # For Windows
        if os.name == windows: 
            _ = os.system('cls')
        # For every other OS
        else: 
            _ = os.system('clear')

    # ----------------------------------
    def game_play(self):
        pass
    
# ============================================

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

player = Player('Benjamin',250)
game = Game(player)
p,d = game.distribute_cards()
game.print_table()
print(p)
print(d)