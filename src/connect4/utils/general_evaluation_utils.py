
def get_unblocked_4_in_row_possibilities(game_state) -> dict:
    result = {1: [], 2: []}  # TODO do this without hard coding player IDs?

    # vertical
    for col in range(7):
        count, for_player_id, space_above = 0, 0, 0
        for row in range(6):
            if game_state[row][col] == 0:
                space_above += 1
            else:
                if for_player_id == 0:
                    for_player_id = game_state[row][col]
                    count += 1
                elif game_state[row][col] == for_player_id:
                    count += 1
                else:
                    break

        if count > 1 and space_above + count >= 4:
            result[for_player_id].append(count)

    # horizontal
    for row in game_state:
        add_unblocked_possibilities_from_row(result, row)

    # diagonals (where space allows - e.g. x, y coords (0, 4), (1, 5): four in a row not possible)
    # FYI: game_state[row][col]
    for i in range(-2, 4):
        diagonal_down_right = []
        diagonal_down_left = []
        if i < 0:
            for j in range(6 + i):
                diagonal_down_right.append(game_state[j - i][j])  # e.g. x, y coords: (0, 2), (1, 3), (2, 4), (3, 5)
                diagonal_down_left.append(game_state[j - i][6 - j])
        else:
            for j in range(min(6, 7-i)):
                diagonal_down_right.append(game_state[j][j + i])
                diagonal_down_left.append(game_state[j][6 - i - j])

        add_unblocked_possibilities_from_row(result, diagonal_down_right)
        add_unblocked_possibilities_from_row(result, diagonal_down_left)

    """
    boundaries (between these (inclusive), four in a row is possible)
    boundaries for down-right:
    0 [[0, 0, 0, X, 0, 0, 0],
    1  [0, 0, 0, 0, X, 0, 0],
    2  [X, 0, 0, 0, 0, X, 0],
    3  [0, X, 0, 0, 0, 0, X],
    4  [0, 0, X, 0, 0, 0, 0],
    5  [0, 0, 0, X, 0, 0, 0]]
        0  1  2  3  4  5  6

    boundaries for down-left:
    0 [[0, 0, 0, X, 0, 0, 0],
    1  [0, 0, X, 0, 0, 0, 0],
    2  [0, X, 0, 0, 0, 0, X],
    3  [X, 0, 0, 0, 0, X, 0],
    4  [0, 0, 0, 0, X, 0, 0],
    5  [0, 0, 0, X, 0, 0, 0]]
        0  1  2  3  4  5  6
    """

    return result


def add_unblocked_possibilities_from_row(result, row):
    # TODO: currently only checks for adjacent pieces in a row e.g. 1 1 1 0 = 3
    #       but if any 3 out of 4 are same player and other is 0 e.g. 1 0 1 1, it should count as 3 (currently counts 2)

    # TODO: score should be based on how many 0s need to be filled in to win.
    #       refactor to return num of 0s required to change to win? (current->new: 4->0, 3->1, 2->2)
    #       once a zero has been counted in a result, don't count it again for current user
    #  -
    #  example           desired result (current scoring method)
    #  [1 1 0 1 1 1 2] - {1: [3]}
    #  [0 0 1 1 0 1 1] - {1: [2, 3]}
    #  [0 0 1 1 0 0 0] - {1: [2, 2]}
    #  [0 1 1 0 0 0 0] - {1: [2]}
    #  [1 0 1 0 1 0 1] - {1: [2]}
    #  [0 0 1 1 1 0 0] - {1: [3, 3]}
    #  [1 1 0 0 1 1 1] - {1: [3]}
    #  [1 1 1 0 2 2 2] - {1: [3], 2: [3]}

    # TODO: duplicate method before refactoring to return 0s
    #  once implemented, compare old method with new method. get old/new engines to play against each other

    count, prev_val, left_space, right_space, temp_player_id = 0, 0, 0, 0, 0
    for val in row:
        if val == 0:
            right_space += 1
        else:
            if prev_val == val:
                count += 1
            else:
                if count >= 2 and left_space + right_space + count >= 4:
                    result[temp_player_id].append(count)
                left_space = right_space
                right_space = 0
                count = 1
            temp_player_id = val
        prev_val = val

    if count >= 2 and left_space + right_space + count >= 4:
        result[temp_player_id].append(count)


def add_unblocked_possibilities_from_row1(result, row):
    # TODO not correct - e.g. [1 1 0 1 1 1 2] give 5 for player 1. should be 3
    count, currently_counting, right_space, other_space = 0, 0, 0, 0
    for val in row:
        if val == 0:
            right_space += 1
        else:
            if currently_counting == val:
                count += 1
                other_space += right_space
                right_space = 0
            elif currently_counting == 0:
                currently_counting = val
                count += 1
                other_space += right_space
                right_space = 0
            else:
                # switch to other player:
                if count >= 2 and right_space + other_space + count >= 4:
                    result[currently_counting].append(count)
                other_space = right_space
                right_space = 0
                count = 0
                currently_counting = val

    if count >= 2 and right_space + other_space + count >= 4:
        result[currently_counting].append(count)


def get_unblocked_4_in_row_possibilities1(game_state) -> dict:
    result = {1: [], 2: []}  # TODO do this without hard coding player IDs?

    # vertical
    for col in range(7):
        count, for_player_id, space_above = 0, 0, 0
        for row in range(6):
            if game_state[row][col] == 0:
                space_above += 1
            else:
                if for_player_id == 0:
                    for_player_id = game_state[row][col]
                    count += 1
                elif game_state[row][col] == for_player_id:
                    count += 1
                else:
                    break

        if count > 1 and space_above + count >= 4:
            result[for_player_id].append(count)

    # horizontal
    for row in game_state:
        add_unblocked_possibilities_from_row1(result, row)

    # diagonals (where space allows - e.g. x, y coords (0, 4), (1, 5): four in a row not possible)
    # FYI: game_state[row][col]
    for i in range(-2, 4):
        diagonal_down_right = []
        diagonal_down_left = []
        if i < 0:
            for j in range(6 + i):
                diagonal_down_right.append(game_state[j - i][j])  # e.g. x, y coords: (0, 2), (1, 3), (2, 4), (3, 5)
                diagonal_down_left.append(game_state[j - i][6 - j])
        else:
            for j in range(min(6, 7 - i)):
                diagonal_down_right.append(game_state[j][j + i])
                diagonal_down_left.append(game_state[j][6 - i - j])

        add_unblocked_possibilities_from_row1(result, diagonal_down_right)
        add_unblocked_possibilities_from_row1(result, diagonal_down_left)

    """
    boundaries (between these (inclusive), four in a row is possible)
    boundaries for down-right:
    0 [[0, 0, 0, X, 0, 0, 0],
    1  [0, 0, 0, 0, X, 0, 0],
    2  [X, 0, 0, 0, 0, X, 0],
    3  [0, X, 0, 0, 0, 0, X],
    4  [0, 0, X, 0, 0, 0, 0],
    5  [0, 0, 0, X, 0, 0, 0]]
        0  1  2  3  4  5  6

    boundaries for down-left:
    0 [[0, 0, 0, X, 0, 0, 0],
    1  [0, 0, X, 0, 0, 0, 0],
    2  [0, X, 0, 0, 0, 0, X],
    3  [X, 0, 0, 0, 0, X, 0],
    4  [0, 0, 0, 0, X, 0, 0],
    5  [0, 0, 0, X, 0, 0, 0]]
        0  1  2  3  4  5  6
    """

    return result
