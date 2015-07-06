import RPi.GPIO as gpio
from RPi.GPIO import OUT
from RPi.GPIO import HIGH
from RPi.GPIO import LOW
from carty_exceptions import BadArgumentError
from carty_exceptions import CartyError
from enum import Enum
import configparser


class Direction(Enum):
    forward = 1
    backward = -1
    no_direction = 0


class Motion:
    def __init__(self, acceleration=HIGH):
        config = configparser.ConfigParser()
        config.read("../carty.ini")
        motion_config = config["MOTION"]

        self.LMOTOR_PWM = int(motion_config["LMOTOR_PWM"])
        self.LMOTOR_CLOCKWISE = int(motion_config["LMOTOR_CLOCKWISE"])
        self.LMOTOR_COUNTER_CLOCKWISE = int(motion_config["LMOTOR_COUNTER_CLOCKWISE"])

        self.RMOTOR_PWM = int(motion_config["RMOTOR_PWM"])
        self.RMOTOR_CLOCKWISE = int(motion_config["RMOTOR_CLOCKWISE"])
        self.RMOTOR_COUNTER_CLOCKWISE = int(motion_config["RMOTOR_COUNTER_CLOCKWISE"])

        gpio.setmode(gpio.BOARD)
        gpio.setup(self.LMOTOR_PWM, OUT)
        gpio.setup(self.LMOTOR_CLOCKWISE, OUT)
        gpio.setup(self.LMOTOR_COUNTER_CLOCKWISE, OUT)
        gpio.setup(self.RMOTOR_PWM, OUT)
        gpio.setup(self.RMOTOR_CLOCKWISE, OUT)
        gpio.setup(self.RMOTOR_COUNTER_CLOCKWISE, OUT)

        self.set_acceleration(acceleration)
        self.direction = Direction.no_direction

    def get_acceleration(self):
        return self.acceleration

    def set_acceleration(self, acceleration):
        # TODO: Implement acceleration with PWM (RPIO.PWM)
        if (acceleration != HIGH) and (acceleration != LOW):
            raise BadArgumentError("Not Implemented!")

        if acceleration < 0 or acceleration > 255:
            raise BadArgumentError("Be careful mate!")

        self.acceleration = acceleration
        gpio.output(self.LMOTOR_PWM, acceleration)
        gpio.output(self.RMOTOR_PWM, acceleration)

    def forward(self):
        gpio.output(self.LMOTOR_CLOCKWISE, HIGH)
        gpio.output(self.RMOTOR_CLOCKWISE, HIGH)
        self.direction = Direction.forward

    def backward(self):
        gpio.output(self.LMOTOR_COUNTER_CLOCKWISE, HIGH)
        gpio.output(self.RMOTOR_COUNTER_CLOCKWISE, HIGH)
        self.direction = Direction.backward

    def stop(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(self.LMOTOR_CLOCKWISE, LOW)
            gpio.output(self.RMOTOR_CLOCKWISE, LOW)
        else:
            gpio.output(self.LMOTOR_COUNTER_CLOCKWISE, LOW)
            gpio.output(self.RMOTOR_COUNTER_CLOCKWISE, LOW)

        self.direction = Direction.no_direction

    def turn_left(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(self.LMOTOR_CLOCKWISE, LOW)
            gpio.output(self.RMOTOR_CLOCKWISE, HIGH)
        else:
            gpio.output(self.LMOTOR_COUNTER_CLOCKWISE, LOW)
            gpio.output(self.RMOTOR_COUNTER_CLOCKWISE, HIGH)

    def turn_right(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(self.RMOTOR_CLOCKWISE, LOW)
            gpio.output(self.LMOTOR_CLOCKWISE, HIGH)
        else:
            gpio.output(self.RMOTOR_COUNTER_CLOCKWISE, LOW)
            gpio.output(self.LMOTOR_COUNTER_CLOCKWISE, HIGH)
