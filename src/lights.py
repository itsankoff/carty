import configparser
import RPi.GPIO as gpio


class Lights:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("carty.ini")
        lights_config = config["LIGHTS"]

        self.FRONT_LIGHTS = lights_config["FRONT_LIGHTS"]
        self.BACK_LIGHTS = lights_config["BACK_LIGHTS"]

        gpio.setup(self.FRONT_LIGHTS, OUT)
        gpio.setup(self.BACK_LIGHTS, OUT)

        self.disable_front_lights()
        self.disable_back_light()

    def enable_front_lights(self):
        gpio.output(self.FRONT_LIGHTS, gpio.HIGH)

    def disable_front_lights(self):
        gpio.output(self.FRONT_LIGHTS, gpio.LOW)

    def enable_back_lights(self):
        gpio.output(self.BACK_LIGHTS, gpio.HIGH)

    def disable_back_lights(self):
        gpio.output(self.BACK_LIGHTS, gpio.LOW)
