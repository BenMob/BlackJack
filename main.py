# By Benjamin Ombeni
# 12/31/2019

# This is a simplified version on the Casino BlackJack game using OOP in Python.
import blackjack

game = blackjack.Game()
game.game_play()

'''
def game_play():
    on = True
    player = Player('Benjamin',250)
    game = Game(player)
    print(num for num in range(0,54))

    
    game.distribute_cards()
    game.print_table()
    

    while on:
        game.execute_play()
        game.print_table()
        if sum(game.player.cards) > 21:
            print('BUST')
            on = False
        elif sum(game.player.cards) == 21:
            print('BLACKJACK !!!!')
            on = False
        else:
            pass

game_play()
''' 


