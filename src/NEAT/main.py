import os
import pickle

import neat

from src.connect4.Connect4Game import Game
from src.NEAT.NEATPlayer import NEATPlayer
from src.connect4.Player import Player
from src.NEAT.train import best_net_file

# play against best genome from train
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    with open(best_net_file, "rb") as f:
        genome = pickle.load(f)
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    Game(Player(1), NEATPlayer(2, net), display_messages=True).run()


# if __name__ == "__main__":
#     Game(Player(1), Player(-1), display_messages=True).run()
