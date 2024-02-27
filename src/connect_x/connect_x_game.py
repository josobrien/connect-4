import numpy as np

from src.connect_x.player import Player
from src.connect_x.utils.game_utils import display_game, check_full, Utils


class Game:
    def __init__(self, player1: Player, player2: Player, init_user_id: int = 1, init_game=None,
                 display_messages: bool = True, num_in_row_to_win=4, num_rows=6, num_cols=7):
        self.player1 = player1
        self.player2 = player2
        self.player_ids = [player1.player_id, player2.player_id]
        self.current_user = player1 if init_user_id == player1.player_id else player2
        self.display_messages = display_messages
        self.utils = Utils(num_in_row_to_win, num_rows, num_cols)
        if init_game is None:
            self.current_game = np.zeros([num_rows, num_cols]).astype(int)
        else:
            self.current_game = init_game.copy()

    def run(self):
        game_ended = False
        winning_user, invalid_move_user, turn_num = 0, 0, 0

        while not game_ended:
            turn_num += 1
            if self.display_messages:
                self.display_current_game()

            game_ended, winning_user, invalid_move_user = self.perform_move()

            if check_full(self.current_game):
                break

        if self.display_messages:
            self.display_current_game()
            if winning_user != 0 or invalid_move_user != 0:
                print("Player " + str(winning_user) + " won!")
            else:
                print("Game over, draw.")

        return winning_user, self.current_game, invalid_move_user, turn_num

    def get_input(self):
        return self.current_user.get_move(self.current_game)

    def perform_move(self):
        column = self.get_input()
        if not self.utils.is_valid_move(self.current_game, column):
            return True, self.get_next_player_id(), self.current_user.player_id

        self.current_game, new_move_y_position = self.utils.add_move_to_game(self.current_game, column, self.current_user.player_id)

        is_win = self.utils.check_win(column, new_move_y_position, self.current_game, self.current_user.player_id)

        if not is_win:
            # increment user
            self.current_user = self.get_next_player_id()
            return False, 0, 0
        else:
            return True, self.current_user.player_id, 0

    def get_next_player_id(self):
        return self.player2 if self.current_user == self.player1 else self.player1

    def random_agent_move(self):
        # assumes grid is not full
        random_move = np.random.randint(0, 7)
        while self.current_game[0][random_move] != 0:
            random_move = np.random.randint(0, 7)
        print(f"Random move: {random_move}")
        return random_move

    def display_current_game(self):
        display_game(self.current_game)
