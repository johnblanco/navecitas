from kaggle_environments.helpers import Direction, Point


def horizontal_flight_plan(origin: Point, target: Point):
    plan = ""
    diff_x = origin.x - target.x

    if 0 < diff_x < 10:
        initial_direction = Direction.WEST
    else:
        initial_direction = Direction.EAST

    if diff_x > 9:
        diff_x = 21 - diff_x

    plan += initial_direction.to_char()
    if diff_x != 0:
        plan += "{}".format(abs(diff_x) - 1)
    plan += initial_direction.opposite().to_char()

    return plan


def vertical_flight_plan(origin: Point, target: Point):
    plan = ""
    diff_y = origin.y - target.y

    if 0 < diff_y < 10:
        initial_direction = Direction.NORTH
    else:
        initial_direction = Direction.SOUTH

    if diff_y > 9:
        diff_y = 21 - diff_y

    plan += initial_direction.to_char()
    if diff_y != 0:
        plan += "{}".format(abs(diff_y) - 1)
    plan += initial_direction.opposite().to_char()

    return plan


def flight_plan_to_target(origin: Point, target: Point):
    plan = ""
    diff_y = origin.y - target.y
    diff_x = origin.x - target.x

    if diff_y == 0:
        return horizontal_flight_plan(origin, target)

    if diff_x == 0:
        return vertical_flight_plan(origin, target)

    if 0 < diff_y < 10:
        initial_direction = Direction.NORTH
    else:
        initial_direction = Direction.SOUTH

    if 0 < diff_x < 10:
        turn_direction = Direction.WEST
    else:
        turn_direction = Direction.EAST

    if diff_x > 9:
        diff_x = 21 - diff_x

    if diff_y > 9:
        diff_y = 21 - diff_y

    plan += initial_direction.to_char()
    if diff_y != 0:
        plan += "{}".format(abs(diff_y) - 1)
    plan += turn_direction.to_char()
    if diff_x != 0:
        plan += "{}".format(abs(diff_x) - 1)
    plan += initial_direction.opposite().to_char()
    if diff_y != 0:
        plan += "{}".format(abs(diff_y) - 1)
    plan += turn_direction.opposite().to_char()

    return plan
