# BlackJack
This is a simplified version on the Casino BlackJack game using OOP in Python.

# Description
BlackJack, also known as 21 is one of the most popular casino games out there. In BlackJack players compete against the house(casino) and not
against each other. In this case, the house dealer will be the computer and you will be the player. The player's goal is to have in hand a total value of cards closer to 21 than the dealer, but not over 21. (Busting)

Card values:
------------
Cards from 2 to 10 their face values.
Jacks Queens and Kings are valued at 10
Aces can be either 1 or 11 depending on the player's favor.

A starting value of a 10 valued card and an Ace is called a Blackjack in chich case neither the player or the dealer wins. The result here is
called a push(tie) No Money exchange.


# Order of play
1. Betting
----------
The player will first place a fake money bet from the fake money bank provided by the computer in this case.
Values: $1   $5   $10   $20   $50   $100   $500   $2500   $5000

2. Card distribution:
---------------------
The dealer will randomly distribute cards from a Deck of 52 cards(Jokers exluded)
        - The player gets two cards both faced up
        - The dealer gets two cards one faced up and one faced down

2. Actions
----------
Stand: If the player is happy with their total card value they can stand, meaning they get no more cards.
Hit: If the player is not happy with their total card, theu can hit and get one more card until they Stand or if they reach or pass 21.

In real BlackJack games, there are more actions such as Double Downs, Split and Surrender but in this game we will only Stand or Hit.

3. Payouts
----------
If the player and dealer have equal umbusted totals, then the game is ties and the player's bet is returned.
If the player wins a hand they are paid out 1:1 on their bet. Example: Bet = $20  --> Win = $20 --> Total Pay = $40
If the player has BlackJack they get paid out 3:2 on their bet. Example: Bet = $10 --> Win = $15 --> Total Pay = $25

Good Luck and have fun :)





