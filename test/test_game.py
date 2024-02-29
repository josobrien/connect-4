from unittest import TestCase

import numpy as np

from src.connect_x.utils.game_utils import Utils


class UnitTests(TestCase):
    def setUp(self) -> None:
        self.utils = Utils(num_in_row_to_win=4, num_rows=6, num_cols=7)

    def test_check_win_horizontal_coords_A(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 0, 0, 0]])

        actual = self.utils.check_win(3, 5, grid_test, 1)
        self.assertTrue(actual)

    def test_check_win_horizontal_coords_B(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 0, 0, 0]])

        actual = self.utils.check_win(0, 5, grid_test, 1)
        self.assertTrue(actual)

    def test_check_win_horizontal_edge_wrap(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 0, 0, 0, 1]])

        actual = self.utils.check_win(0, 5, grid_test, 1)
        self.assertFalse(actual)

    def test_check_win_vertical(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0]])

        actual = self.utils.check_win(2, 2, grid_test, 1)
        self.assertTrue(actual)

    def test_check_win_diagonal1(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0],
                              [0, 0, 2, 1, 0, 0, 0],
                              [0, 0, 1, 2, 1, 0, 0],
                              [0, 2, 1, 2, 2, 1, 0]])

        actual = self.utils.check_win(2, 2, grid_test, 1)
        self.assertTrue(actual)

    def test_check_win_diagonal2(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1, 1, 0],
                              [0, 0, 0, 1, 2, 2, 0],
                              [0, 2, 1, 2, 2, 1, 0]])

        actual = self.utils.check_win(5, 2, grid_test, 1)
        self.assertTrue(actual)

    def test_check_win_no_win(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 2, 0, 0],
                              [0, 0, 0, 0, 1, 2, 0],
                              [1, 1, 0, 1, 1, 1, 2]])

        actual = self.utils.check_win(4, 3, grid_test, 1)
        self.assertEqual(False, actual)

    # TODO more testing of the game code
    # def test_perform_move_1(self):
    #     grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [1, 1, 1, 0, 0, 0, 0]])
    #
    #     expected = np.array([[0, 0, 0, 0, 0, 0, 0],
    #                          [0, 0, 0, 0, 0, 0, 0],
    #                          [0, 0, 0, 0, 0, 0, 0],
    #                          [0, 0, 0, 0, 0, 0, 0],
    #                          [0, 0, 0, 0, 0, 0, 0],
    #                          [1, 1, 1, 1, 0, 0, 0]])
    #
    #     temp = Game(init_game=grid_test, init_user=1)
    #     temp.perform_move(3)
    #     actual = temp.current_game
    #     self.assertEqual(expected, actual)
    #
    # def test_perform_move_2(self):
    #     grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 1, 2, 0],
    #                           [1, 1, 0, 1, 1, 1, 2]])
    #
    #     expected = np.array([[0, 0, 0, 0, 0, 0, 0],
    #                          [0, 0, 0, 0, 0, 0, 0],
    #                          [0, 0, 0, 0, 0, 0, 0],
    #                          [0, 0, 0, 0, 2, 0, 0],
    #                          [0, 0, 0, 0, 1, 2, 0],
    #                          [1, 1, 0, 1, 1, 1, 2]])
    #
    #     temp = Game(init_game=grid_test, init_user=2)
    #     temp.perform_move(4)
    #     actual = temp.current_game
    #     self.assertEqual(expected, actual)
