# By Benjamin

import os
import time
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
        self.round = 1

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

        # Storing total values
        player_total = sum(self.player.cards)
        dealer_total = sum(self.dealer.cards)

        # Hiding one of the deal's cards
        self.dealer.hide_first_card()

        return (player_total, dealer_total)

    # --------------------------------
    def hit(self, card_list = []):
        '''
        INPUT: List of current cards
        OUTPUT:  
        '''
        _, value = self.deck.draw_a_card(card_list)
        card_list.append(value)

    # --------------------------------
    def evaluate_results(self, result):
        '''
        INPUT: Result string-> 'blackjack', 'win', 'push' or 'bust 
        '''
        self.print_table()

        if result == 'blackjack':
            print('\t\t\tBLACKJACK WIN!\n')
            amount = self.current_deal + (self.current_deal//2)
            self.player.add_funds(amount)
            print(f'\t\t\t\tYou won ${amount}, you now have ${self.player.funds}\n')

        elif result == 'win':
            print('\t\t\tWIN\n')
            self.player.add_funds(self.current_deal * 2)
            print(f'\t\t\t\tYou won ${self.current_deal}, you now have ${self.player.funds}\n')

        elif result == 'push':
            print('\t\t\tPUSH\n')
            self.player.add_funds(self.current_deal)
            print(f'\n\t\t\t\tYou get back your ${self.current_deal}, you still have ${self.player.funds}\n')

        elif result == 'bust':
            print('\t\t\tBUST\n')
            print(f'\n\t\t\t\tYou have ${self.player.funds} left\n')

        # reset the game 
        self.reset(self.player.funds)

        # Checking if the player still wnat to bet
        if self.player.funds > 0:

            while True:
                choice = input('\t\t\t\tDo you want to bet again ? (Y or N): ')
                if choice.lower() in ('y','n'):
                    break
                else:
                    self.print_table()

            if choice.lower() == 'y':
                self.print_table(False)
                self.game_play()

            elif choice.lower() == 'n':
                print('\n\t\t\t\tGood Bye!\n')
        else:
            print('\t\t\t\tGood Bye!\n')


    # ---------------------------------------------------------------------
    def print_table(self, hit_or_stand = True):
        '''
        INPUT: None
        TASK: Prints the game table
        '''
        self.clearTable()
        print('\n___________________________\n')
        print(f'   Pocket: ${self.player.funds}')
        print(f'   Bet: ${self.current_deal}')
        print(f'   Deal: +${self.current_deal * 2}')
        print(f'___________________________\n{self.round}\n')

        print(f'\n\tYou: {self.player.cards} \t\t\t\t Dealer: {self.dealer.cards} -> ', end = '')
        
        # Include the dealer's first card only if it is not hidden
        if 'X' in self.dealer.cards:
            print(sum(list(self.dealer.cards[1:])))
        else:
            print(sum(self.dealer.cards))
        print(f'\t{sum(self.player.cards)}\n')

        if hit_or_stand:
            print('\n\t1. Hit\n\t2. Stand\n')


    # ----------------------------------------------------     
    def execute_play(self):
        '''
        INPUT: None
        Return 1 for hit and 2 for stand
        '''
        # Collecting player's choice
        while True:
            try:
                choice = int(input('\fChoice: ' ))
                if choice == 1 or choice == 2:
                    break
                else:
                    self.print_table()
            except:
                self.print_table()

        return choice
        
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

    # ----------------------------------
    def dealer_turn(self, first_try = False):
        '''
        INPUT: None
        This method will execute the dealer's play
        '''
        # Revealing the dealer's hidden card
        self.dealer.reveal_hidden_card()
        
        while sum(self.dealer.cards) <= sum(self.player.cards):

            self.print_table()
            if first_try:
                print('\t\t\tBLACKJACK!')   
            print('\t\t\tWait for the dealer ...')
            time.sleep(3)

            # Dealer's total == Player's total
            if sum(self.dealer.cards) == sum(self.player.cards):
                return 'push' # Tie game
           
            # Dealer's total is less than player's
            else:
                self.hit(self.dealer.cards)

        # Dealer has won
        if sum(self.dealer.cards) <= 21:
            return 'bust'
        
        # Dealer has busted
        else:
            return 'win' 
            
    # ----------------------------------
    def player_has_busted(self):
        '''
        INPUT: None
        '''
        return sum(self.player.cards) > 21
        

    # ---------------------------------
    def start_game(self):
        '''
        INPUT: None
        This method sets the the game, then calls the gameplay method
        '''
        # Step 0: Preparing the game
        self.clearTable()
        print('\n\t\tWELCOME TO BLACKJACK\n')

        while True:
            try:
                self.player.funds = int(input('Load money: $'))
                if self.player.funds <= 0:
                    print('You must have at least $1')
                else:
                    break
            except:
                print('Invalid Input!')

        # Let the game start
        self.game_play()

    # -------------------------------------    
    def game_play(self):
        '''
        This methos executes the game
        '''
        # Step 1: Asking the player how much money they are betting.
        self.current_deal = self.player.bet()

        # Step 2: Distributing cards
        player_total, _ = self.distribute_cards()
        
        # Checking for Black Jack Tie
        if player_total == 21:
            if self.dealer_turn(True) == 'push': 
                self.evaluate_results('push')
                
            elif self.dealer_turn(True) == 'win':
                self.evaluate_results('blackjack')   

        # NO BLACK_JACK
        else:
            # Step 3: Hit or Stand
            while True:
                self.print_table()

                if self.execute_play() == 1:
                    self.hit(self.player.cards)

                    if self.player_has_busted():
                        self.evaluate_results('bust')
                        break
                   
                else:
                    result = self.dealer_turn()
                    self.evaluate_results(result)
                    break

    # -----------------------------------------------------
    def reset(self, player_fund = 0):
        '''
        INPUT: player's fund
        This method resets the game
        '''
        self.player = Player(player_fund)
        self.dealer = Dealer()
        self.deck = Cards()
        self.current_deal = 0
        self.round += 1
                    




                


        