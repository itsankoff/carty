import RPi.GPIO as gpio
from RPi.GPIO import OUT
from RPi.GPIO import HIGH
from RPi.GPIO import LOW
from carty_exceptions import BadArgumentError
from carty_exceptions import CartyError
from enum import Enum


LMOTOR_PWM = 26
LMOTOR_CLOCKWISE = 22
LMOTOR_COUNTER_CLOCKWISE = 24

RMOTOR_PWM = 15
RMOTOR_CLOCKWISE = 13
RMOTOR_COUNTER_CLOCKWISE = 11


class Direction(Enum):
    forward = 1
    backward = -1
    no_direction = 0


class Motion:
    def __init__(self, acceleration=HIGH):
        gpio.setmode(gpio.BOARD)
        gpio.setup(LMOTOR_PWM, OUT)
        gpio.setup(LMOTOR_CLOCKWISE, OUT)
        gpio.setup(LMOTOR_COUNTER_CLOCKWISE, OUT)
        gpio.setup(RMOTOR_PWM, OUT)
        gpio.setup(RMOTOR_CLOCKWISE, OUT)
        gpio.setup(RMOTOR_COUNTER_CLOCKWISE, OUT)

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
        gpio.output(LMOTOR_PWM, acceleration)
        gpio.output(RMOTOR_PWM, acceleration)

    def forward(self):
        gpio.output(LMOTOR_CLOCKWISE, HIGH)
        gpio.output(RMOTOR_CLOCKWISE, HIGH)
        self.direction = Direction.forward

    def backward(self):
        gpio.output(LMOTOR_COUNTER_CLOCKWISE, HIGH)
        gpio.output(RMOTOR_COUNTER_CLOCKWISE, HIGH)
        self.direction = Direction.backward

    def stop(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(LMOTOR_CLOCKWISE, LOW)
            gpio.output(RMOTOR_CLOCKWISE, LOW)
        else:
            gpio.output(LMOTOR_COUNTER_CLOCKWISE, LOW)
            gpio.output(RMOTOR_COUNTER_CLOCKWISE, LOW)

        self.direction = Direction.no_direction

    def turn_left(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(LMOTOR_CLOCKWISE, LOW)
            gpio.output(RMOTOR_CLOCKWISE, HIGH)
        else:
            gpio.output(LMOTOR_COUNTER_CLOCKWISE, LOW)
            gpio.output(RMOTOR_COUNTER_CLOCKWISE, HIGH)

    def turn_right(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(RMOTOR_CLOCKWISE, LOW)
            gpio.output(LMOTOR_CLOCKWISE, HIGH)
        else:
            gpio.output(RMOTOR_COUNTER_CLOCKWISE, LOW)
            gpio.output(LMOTOR_COUNTER_CLOCKWISE, HIGH)
