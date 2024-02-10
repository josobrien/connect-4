import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt

from src.connect4.Player import Player
from src.connect4.connect4_utils import is_valid_move, add_move_to_game, get_next_player_id, check_win


class Game:
    def __init__(self, player1: Player, player2: Player, init_user: int = 1, init_game=np.zeros([6, 7]).astype(int),
                 display_messages: bool = True):
        self.player1 = player1
        self.player2 = player2
        self.player_ids = [player1.player_id, player2.player_id]
        self.current_game = init_game.copy()
        self.current_user = init_user
        self.display_messages = display_messages

    def run(self):
        game_ended = False
        winning_user, invalid_move_user, turn_num = 0, 0, 0

        while not game_ended:
            turn_num += 1
            if self.display_messages:
                self.display_game()

            game_ended, winning_user, invalid_move_user = self.perform_move()

            if self.check_full():
                break

        if self.display_messages:
            self.display_game()
            if winning_user != 0 or invalid_move_user != 0:
                print("Player " + str(winning_user) + " won!")
            else:
                print("Game over, draw.")

        return winning_user, self.current_game, invalid_move_user, turn_num

    def get_input(self):
        if self.current_user == self.player1.player_id:
            return self.player1.get_move(self.current_game)
        else:
            return self.player2.get_move(self.current_game)

    def perform_move(self):
        column = self.get_input()
        if not is_valid_move(self.current_game, column):
            return True, self.get_next_player_id(), self.current_user

        self.current_game, new_move_y_position = add_move_to_game(self.current_game, column, self.current_user)

        is_win = check_win(column, new_move_y_position, self.current_game, self.current_user)

        if not is_win:
            # increment user
            self.current_user = self.get_next_player_id()
            return False, 0, 0
        else:
            return True, self.current_user, 0

    def get_next_player_id(self):
        return get_next_player_id(self.player_ids, self.current_user)

    def check_full(self):
        if 0 not in self.current_game[0]:
            return True
        return False

    def random_agent_move(self):
        # assumes grid is not full
        random_move = np.random.randint(0, 7)
        while self.current_game[0][random_move] != 0:
            random_move = np.random.randint(0, 7)
        print(f"Random move: {random_move}")
        return random_move

    def display_game(self):
        print(self.current_game)
        print("  0-1-2-3-4-5-6")
        # sns.heatmap(self.current_game, cbar=False).axes.get_yaxis().set_visible(False)  # TODO: display better
        # plt.show()
