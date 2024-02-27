from src.connect_x.connect_x_game import Game
from src.connect_x.player import Player

if __name__ == "__main__":
    Game(Player(1), Player(2), display_messages=True).run()
