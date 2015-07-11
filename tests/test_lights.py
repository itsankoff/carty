import unittest
from time import sleep

import sys
sys.path.append("../src")
from lights import *


class LightsTest(unittest.TestCase):
    def test_enable_front_lights(self):
        print("test enable lights")
        lights = Lights()
        lights.enable_front_lights()
        sleep(2)

    def test_disable_front_lights(self):
        print("test disable lights")
        lights = Lights()
        sleep(2)
        lights.disable_front_lights()
        print("lights disabled")
        sleep(1)

    def test_enable_back_lights(self):
        print("test enable back lights")
        lights = Lights()
        lights.enable_back_lights()
        print("back lights enabled")
        sleep(2)

    def test_disable_back_lights(self):
        print("test_disable back lights")
        lights = Lights()
        lights.enable_back_lights()
        sleep(2)
        lights.disable_back_lights()
        print("back lights disabled")
        sleep(1)
