import unittest

import sys
sys.path.append("../src")
from remote_controller import *


class TestRemoteController(unittest.TestCase):
    class StuntMotion():
        def __init__(self):
            self.reset()

        def forward(self):
            self.fward = True

        def backward(self):
            self.bward = True

        def turn_right(self):
            self.right = True

        def turn_left(self):
            self.left = True

        def stop(self):
            self.stop_ = True

        def reset(self):
            self.fward = False
            self.bward = False
            self.right = False
            self.left = False
            self.stop_ = False

    class StuntLights():
        def __init__(self):
            self.reset()

        def enable_front_lights(self):
            self.front_lights = True

        def disable_front_lights(self):
            self.front_lights = False

        def enable_back_lights(self):
            self.back_lights = True

        def disable_back_lights(self):
            self.back_lights = False

        def reset(self):
            self.front_lights = False
            self.back_lighst = False

    def test_command_realtime(self):
        rc = RemoteController()
        rc.motion = self.StuntMotion()
        rc.lights = self.StuntLights()

        rc.command_realtime("F")
        self.assertEqual(rc.motion.fward, True)
        rc.motion.reset()

        rc.command_realtime("B")
        self.assertEqual(rc.motion.bward, True)
        rc.motion.reset()

        rc.command_realtime("L")
        self.assertEqual(rc.motion.left, True)
        rc.motion.reset()

        rc.command_realtime("R")
        self.assertEqual(rc.motion.right, True)
        rc.motion.reset()

        rc.command_realtime("G")
        self.assertEqual(rc.motion.fward, True)
        self.assertEqual(rc.motion.left, True)
        rc.motion.reset()

        rc.command_realtime("I")
        self.assertEqual(rc.motion.fward, True)
        self.assertEqual(rc.motion.right, True)
        rc.motion.reset()

        rc.command_realtime("H")
        self.assertEqual(rc.motion.bward, True)
        self.assertEqual(rc.motion.left, True)
        rc.motion.reset()

        rc.command_realtime("J")
        self.assertEqual(rc.motion.bward, True)
        self.assertEqual(rc.motion.right, True)
        rc.motion.reset()

        rc.command_realtime("S")
        self.assertEqual(rc.motion.stop_, True)
        rc.motion.reset()

        rc.command_realtime("W")
        self.assertEqual(rc.lights.front_lights, True)
        rc.lights.reset()

        rc.lights.front_lights = True
        rc.command_realtime("w")
        self.assertEqual(rc.lights.front_lights, False)
        rc.lights.reset()

        rc.command_realtime("U")
        self.assertEqual(rc.lights.back_lights, True)
        rc.lights.reset()

        rc.lights.back_lights = True
        rc.command_realtime("u")
        self.assertEqual(rc.lights.back_lights, False)
        rc.lights.reset()

    def test_predefined(self):
        rc = RemoteController()
        rc.motion = self.StuntMotion()
        rc.lights = self.StuntLights()

        rc.on_message("V")
        rc.on_message("F")
        rc.on_message("S")
        rc.on_message("B")
        rc.on_message("S")
        rc.on_message("v")

        self.assertEqual(rc.motion.fward, True)
        self.assertEqual(rc.motion.stop_, True)
        self.assertEqual(rc.motion.bward, True)

    def test_predefined_lights(self):
        rc = RemoteController()
        rc.motion = self.StuntMotion()
        rc.lights = self.StuntLights()

        rc.on_message("V")
        rc.on_message("W")
        rc.on_message("U")
        rc.on_message("v")

        self.assertEqual(rc.lights.front_lights, True)
        self.assertEqual(rc.lights.back_lights, True)


if __name__ == "__main__":
    unittest.main()
