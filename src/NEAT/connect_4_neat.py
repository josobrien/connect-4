# DQN or NEAT
# from rl.agents.dqn import DQNAgent
# import gym
#
# np.random.seed(123)
import neat

from src.connect4.Connect4Game import Game
from src.NEAT.NEATPlayer import NEATPlayer


def fitness(genomes, config):
    nets = [neat.nn.FeedForwardNetwork.create(genome, config) for [_, genome] in genomes]

    for [_, genome] in genomes:
        genome.fitness = 0

    for i in range(0, len(nets)):
        net_2_id = (i+1) % (len(nets))
        net_3_id = (i+2) % (len(nets))
        net_4_id = (i+3) % (len(nets))

        _, genome_1 = genomes[i]
        _, genome_2 = genomes[net_2_id]
        _, genome_3 = genomes[net_3_id]
        _, genome_4 = genomes[net_4_id]

        winning_player, end_grid, invalid_move_player, turn_num = Game(NEATPlayer(1, nets[i]), NEATPlayer(2, nets[net_2_id]), display_messages=False).run()
        genome_1.fitness, genome_2.fitness = generate_fitnesses(winning_player, end_grid, invalid_move_player, turn_num, genome_1.fitness, genome_2.fitness)

        winning_player, end_grid, invalid_move_player, turn_num = Game(NEATPlayer(1, nets[i]), NEATPlayer(2, nets[net_3_id]), display_messages=False).run()
        genome_1.fitness, genome_3.fitness = generate_fitnesses(winning_player, end_grid, invalid_move_player, turn_num, genome_1.fitness, genome_3.fitness)

        winning_player, end_grid, invalid_move_player, turn_num = Game(NEATPlayer(1, nets[i]), NEATPlayer(2, nets[net_4_id]), display_messages=False).run()
        genome_1.fitness, genome_4.fitness = generate_fitnesses(winning_player, end_grid, invalid_move_player, turn_num, genome_1.fitness, genome_4.fitness)


def generate_fitnesses(winning_player, game_grid, invalid_move_player, turn_num, p1_init_fitness, p2_init_fitness):
    genome_1_fitness = p1_init_fitness
    genome_2_fitness = p2_init_fitness
    genome_1_fitness += turn_num*2
    genome_2_fitness += turn_num*2
    if invalid_move_player != 0:
        if invalid_move_player == 1:
            genome_1_fitness -= 100
        else:
            genome_2_fitness -= 100
    elif winning_player != 0:
        if winning_player == 1:
            genome_1_fitness += 30
            genome_2_fitness -= 30
        else:
            genome_2_fitness += 30
            genome_1_fitness -= 30
    # else:
        # reward for more in a row?
        # reward for blocking 3 in a row?
    return genome_1_fitness, genome_2_fitness


def run(config_path, generations=0):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5))

    if generations:
        # Run for up to x generations.
        winner = p.run(fitness, generations)
    else:
        # Run until desired fitness reached
        winner = p.run(fitness)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))

    return winner

