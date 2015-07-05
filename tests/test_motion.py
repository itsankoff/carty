import unittest
from time import sleep
from ..src.motion import *


class MotionTest(unittest.TestCase):
    def setUp(self):
        self.move = Motion()

    def tearDown(self):
        self.move.stop()

    def test_forward_movement(self):
        self.move.forward()
        sleep(2)

    def test_backward_movement(self):
        self.move.backward()
        sleep(2)

    def test_turn_left_forward(self):
        self.move.forward()
        self.move.turn_left()
        sleep(1)

    def test_turn_left_backward(self):
        self.move.backward()
        self.move.turn_left()
        sleep(1)

    def test_turn_right_forward(self):
        self.move.forward()
        self.move.turn_right()
        sleep(1)

    def test_turn_right_backward(self):
        self.move.forward()
        self.move.turn_right()
        sleep(1)

    def test_set_acceleration_high(self):
        print("Tes acceleration high")
        self.move.set_acceleration(HIGH)
        self.move.forward()

    def test_set_acceleration_low(self):
        print("Test acceleration low")
        self.move.set_acceleration(LOW)
        self.move.forward()
        sleep(2)

    def test_get_acceleration(self):
        self.move.set_acceleration(HIGH)
        self.assertEqual(self.move.get_acceleration, HIGH)


if __name__ == "__main__":
    unittest.main()
