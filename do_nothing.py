from kaggle_environments.envs.kore_fleets.helpers import *

from src.basic import max_ships_to_spawn


def agent(obs, config):
    board = Board(obs, config)
    me = board.current_player

    for s in me.shipyards:
        print(s.position)


    return me.next_actions
