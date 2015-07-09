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
        motion_config = config.items("MOTION")

        self.pins = dict(motion_config);

        self.init_hardware()

        for name, pin in self.pins.items():
            gpio.output(int(pin), LOW)        

        self.set_acceleration(acceleration)
        self.direction = Direction.no_direction

    def init_hardware(self):
        gpio.setmode(gpio.BOARD)

        for name, pin in self.pins.items():
            gpio.setup(int(pin), OUT)
    

    def get_acceleration(self):
        return self.acceleration

    def set_acceleration(self, acceleration):
        # TODO: Implement acceleration with PWM (RPIO.PWM)
        if (acceleration != HIGH) and (acceleration != LOW):
            raise BadArgumentError("Not Implemented!")

        if acceleration < 0 or acceleration > 255:
            raise BadArgumentError("Be careful mate!")

        self.acceleration = acceleration
        gpio.output(self.get_channel('lmotor_pwm'), acceleration)
        gpio.output(self.get_channel('rmotor_pwm'), acceleration)

    def get_channel(self, name):
        return int(self.pins[name])

    def forward(self):
        gpio.output(self.get_channel("lmotor_clockwise"), HIGH)
        gpio.output(self.get_channel("rmotor_clockwise"), HIGH)
        self.direction = Direction.forward

    def backward(self):
        gpio.output(self.get_channel("lmotor_counter_clockwise"), HIGH)
        gpio.output(self.get_channel("rmotor_counter_clockwise"), HIGH)
        self.direction = Direction.backward

    def stop(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(self.get_channel("lmotor_clockwise"), LOW)
            gpio.output(self.get_channel("rmotor_clockwise"), LOW)
        else:
            gpio.output(self.get_channel("lmotor_counter_clockwise"), LOW)
            gpio.output(self.get_channel("rmotor_counter_clockwise"), LOW)

        self.direction = Direction.no_direction

    def turn_left(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(self.get_channel("lmotor_clockwise"), LOW)
            gpio.output(self.get_channel("rmotor_clockwise"), HIGH)
        else:
            gpio.output(self.get_channel("lmotor_counter_clockwise"), LOW)
            gpio.output(self.get_channel("rmotor_counter_clockwise"), HIGH)

    def turn_right(self):
        if self.direction == Direction.no_direction:
            return

        if self.direction == Direction.forward:
            gpio.output(self.get_channel("rmotor_clockwise"), LOW)
            gpio.output(self.get_channel("lmotor_clockwise"), HIGH)
        else:
            gpio.output(self.get_channel("rmotor_counter_clockwise"), LOW)
            gpio.output(self.get_channel("lmotor_counter_clockwise"), HIGH)
