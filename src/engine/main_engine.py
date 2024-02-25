import numpy as np

from src.connect4.connect4_game import Game
from src.connect4.player import Player
from src.engine.engine_player import EnginePlayer

if __name__ == "__main__":
    Game(EnginePlayer(1, depth=6), EnginePlayer(2, depth=6, use_new=True)).run()

    # can start games from specific states:
    # game_state = np.array([[0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0, 0, 0],
    #                        [0, 0, 2, 0, 0, 0, 0],
    #                        [0, 0, 2, 1, 0, 1, 0],
    #                        [0, 2, 1, 1, 1, 2, 0]])
    #
    # Game(Player(1), EnginePlayer(2, depth=6), init_game=game_state, init_user_id=2).run()

    # game_state = np.array([[0, 1, 1, 0, 0, 0, 0],
    #                        [0, 1, 2, 0, 2, 0, 0],
    #                        [0, 2, 1, 0, 1, 0, 0],
    #                        [0, 1, 2, 0, 2, 0, 0],
    #                        [1, 2, 1, 0, 2, 2, 0],
    #                        [2, 1, 2, 1, 1, 2, 0]])
    #
    # Game(Player(1), EnginePlayer(2, depth=6), init_game=game_state, init_user_id=1).run()
