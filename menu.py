## @package menu
#  Source file for the menu object
#
#  Project: Minesweeper
#  Author: Ayah Alkhatib
#  Created: 09/08/18
#  Completed:

from executive import Executive

class Menu :

    def __init__(self):
        self.choice = 2
        self.mines_num = 0
        self.board_size = 0
        #self.game_over = game_over
        self.is_loser = False
        self.myGame = Executive ()
    

    def game_menu(self):
        while (self.myGame.game_over == False):
            
            print("Please, chose from the menu:")
            print("""1. Play the Game
2. Quit""")
            self.choice = int(input())
            if self.choice == 1:
                self.myGame.setup()
                self.myGame.play()
            else:
                print("Goodbye! See you later!")
                return
            play_again = input ("Play again (p), otherwise (q): ")
            if play_again == "p":
                self.myGame = Executive ()
                self.myGame.setup()
                self.myGame.play()
            else:
                print ("Goodbye! See you later!")
                return

    def game_rules (self):
        print ("""Welcome to Minesweepers!

Here are the game instructions:
The game will provid players a square board with a number of hidden mines and similar number of flags.
Player has three choices of action:
    - Flag: to flag squares that might have mines.
    - Unflag: to unflag if player changed mind.
    - Reveal: to see what squares have underneath.
When player chose to reveal:
    - If the square has a mine -> Gameover!
    - If not a mine, it will show spaces and numbers to tell player the number of mines around the chosen square.

The goal is to flag all mines until the counter of flags equals to zero without revealing any mine.

Good Luck!
""")

    def play_again(self):
        if self.is_winner:
            print("YOU WON!!")
            self.game_menu()
            self.is_winner = False
        elif self.is_loser:
            print("GAME OVER!")
            self.game_menu()
            self.is_loser = False

    def play_game(self):
        while not self.is_winner or not self.is_loser:
            # some interactive between the game and the user
            print("still playing")
        self.play_again()
