from unittest import TestCase

import numpy as np

from src.connect_x.connect_x_game import Game
from src.engine.engine_player import EnginePlayer


class TestParameters(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super()
        cls.num_in_row_to_win = 4
        cls.num_cols = 7
        cls.num_rows = 6

        cls.engine1 = EnginePlayer(1, depth=6, num_in_row_to_win=cls.num_in_row_to_win, num_rows=cls.num_rows,
                                   num_cols=cls.num_cols, use_test_eval_method=False, display_messages=False)
        cls.engine2 = EnginePlayer(2, depth=6, num_in_row_to_win=cls.num_in_row_to_win, num_rows=cls.num_rows,
                                   num_cols=cls.num_cols, use_test_eval_method=True, display_messages=False)

        cls.results = {"1-win": 0, "2-win": 0, "tie": 0, "1-invalid": 0, "2-invalid": 0}

    @classmethod
    def tearDownClass(cls) -> None:
        print("\n\nTest Results: \n" + str(cls.results))

    def setUp(self) -> None:
        print()  # so logging starts on new line for each test

    def get_game(self, init_game, starting_user):
        return Game(
            self.engine1,
            self.engine2,
            num_in_row_to_win=self.num_in_row_to_win,
            num_rows=self.num_rows,
            num_cols=self.num_cols,
            display_messages=False,
            init_game=init_game,
            init_user_id=starting_user
        )

    def add_result(self, invalid_move_user, winning_user):
        if winning_user != 0:
            result = str(winning_user) + "-win"
        elif invalid_move_user != 0:
            result = str(winning_user) + "-invalid"
        else:
            result = "tie"
        print(f"Adding {result}")
        self.results[result] += 1

    @staticmethod
    def switch_user_ids(game_state) -> np.ndarray:
        return np.array([[(val % 2) + 1 if val != 0 else val for val in row] for row in game_state])

    def test_default(self):
        init_game = np.zeros([6, 7]).astype(int)
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

    def test_pos_1(self):
        init_game = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [2, 0, 0, 0, 0, 0, 0]])
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        init_game = self.switch_user_ids(init_game)
        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

    def test_pos_2(self):
        init_game = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 2, 0, 0, 0, 0, 0]])
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        init_game = self.switch_user_ids(init_game)
        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

    def test_pos_3(self):
        init_game = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 2, 0, 0, 0, 0]])
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        init_game = self.switch_user_ids(init_game)
        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

    def test_pos_4(self):
        init_game = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 2, 0, 0, 0]])
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        init_game = self.switch_user_ids(init_game)
        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

    def test_pos_5(self):
        init_game = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 2, 0, 0]])
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        init_game = self.switch_user_ids(init_game)
        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

    def test_pos_6(self):
        init_game = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 2, 0]])
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        init_game = self.switch_user_ids(init_game)
        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

    def test_pos_7(self):
        init_game = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 2]])
        game = self.get_game(init_game, 1)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)

        init_game = self.switch_user_ids(init_game)
        game = self.get_game(init_game, 2)
        winning_user, end_game, invalid_move_user, num_of_turns = game.run()
        self.add_result(invalid_move_user, winning_user)
