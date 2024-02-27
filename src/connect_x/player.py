class Player:
    def __init__(self, player_id):
        self.player_id = player_id

    def get_move(self, current_game):
        # TODO validate input
        return int(input(f"Player {self.player_id} input column: ")) - 1

    @staticmethod
    def transform_grid(game_grid):
        # requires that a player exists with id 1. could be more general
        return [[i if i == 1 else -1 for i in row] for row in game_grid]
