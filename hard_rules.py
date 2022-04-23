from kaggle_environments.envs.kore_fleets.helpers import *
from random import randint

from flight_planner import flight_plan_to_target


def max_ships_to_spawn(turns_controlled: int) -> int:
    for idx, target in enumerate(SPAWN_VALUES):
        if turns_controlled < target:
            return idx + 1
    return len(SPAWN_VALUES) + 1


def max_kore_position(cells) -> Point:
    max_kore = 0
    res = None
    for c in cells:
        if c.kore > max_kore:
            max_kore = c.kore
            res = c.position


    return res


def agent(obs, config):
    board = Board(obs, config)
    me = board.current_player

    turn = board.step

    spawn_cost = board.configuration.spawn_cost
    kore_left = me.kore

    ship_amount = 0
    for fleet in me.fleets:
        ship_amount += fleet.ship_count

    target_position = max_kore_position(board.cells.values())
    print("turn: {} max_kore_pos: {}".format(turn, target_position))
    ships_available_to_spawn = max_ships_to_spawn(turn)

    for shipyard in me.shipyards:
        action = None

        if shipyard.ship_count >= 21 and target_position is not None:
            flight_plan = flight_plan_to_target(shipyard.position, target_position)
            action = ShipyardAction.launch_fleet_with_flight_plan(21, flight_plan)
        elif kore_left >= spawn_cost * ships_available_to_spawn and ship_amount <= 100:
            action = ShipyardAction.spawn_ships(ships_available_to_spawn)

        shipyard.next_action = action

    return me.next_actions
