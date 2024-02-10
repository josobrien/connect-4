from src.connect4.Connect4Game import Game
from src.connect4.Player import Player
from src.engine.EnginePlayer import EnginePlayer

if __name__ == "__main__":
    Game(Player(1), EnginePlayer(2, depth=6)).run()
