from unittest import TestCase

import numpy as np

from src.connect_x.utils.general_evaluation_utils import EvalUtils


class Test(TestCase):
    def setUp(self) -> None:
        self.eval_utils = EvalUtils(num_in_row_to_win=4, num_rows=6, num_cols=7)

    def test_get_possible_wins(self):
        grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 2, 0, 0],
                              [0, 0, 0, 0, 1, 2, 0],
                              [1, 1, 0, 1, 1, 1, 2]])

        actual = self.eval_utils.get_unblocked_x_in_row_possibilities(grid_test)
        self.assertEqual({1: [3, 2, 2], 2: [3]}, actual)

    # TODO for after future improvements
    # def test_get_possible_wins2(self):
    #     grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 1, 1, 0, 1, 1]])
    #
    #     actual = get_unblocked_x_in_row_possibilities(grid_test)
    #     self.assertEqual({1: [2, 3], 2: []}, actual)
    #
    # def test_get_possible_wins3(self):
    #     grid_test = np.array([[0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 0, 0, 0, 0, 0],
    #                           [0, 0, 1, 1, 0, 0, 0]])
    #
    #     actual = get_unblocked_x_in_row_possibilities(grid_test)
    #     self.assertEqual({1: [2, 2], 2: []}, actual)

    """
    input - expected
    [1 1 0 1 1 1 2] - {1: [1], 2: []}
    [0 0 1 1 0 1 1] - {1: [2, 1], 2: []}
    [0 0 1 1 0 0 0] - {1: [2, 2], 2: []}
    [0 1 1 0 0 0 0] - {1: [2], 2: []}
    [1 0 1 0 1 0 1] - {1: [2], 2: []}
    [0 0 1 1 1 0 0] - {1: [1, 1], 2: []}
    [1 1 0 0 1 1 1] - {1: [1], 2: []}
    """

    # def test_add_unblocked_possibilities_from_row(self):
    #     row_test = [1, 1, 0, 1, 1, 1, 2]
    #
    #     result = {1: [], 2: []}
    #     add_unblocked_possibilities_from_row(result, row_test)
    #
    #     self.assertEqual({1: [1], 2: []}, result)
    #
    # def test_add_unblocked_possibilities_from_row2(self):
    #     row_test = [0, 0, 1, 1, 0, 1, 1]
    #
    #     result = {1: [], 2: []}
    #     add_unblocked_possibilities_from_row(result, row_test)
    #
    #     self.assertEqual({1: [2, 1], 2: []}, result)
    #
    # def test_add_unblocked_possibilities_from_row3(self):
    #     row_test = [0, 0, 1, 1, 0, 0, 0]
    #
    #     result = {1: [], 2: []}
    #     add_unblocked_possibilities_from_row(result, row_test)
    #
    #     self.assertEqual({1: [2, 2], 2: []}, result)
    #
    # def test_add_unblocked_possibilities_from_row4(self):
    #     row_test = [0, 1, 1, 0, 0, 0, 0]
    #
    #     result = {1: [], 2: []}
    #     add_unblocked_possibilities_from_row(result, row_test)
    #
    #     self.assertEqual({1: [2], 2: []}, result)
    #
    # def test_add_unblocked_possibilities_from_row5(self):
    #     row_test = [1, 0, 1, 0, 1, 0, 1]
    #
    #     result = {1: [], 2: []}
    #     add_unblocked_possibilities_from_row(result, row_test)
    #
    #     self.assertEqual({1: [2], 2: []}, result)
    #
    # def test_add_unblocked_possibilities_from_row6(self):
    #     row_test = [0, 0, 1, 1, 1, 0, 0]
    #
    #     result = {1: [], 2: []}
    #     add_unblocked_possibilities_from_row(result, row_test)
    #
    #     self.assertEqual({1: [1, 1], 2: []}, result)
    #
    # def test_add_unblocked_possibilities_from_row7(self):
    #     row_test = [1, 1, 0, 0, 1, 1, 1]
    #
    #     result = {1: [], 2: []}
    #     add_unblocked_possibilities_from_row(result, row_test)
    #
    #     self.assertEqual({1: [1], 2: []}, result)
