# By Benjamin
import os
from dealer import Dealer
from player import Player
from cards import Cards

class Game:
    '''
    INPUT: An object of the class player
    '''
    # ---------------------------------
    def __init__(self):    
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Cards()
        self.current_deal = 0

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
            _, value = self.deck.draw_a_card(self.player.cards)
            self.player.cards.append(value)
            
            # Drawing dealer's card
            _, value = self.deck.draw_a_card(self.dealer.cards)
            self.dealer.cards.append(value)

            # Hiding one of the deal's cards
            self.dealer.hide_first_card()

        return (sum(self.player.cards), sum(self.dealer.cards[1:]))

    # --------------------------------
    def hit(self, card_list = []):
        '''
        INPUT: List of current cards
        OUTPUT:  
        '''
        _, value = self.deck.draw_a_card(card_list)
        card_list.append(value)

    # -------------------------------- 
    def stand(self):
        print('Done')

    # --------------------------------
    def payout(self):
        pass
    
    def print_table(self):
        '''
        INPUT: None
        TASK: Prints the game table
        '''
        self.clearTable()
        print('\n_____________________________\n')
        print(f'Current fund: ${self.player.funds}')
        print(f'Current deal: ${self.current_deal}')
        print(f'Possible win: ${self.current_deal * 2}')
        print('_____________________________\n')

        print(f'\n\tYou: {self.player.cards} \t\t\t\t Dealer: {self.dealer.cards} -> {sum(list(self.dealer.cards[1:]))}')
        print(f'\t{sum(self.player.cards)}\n')
        print('\n\t1. Hit\n\t2. Stand\n')

    # ----------------------------------------------------     
    def execute_play(self):
        '''
        INPUT: None
        Executes the player's move (Hit or Stand)
        '''
        while True:
            try:
                choice = int(input('\fChoice: ' ))
                if choice == 1 or choice == 2:
                    break
                else:
                    self.print_table()
            except:
                self.print_table()

        # Executing play
        if choice == 1:
            self.hit(self.player.cards)
        else:
            return 'stand'
        
    # ----------------------------------
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

    # ---------------------------------
    def game_play(self):
        '''
        INPUT: None
        This method execute the game
        '''
        # Step 0: Preparing the game
        print('\n\t\tWELCOME TO BLACKJACK\n')
        self.player.username = input('Enter your name: ')
        while True:
            try:
                self.player.funds = int(input('Load money: $'))
                break
            except:
                print('Invalid Input!')

        # Step 1: Asking the player how much money they are betting.
        self.current_deal = self.player.bet()

        # Step 2: Distributing cards
        player_total, dealer_total = self.distribute_cards()

        # Step 3: Game starts
        game_on = True

        while game_on:
            self.print_table()
            move = self.execute_play()
            if move ==  'stand':
                game_on = False


        