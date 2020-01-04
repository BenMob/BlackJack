# By Benjamin ombeni

class Player:
    '''
    INPUT: funds(int)
    This is the player's class
    '''
    # --------------------------------------
    def __init__(self, username = '', funds = 0):
        self.username = username 
        self.funds = funds
        self.cards = [] # Place holder for the player's cards
        self.total_card_value = 0

    # --------------------------------
    def bet(self):
        '''
        INPUT: None
        Extracts the amount from the total funds and returns it.
        '''
        while True:
            try:
                amount = int(input('How much are you betting: $'))

                # Checking the amount
                if amount > self.funds:
                    print("Stay within your financial lane!")
                else:
                    self.funds -= amount
                    return amount
            except:
                print('Invalid Input!')

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

