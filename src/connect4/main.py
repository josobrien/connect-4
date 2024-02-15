from src.connect4.connect4_game import Game
from src.connect4.player import Player

if __name__ == "__main__":
    Game(Player(1), Player(2), display_messages=True).run()
