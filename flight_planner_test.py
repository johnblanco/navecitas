import unittest

from kaggle_environments.helpers import Point

from flight_planner import flight_plan_to_target


class FlightPlanTest(unittest.TestCase):

    def test_flight_plan_to_kore_1(self):
        kore_position = Point(4, 1)
        shipyard_position = Point(10, 10)
        res = flight_plan_to_target(shipyard_position, kore_position)

        self.assertEqual('N8W5S8E', res)

    def test_flight_plan_to_kore_2(self):
        kore_position = Point(13, 13)
        shipyard_position = Point(10, 10)
        res = flight_plan_to_target(shipyard_position, kore_position)

        self.assertEqual('S2E2N2W', res)

    def test_flight_plan_to_kore_3(self):
        kore_position = Point(0, 3)
        shipyard_position = Point(19, 1)
        res = flight_plan_to_target(shipyard_position, kore_position)

        self.assertEqual('S1E1N1W', res)

    def test_flight_plan_to_kore_4(self):
        shipyard_position = Point(11, 3)
        kore_position = Point(8, 3)
        res = flight_plan_to_target(shipyard_position, kore_position)

        self.assertEqual('W2E', res)

    def test_flight_plan_to_kore_5(self):
        shipyard_position = Point(0, 11)
        kore_position = Point(0, 8)
        res = flight_plan_to_target(shipyard_position, kore_position)

        self.assertEqual('N2S', res)
