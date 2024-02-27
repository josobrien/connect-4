import numpy as np

from src.connect_x.connect_x_game import Game
from src.connect_x.player import Player
from src.engine.engine_player import EnginePlayer

if __name__ == "__main__":
    num_in_row_to_win = 4
    num_rows = 6
    num_cols = 7

    engine_player = EnginePlayer(2, depth=6, num_in_row_to_win=num_in_row_to_win, num_rows=num_rows, num_cols=num_cols)
    # engine_player1 = EnginePlayer(1, depth=6, num_in_row_to_win=num_in_row_to_win, num_rows=num_rows, num_cols=num_cols)

    Game(Player(1), engine_player, num_in_row_to_win=num_in_row_to_win, num_rows=num_rows, num_cols=num_cols).run()

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
