from src.connect4.player import Player
from src.connect4.connect4_utils import is_valid_move, add_move_to_game, get_unblocked_4_in_row_possibilities, \
    get_next_player_id, check_win


class EnginePlayer(Player):
    # TODO player IDs are hard coded throughout. could be better
    def __init__(self, player_id, depth=5):
        super().__init__(player_id)
        self.depth = depth
        self.is_maximising_player = player_id == 1

    def get_move(self, current_game):
        # positive is good for player 1, negative is good for player 2

        move, value = self.evaluate_possible_positions(current_game, self.is_maximising_player, self.depth, -100000, 100000)

        print(f"Computer move: {move}, eval: {value}")
        return move

    def evaluate_possible_positions(self, current_game, is_maximising_player, depth, alpha, beta):
        max_eval, min_eval = -100000, 100000
        best_move = -1

        player_turn = 1 if is_maximising_player else 2

        for possible_move in [0, 1, 2, 3, 4, 5, 6]:
            if not is_valid_move(current_game, possible_move):
                value = 10000 * (-1 if is_maximising_player else 1)
            else:
                game_after_move, new_move_y_position = add_move_to_game(current_game, possible_move, player_turn)

                if depth == 0 or check_win(possible_move, new_move_y_position, game_after_move, player_turn):
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

    @staticmethod
    def evaluate_position(game_state):
        # TODO just return as soon as 4 in row found
        possible_wins_per_player = get_unblocked_4_in_row_possibilities(game_state)

        evaluation = 0

        for player, possible_wins in possible_wins_per_player.items():
            multiplier = 1 if player == 1 else -1
            for val in possible_wins:
                if val >= 4:
                    evaluation += 1000 * multiplier
                elif val == 3:
                    evaluation += 8 * multiplier
                else:
                    evaluation += 3 * multiplier

        # TODO evaluation improvements:
        #   centre of the board better?
        #   improve possibility checking (TODO in add_unblocked_possibilities_from_row in utils)

        return evaluation
