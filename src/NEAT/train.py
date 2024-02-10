import os
import pickle

from src.NEAT.connect_4_neat import run

best_net_file = "NEAT/winner1.pkl"

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    winner = run(config_path, 50)

    with open(best_net_file, "wb") as f:
        pickle.dump(winner, f)
