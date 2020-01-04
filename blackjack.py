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

            # Updating player's total value
            self.player.total_card_value = sum(self.player.cards)

            # Hiding one of the deal's cards
            self.dealer.hide_first_card()

        return (self.player.total_card_value, sum(self.dealer.cards[1:]))

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
        print(f'   Current fund: ${self.player.funds}')
        print(f'   Current deal: ${self.current_deal}')
        print(f'   Possible win: ${self.current_deal * 2}')
        print('_____________________________\n')

        print(f'\n\tYou: {self.player.cards} \t\t\t\t Dealer: {self.dealer.cards} -> {sum(list(self.dealer.cards[1:]))}')
        print(f'\t{sum(self.player.cards)}\n')
        print('\n\t1. Hit\n\t2. Stand\n')

    # ----------------------------------------------------     
    def execute_play(self):
        '''
        INPUT: None
        Return 1 for hit and 2 for stand
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
    def check_blackjack(self, card_list = []):
        '''
        '''
        if sum(card_list) == 21:
            return 'blackjack'
        elif sum(card_list) < 21:
            return 'ok'
        else:
            return 'bust'

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

        # Execute player's turn
        self.player_play()

    # -------------------------------------    
    def player_play(self):
        # Step 1: Asking the player how much money they are betting.
        self.current_deal = self.player.bet()

        # Step 2: Distributing cards
        player_total, _= self.distribute_cards()
        
        if player_total == 21:
            self.print_table()
            print('\f BLACKJACK. WOHAA!!!')
            ## self.payout('blackjack')
            ## self.show_current funds and ask if they want to play again
        else:
            # Step 3: Hit or Stand
            player_turn = True
        
            while player_turn:
                self.print_table()

                if self.execute_play() == 1:
                    self.hit(self.player.cards)

                    deal = self.check_blackjack(self.player.cards)
                    
                    if deal == 'blackjack':
                        self.print_table()
                        print("Dealer's turn (Possible tie)")
                        ## self.dealer_turn()
                        ## Id dealer's turn is also black jack deal = tie
                        break
                    elif deal == 'bust':
                        self.print_table()
                        print('\t\t\tBUST\n')
                        break
                        ## self.payout('bust')
                        ## self.show_current funds and ask if they want to play again
                else:
                    print("Dealer's turn, (no possible tie)")
                    break
                    ## self.dealer_turn
                    ## self.dealer's turn (No possible tie)




                


        