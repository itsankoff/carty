import configparser
import RPi.GPIO as gpio


class Lights:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../carty.ini")
        lights_config = config["LIGHTS"]

        self.FRONT_LIGHTS = int(lights_config["FRONT_LIGHTS"])
        self.BACK_LIGHTS = int(lights_config["BACK_LIGHTS"])

        gpio.setmode(gpio.BOARD)
        gpio.setup(self.FRONT_LIGHTS, gpio.OUT)
        gpio.setup(self.BACK_LIGHTS, gpio.OUT)

        # In Europe front lights are obligatory
        self.enable_front_lights()
        self.disable_back_lights()

    def enable_front_lights(self):
        gpio.output(self.FRONT_LIGHTS, gpio.HIGH)

    def disable_front_lights(self):
        gpio.output(self.FRONT_LIGHTS, gpio.LOW)

    def enable_back_lights(self):
        gpio.output(self.BACK_LIGHTS, gpio.HIGH)

    def disable_back_lights(self):
        gpio.output(self.BACK_LIGHTS, gpio.LOW)
