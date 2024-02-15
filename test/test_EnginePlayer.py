from unittest import TestCase

import numpy as np

from src.engine.engine_player import EnginePlayer


class Test(TestCase):
    def test_engine_player_1_forced_win(self):
        game_state = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 2, 2, 1, 0, 0],
                               [1, 0, 1, 2, 2, 0, 0],
                               [2, 0, 2, 1, 2, 0, 0],
                               [2, 0, 1, 1, 1, 0, 0],
                               [2, 0, 1, 1, 2, 0, 1]])

        player_id = 2
        depth = 3
        player = EnginePlayer(player_id, depth=depth)
        move, value = player.evaluate_possible_positions(game_state, player.is_maximising_player, player.depth, -100000, 100000)

        self.assertGreater(value, 500)

    def test_engine_player_2_blocks_win(self):
        game_state = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 2, 2, 1, 0, 0],
                               [1, 0, 1, 2, 2, 0, 0],
                               [2, 0, 2, 1, 2, 0, 0],
                               [2, 0, 2, 1, 1, 0, 0],
                               [2, 0, 1, 1, 2, 0, 1]])

        player_id = 2
        depth = 1
        player = EnginePlayer(player_id, depth=depth)
        move, value = player.evaluate_possible_positions(game_state, player.is_maximising_player, player.depth, -100000, 100000)

        self.assertGreater(value, -40)
        self.assertLess(value, 40)

    def test_engine_player_2_blocks_win_causing_pruning(self):
        # TODO test that pruning is working
        game_state = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0, 0, 0],
                               [1, 0, 0, 2, 0, 0, 0],
                               [1, 0, 0, 2, 0, 0, 0]])

        player_id = 2
        depth = 3
        player = EnginePlayer(player_id, depth=depth)
        move, value = player.evaluate_possible_positions(game_state, player.is_maximising_player, player.depth, -100000, 100000)

        self.assertGreater(value, -40)
        self.assertLess(value, 40)

    def test_engine_player_2_win_with_depth_at_least_6(self):
        game_state = np.array([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 2, 2, 0, 0, 0],
                               [0, 0, 2, 1, 1, 1, 0],
                               [0, 2, 1, 1, 1, 2, 0]])

        player_id = 2
        depth = 6
        player = EnginePlayer(player_id, depth=depth)
        move, value = player.evaluate_possible_positions(game_state, player.is_maximising_player, player.depth, -100000, 100000)

        self.assertLess(value, -500)
