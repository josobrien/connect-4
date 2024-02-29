from src.connect_x.player import Player
from src.connect_x.utils.game_utils import Utils, check_full
from src.connect_x.utils.general_evaluation_utils import EvalUtils


class EnginePlayer(Player):
    # TODO player IDs are hard coded throughout. could be better
    def __init__(self, player_id, depth=5, num_in_row_to_win=4, num_rows=6, num_cols=7, use_test_eval_method=False, display_messages=True):
        super().__init__(player_id)
        self.depth = depth
        self.is_maximising_player = player_id == 1
        self.num_in_row_to_win = num_in_row_to_win
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.utils = Utils(num_in_row_to_win, num_rows, num_cols)
        self.evaluation_utils = EvalUtils(num_in_row_to_win, num_rows, num_cols)
        self.use_test_eval_method = use_test_eval_method
        self.display_messages = display_messages
        self.column_nums_in_order = self.get_column_nums_in_order(num_cols)

    def get_move(self, current_game):
        # positive is good for player 1, negative is good for player 2

        move, value = self.evaluate_possible_positions(current_game, self.is_maximising_player, self.depth, -100000, 100000)

        if self.display_messages:
            print(f"Computer {self.player_id} move: {move + 1}, eval: {value}")

        return move

    def evaluate_possible_positions(self, current_game, is_maximising_player, depth, alpha, beta):
        max_eval, min_eval = -100000, 100000
        best_move = -1

        player_turn = 1 if is_maximising_player else 2

        for possible_move in self.column_nums_in_order:
            if check_full(current_game):
                value = 0
            elif not self.utils.is_valid_move(current_game, possible_move):
                value = 20000 * (-1 if is_maximising_player else 1)
            else:
                game_after_move, new_move_y_position = self.utils.add_move_to_game(current_game, possible_move, player_turn)

                if self.utils.check_win(possible_move, new_move_y_position, game_after_move, player_turn):
                    value = 10000 * (1 if is_maximising_player else -1)
                elif depth == 0:
                    value = self.evaluate_position(game_after_move)
                else:
                    _, value = self.evaluate_possible_positions(game_after_move, not is_maximising_player, depth - 1, alpha, beta)

            if is_maximising_player:
                alpha = max(alpha, value)
                if value > max_eval:
                    max_eval = value
                    best_move = possible_move
            else:
                beta = min(beta, value)
                if value < min_eval:
                    min_eval = value
                    best_move = possible_move

            if beta <= alpha:
                break

        best_value = max_eval if is_maximising_player else min_eval

        return best_move, best_value

    def evaluate_position(self, game_state):
        # TODO just return as soon as X in row found
        possible_wins_per_player = self.evaluation_utils.get_unblocked_x_in_row_possibilities(game_state)

        evaluation = 0

        for player, possible_wins in possible_wins_per_player.items():
            multiplier = 1 if player == 1 else -1
            for val in possible_wins:
                # TODO experiment with different eval calculations
                if val >= self.num_in_row_to_win:
                    return 10000 * multiplier
                if not self.use_test_eval_method:
                    if val >= 2:
                        evaluation += (2**val - 1) * multiplier
                else:
                    if val == 3:
                        evaluation += 5 * multiplier
                    elif val == 2:
                        evaluation += 2 * multiplier

        # TODO evaluation improvements:
        #   centre of the board better?
        #   improve possibility checking (TODO in add_unblocked_possibilities_from_row in utils)

        return evaluation

    @staticmethod
    def get_column_nums_in_order(num_cols):
        # middle columns more likely to be better, so put those first
        result = []
        middle_col = num_cols // 2
        if num_cols % 2 == 0:
            result.append(middle_col - 1)
            result.append(middle_col)
            for i in range(1, middle_col):
                result.append(middle_col - i - 1)
                result.append(middle_col + i)
        else:
            result.append(middle_col)
            for i in range(1, middle_col + 1):
                result.append(middle_col - i)
                result.append(middle_col + i)

        return result
