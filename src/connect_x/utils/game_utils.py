import numpy as np

from src.connect_x.utils.colours import Colours


class Utils:
    def __init__(self, num_in_row_to_win, num_rows, num_cols):
        self.num_in_row_to_win = num_in_row_to_win
        self.num_rows = num_rows
        self.num_cols = num_cols

    def is_valid_move(self, game_state, column) -> bool:
        if type(column) != int or not 0 <= column < self.num_cols:
            print("Invalid, column doesn't exist.")
            return False
        if game_state[0, column] != 0:
            return False
        return True

    def check_win(self, x, y, current_game, current_user):
        # vertical
        if y <= self.num_rows - self.num_in_row_to_win:
            if np.all(current_game[y+1:y+self.num_in_row_to_win, x] == [current_user] * (self.num_in_row_to_win-1)):
                return True

        # horizontal
        num_connected_hori = 0
        for i in range(self.num_cols):
            if current_game[y, i] == current_user:
                if num_connected_hori == self.num_in_row_to_win-1:
                    return True
                num_connected_hori += 1
            else:
                num_connected_hori = 0

        # diagonals
        num_connected_diag_down_left = 0
        num_connected_diag_down_right = 0
        for i in range(x - self.num_in_row_to_win + 1, x + self.num_in_row_to_win):
            if 0 <= i < self.num_cols:
                row_to_check_down_left = y + (x - i)
                if 0 <= row_to_check_down_left < self.num_rows:
                    if current_game[row_to_check_down_left, i] == current_user:
                        num_connected_diag_down_left += 1
                    else:
                        num_connected_diag_down_left = 0
                    if num_connected_diag_down_left == self.num_in_row_to_win:
                        return True

                row_to_check_down_right = y - (x - i)
                if 0 <= row_to_check_down_right < self.num_rows:
                    if current_game[row_to_check_down_right, i] == current_user:
                        num_connected_diag_down_right += 1
                    else:
                        num_connected_diag_down_right = 0
                    if num_connected_diag_down_right == self.num_in_row_to_win:
                        return True

        return False

    def add_move_to_game(self, game_state, column, current_user):
        game_state_copy = np.copy(game_state)
        for i in range(self.num_rows):
            row_to_check = self.num_rows - 1 - i
            if game_state_copy[row_to_check, column] == 0:
                game_state_copy[row_to_check, column] = current_user
                new_move_y_position = row_to_check
                break

        return game_state_copy, new_move_y_position


def check_full(game_state):
    if 0 not in game_state[0]:
        return True
    return False


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

    print(output_game_state)

    col_labels = "1"
    for i in range(1, len(game_state[0])):
        col_labels += f"-{i+1}"

    print(col_labels)
