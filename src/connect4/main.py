from src.connect4.Connect4Game import Game
from src.connect4.Player import Player

if __name__ == "__main__":
    Game(Player(1), Player(2), display_messages=True).run()
