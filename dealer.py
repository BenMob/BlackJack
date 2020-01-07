'''
By Benjamin
'''

class Dealer:
    '''
    INPUT: None
    This is the dealer's class. 
    '''
    def __init__(self):
        self.cards = [] # Place holder for the dealer's cards
        self.hidden_card = 0 # Place holder for the hidden card

    # ----------------------------
    def hide_first_card(self):
        '''
        INPUT: None
        Hides the first card given to the card.
        '''        
        try:
            self.hidden_card = self.cards[0]
        except IndexError:
            print('The dealer doe not have any card currenty.')
        
        self.cards[0] = 'X'
        
    # --------------------------------
    def reveal_hidden_card(self):
        '''
        INPUT: None
        Reveals the dealer's hidden card if this one exists.
        '''
        # Checking if a card has been hidden previously
        if self.hide_first_card != 0:
            self.cards[0] = self.hidden_card
        else:
            print('The dealer has no hidden card currently.')

