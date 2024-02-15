from src.connect4.connect4_game import Game
from src.connect4.player import Player
from src.engine.engine_player import EnginePlayer

if __name__ == "__main__":
    Game(Player(1), EnginePlayer(2, depth=6)).run()
