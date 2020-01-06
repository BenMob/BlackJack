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
    def payout(self, result):
        '''
        INPUT: Result string-> 'blackjack', 'win, push 
        '''

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

        # Checking if the player still wnat to bet
        if self.player.funds > 0:

            while True:
                choice = input('\t\t\t\tDo you want to bet again ? (Y or N): ')
                if choice.lower() in ('y','n'):
                    break
                else:
                    self.print_table()

            if choice.lower() == 'y':
                self.reset(self.player.funds)
                self.print_table()
                self.player_play()

            elif choice == 'n':
                print('\n\t\t\t\tGood Bye!\n')
        else:
            print('\n\t\t\t\tYou have no money left. Good Bye!\n')


    # ---------------------------------------------------------------------
    def print_table(self):
        '''
        INPUT: None
        TASK: Prints the game table
        '''
        self.clearTable()
        print('\n___________________________\n')
        print(f'   Your money: ${self.player.funds + self.current_deal}')
        print(f'   Your bet: ${self.current_deal}')
        print(f'   Possible win: ${self.current_deal * 2}')
        print(f'___________________________\nRound: {self.round}\n')

        print(f'\n\tYou: {self.player.cards} \t\t\t\t Dealer: {self.dealer.cards} -> ', end = '')
        
        # Include the dealer's first card only if it is not hidden
        if 'X' in self.dealer.cards:
            print(sum(list(self.dealer.cards[1:])))
        else:
            print(sum(self.dealer.cards))

        print(f'\t{sum(self.player.cards)}\n')
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
    def game_play(self):
        '''
        INPUT: None
        This method execute the game
        '''
        # Step 0: Preparing the game
        self.clearTable()
        print('\n\t\tWELCOME TO BLACKJACK\n')

        while True:
            try:
                self.player.funds = int(input('Load money: $'))
                break
            except:
                print('Invalid Input!')

        # Execute player's turn
        self.player_play()

    # -------------------------------------    
    def player_play(self):

        # Step 1: Asking the player how much money they are betting.
        self.current_deal = self.player.bet()

        # Step 2: Distributing cards
        player_total, _ = self.distribute_cards()
        
        # Checking for Black Jack Tie
        if player_total == 21:
            if self.dealer_turn(True) == 'push':
                self.print_table()
                self.payout('push')
                
            elif self.dealer_turn(True) == 'win':
                self.print_table()
                self.payout('blackjack')   

        # NO BLACK_JACK
        else:
            # Step 3: Hit or Stand
            player_turn = True
        
            while player_turn:
                self.print_table()

                if self.execute_play() == 1:
                    self.hit(self.player.cards)

                    if self.player_has_busted():
                        self.print_table()
                        print('\t\t\tBUST\n')
                        print(self.player_has_busted())
                        self.payout('bust')

                        player_turn = False
                   
                else:
                    result = self.dealer_turn()
                    self.print_table()
                    self.payout(result)

    # -----------------------------------------------------
    def reset(self, player_fund = 0):
        '''
        '''
        self.player = Player(player_fund)
        self.dealer = Dealer()
        self.deck = Cards()
        self.current_deal = 0
        self.round += 1
                    




                


        