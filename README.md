# BlackJack
This is a simplified version on the Casino BlackJack game using OOP in Python.

# Description

        BlackJack, also known as 21 is one of the most popular casino games out there. 
        In BlackJack players compete against the house(casino) and not against each other. 
        In this case, the house dealer will be the computer and you will be the player. 
        The player's goal is to have in hand a total value of cards closer to 21 than the dealer, but not over 21. (Busting)

Card Values
-----------
        . Cards from 2 to 10 keep their face values.
        . Jacks Queens and Kings are valued at 10.
        . Aces can be either 1 or 11 depending on the player's favor.

        A player starting value of a 10 valued card and an Ace is called a Blackjack in which case the player automaticaly
        wins.


# Order of play
1. BETTING  
----------
        . The player will first place a fake money bet from the fake money bank provided by the computer in this case. 
        . Values: $1   $5   $10   $20   $50   $100   $500   $2500   $5000

2. CARD DISTRIBUTION
---------------------
        The dealer will randomly distribute cards from a deck of 52 cards(Jokers exluded).
        
        . The player gets two cards both faced up
        . The dealer gets two cards one faced up and one faced down

3. ACTIONS
----------
<<<<<<< HEAD
. Stand: If the player is happy with their total card value they can stand, meaning they get no more cards.
. Hit: If the player is not happy with their total card value, they can hit and get one more card until they Stand or if they reach or pass 21.

. In real BlackJack games, there are more actions such as Double Downs, Split and Surrender but in this game we will only Stand or Hit.
=======
        . Stand: If the player is happy with their total card value they can stand, meaning they get no more cards.
        . Hit: If the player is not happy with their total card, they can hit and get one more card until they Stand, or if  they reach or pass 21.
>>>>>>> 615c86b32f1ee0e7351eb53aa809451647393217

        In real BlackJack games, there are more actions such as Double Downs, Split and Surrender but in this game we will
        only Stand or Hit.
        
3. Payouts
----------
<<<<<<< HEAD
. If the player and dealer have equal unbusted totals, then the game is tied and the player's bet is returned.
. If the player wins a hand they are paid out 1:1 on their bet. Example: Bet = $20  --> Win = $20 --> Total Pay = $40.
. If the player has BlackJack they get paid out 3:2 on their bet. Example: Bet = $10 --> Win = $15 --> Total Pay = $25.
=======
        . If the player and dealer have equal umbusted totals, then the game is ties and the player's bet is returned.
        . If the player wins a hand they are paid out 1:1 on their bet. Example: Bet = $20  --> Win = $20 --> Total Pay =
        $40.
        . If the player has BlackJack they get paid out 3:2 on their bet. Example: Bet = $10 --> Win = $15 --> Total Pay =
        $25.
>>>>>>> 615c86b32f1ee0e7351eb53aa809451647393217

Good Luck and have fun :)


# Documentation

Dealer class:
--------------
        Attributes
        ----------
        . cards (List)
        . hidden_card (int)
        
        Methods:
        --------
        . hide_first_card() : Hides the one of the dealer's cards.
        . reveal_hidden_card() : Reveals the dealer's hidden card.

Player class:
-------------
        Attributes
        ----------
        . username: string
        . funds: int
        . cards: List
        
        Methods
        -------
        . bet(): Asks the player how much they want to bet.
        . add_funds(int amount): Adds amount to the player's funds.

Cards class:
------------
        Attributes
        ----------
        . Deck: List of tuples holding card names and values.
        
        Methods
        -------
        . shuffle(): Shuffles cards.
        . draw_a_card(): Draws a card from the deck and returns a tuple (card, value).
        . determine_Ace_value(card list): Determins whether the value of ace should be 1 or 11 based on the card list passed in.
        
Game class:
-----------
        Attributes
        ----------
        player: Object of type Player.
        dealer: Object of type Dealer.
        deck: Object of type Cards.
        
        Methods
        -------

