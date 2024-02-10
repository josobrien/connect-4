# connect-4

Connect 4 in Python with computer players.

https://en.wikipedia.org/wiki/Connect_Four

This project enables two players to play connect 4 against each other. The players
can be human, but the main purpose of this project is to create non-human players
that can achieve a high level of performance when compared with an average human
player.

## Running code

Pass two players into the `Game` class and call `.run()`

Ready-to-run `main.py` files already exist for the following options:

### Human vs Human

`src/connect4/main.py`

Two human users take turns inputting moves.

### Human vs Engine

`src/engine/main.py`

A human user plays against an engine using the 'minimax' algorithm to evaluate 
potential moves and the future positions they could create.

### Human vs NEAT

`src/NEAT/main.py`

A human user plays against an AI player previously trained using NEAT. 
Read more here: https://neat-python.readthedocs.io/en/latest/neat_overview.html

Also, NEAT vs NEAT (training) in `src/NEAT/train.py`

## Limitations + Improvements

### Engine

Limitation: once depth reaches ~7 it starts taking annoying lengths of time to 
evaluate positions (depending on hardware).

How to improve:
- Branch pruning is already implemented but to speed it up, evaluate positions in 
order of how good they are expected to be (makes pruning more likely). How to
quickly estimate order?
- Rewrite in a faster language e.g. java.

Limitation: the method to evaluate positions is basic. It just assigns points 
based on how many pieces are in a row for each player. 

How to improve:
- Not really sure. Is centre control good?
- Need to be careful not to slow it down too much. Don't want to remove depth

### NEAT

Problems:
- Mostly just chooses one column!

Possible causes:
- Playing against self can cause problems (like starting player always winning - 
some bad habits don't get punished if both players do it)
- Rewarding for turn reached means surviving is rewarded, not winning
- Should encourage blocking opponent (but not by measuring surviving since 
non-winning moves can do this)

Ideas:
- Give nets random start position so whole game is trained, not just start
- Only perform one move then evaluate how good it was
- Punish for only choosing 1 column
- Reward for blocking 3 in a row
- Test nets by playing against known alg, e.g. Engine. custom ability - start 
test against weak opponent and increase strength slowly

