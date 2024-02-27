from neat.nn import FeedForwardNetwork

from src.connect_x.player import Player


class NEATPlayer(Player):
    def __init__(self, player_id, net: FeedForwardNetwork):
        super().__init__(player_id)
        self.net = net

    def get_move(self, current_game):
        current_game = self.transform_grid(current_game)

        output = self.net.activate([num for row in current_game for num in row])
        # print(output)

        move = max(range(len(output)), key=output.__getitem__)

        # print(f"Computer move: {move}")
        return move
