import numpy as np

from src.connect4.colours import Colours


def is_valid_move(game_state, column) -> bool:
    if type(column) != int or not 0 <= column <= 6:
        print("Invalid, column doesn't exist.")
        return False
    if game_state[0, column] != 0:
        # print("Invalid, column is full.")
        return False
    return True


def check_win(x, y, current_game, current_user):
    # vertical
    if y <= 2:
        if np.all(current_game[y + 1:y + 4, x] == [current_user, current_user, current_user]):
            return True

    # TODO find out which of the following horizontal algs is faster
    #  how to test? (remember most of the time this will be returning false)
    # horizontal
    num_connected_hori = 0
    for i in range(7):
        if current_game[y, i] == current_user:
            if num_connected_hori == 3:
                return True
            num_connected_hori += 1
        else:
            num_connected_hori = 0

    # horizontal
    # num_connected_hori, count = 0, 0
    # test = False
    # for i in range(6):
    #     if current_game[y, x + count] == current_user:
    #         if num_connected_hori == 3:
    #             return True
    #         num_connected_hori += 1
    #         if test:
    #             count -= 1
    #         else:
    #             count += 1
    #     elif i > 0:
    #         test = True
    #         count = 0
    #     else:
    #         break

    # diagonals
    num_connected_diag1 = 0
    for i in range(x - 3, x + 4):
        if 0 <= i <= 6:
            if 0 <= y + (x - i) <= 5:
                if current_game[y + (x - i), i] == current_user:
                    num_connected_diag1 += 1
                else:
                    num_connected_diag1 = 0
                if num_connected_diag1 == 4:
                    return True

    num_connected_diag2 = 0
    for i in range(x - 3, x + 4):
        if 0 <= i <= 6:
            if 0 <= y - (x - i) <= 5:
                if current_game[y - (x - i), i] == current_user:
                    num_connected_diag2 += 1
                else:
                    num_connected_diag2 = 0
                if num_connected_diag2 == 4:
                    return True

    return False


def add_move_to_game(game_state, column, current_user):
    game_state_copy = np.copy(game_state)
    for i in range(6):
        if game_state_copy[5 - i, column] == 0:
            game_state_copy[5 - i, column] = current_user
            new_move_y_position = 5 - i
            break

    return game_state_copy, new_move_y_position


def get_next_player_id(player_ids, current_user):
    return player_ids[(player_ids.index(current_user) + 1) % 2]


def display_game(game_state):
    output_game_state = str(game_state)

    output_game_state = output_game_state.replace("[", "")
    output_game_state = output_game_state.replace("]", "")
    output_game_state = output_game_state.replace("\n ", "\n")
    output_game_state = output_game_state.replace("1", f"{Colours.YELLOW}1{Colours.DEFAULT}")
    output_game_state = output_game_state.replace("2", f"{Colours.RED}2{Colours.DEFAULT}")

    output_game_state = Colours.DEFAULT + output_game_state

    # for char in str(game_state):
    #     if char == "1":
    #         output_game_state += Colours.YELLOW + char + Colours.DEFAULT
    #     elif char == "2":
    #         output_game_state += Colours.RED + char + Colours.DEFAULT
    #     elif char == "[" or char == "]":
    #         continue
    #     else:
    #         output_game_state += char

    print(output_game_state)
    print("1-2-3-4-5-6-7")
