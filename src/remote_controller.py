import bluetooth
import RPi.GPIO as gpio
import configparser
import motion
import lights

from enum import Enum
from time import sleep
from datetime import datetime


class Mode(Enum):
    predefined = 0
    realtime = 1


class RemoteController:
    def __init__(self):
        # indication led
        config = configparser.ConfigParser()
        config.read("../carty.ini")
        self.indication_led = int(config["MAIN"]["INDICATION_LED"])
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.indication_led, gpio.OUT)
        gpio.output(self.indication_led, gpio.LOW)

        # hardware modules
        self.motion = motion.Motion()
        self.lights = lights.Lights()

        # mode
        self.mode = Mode.realtime
        self.cached_commands = []
        self.command_time = 0
        self.prev_command = ""

    def on_open(self):
        gpio.output(self.indication_led, gpio.HIGH)

    def on_message(self, message):
        print("on_message {}".format(message))

        if message == "V":
            self.mode = Mode.predefined
            return
        elif message == "v":
            # end of predefined mode
            # update last command time and exceute all buffered
            # commands
            time_interval = datetime.now() - self.command_time
            time_interval = int(time_interval.seconds + time_interval.microseconds / 1000000)
            self.cached_commands.append((self.prev_command, time_interval))

            self.mode = Mode.realtime
            for command, time in self.cached_commands:
                self.command_realtime(command)
                print("sleep {}".format(time))
                sleep(time)

            # reset
            self.cached_commands.clear()
            self.command_time = 0
            self.prev_command = 0
            return
        else:
            if self.mode == Mode.realtime:
                self.command_realtime(message)
            else:
                if self.command_time == 0:
                    self.command_time = datetime.now()
                    self.prev_command = message
                else:
                    now = datetime.now()
                    time_interval = now - self.command_time
                    time_interval = int(time_interval.seconds + time_interval.microseconds / 1000000)
                    self.cached_commands.append((self.prev_command, time_interval))
                    self.prev_command = message
                    self.command_time = now

    def on_close(self):
        gpio.output(self.indication_led, gpio.LOW)

    def on_error(self, err):
        print("ERROR {}".format(err))
        gpio.output(self.indication_lef, gpio.LOW)

    def command_realtime(self, command):
        print("execute {}".format(command))
        if command == "F":
            self.motion.forward()
        elif command == "B":
            self.motion.backward()
        elif command == "L":
            self.motion.turn_left()
        elif command == "R":
            self.motion.turn_right()
        elif command == "G":
            self.motion.forward()
            self.motion.turn_left()
        elif command == "I":
            self.motion.forward()
            self.motion.turn_right()
        elif command == "H":
            self.motion.backward()
            self.motion.turn_left()
        elif command == "J":
            self.motion.backward()
            self.motion.turn_right()
        elif command == "S":
            self.motion.stop()
        elif command == "W":
            self.lights.enable_front_lights()
        elif command == "w":
            self.lights.disable_front_lights()
        elif command == "U":
            self.lights.enable_back_lights()
        elif command == "u":
            self.lights.disable_back_lights()
        else:
            print("unsupported command {}".format(command))
