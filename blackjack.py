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
        self.Deck = [{'A_heart':[1,11]},{'A_diamond':[1,11]},{'A_spade':[1,11]},{'A_club':[1,11]},
                     2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
                     {'Q_heart':10},{'Q_diamond':10},{'Q_spade':10},{'Q_club':10},
                     {'K_heart':10},{'K_diamond':10},{'K_spade'},{'K_club':10}]

        '''
        self.Deck = [{'A_heart':[1,11]},{'A_diamond':[1,11]},{'A_spade':[1,11]},{'A_club':[1,11]},
                     2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
                     {'Q_heart':10},{'Q_diamond':10},{'Q_spade':10},{'Q_club':10},
                     {'K_heart':10},{'K_diamond':10},{'K_spade'},{'K_club':10}]
        '''
    def shuffle(self):
        '''
        INPUT: None
        This method simply shuffles the deck of cards.
        '''
        return random.shuffle(self.Deck)

    def __str__(self):
        return(f"{self.Deck}")

    def draw_a_card(self):
        '''
        INPUT: None
        OUTPUT: A valid card value in BlackJack
        '''
        num = random.randint(0, len(self.Deck))
        print(f'\nThe random index picked is {num} and the car there is {self.Deck[num]}\n')

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
'''
cards = Cards()
cards.draw_a_card()



