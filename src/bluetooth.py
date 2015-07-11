import serial
from enum import Enum


class ConnectionStatus(Enum):
    disconnected = 0
    connected = 1


class Bluetooth:
    def __init__(self, on_open, on_message, on_close, on_error):
        self.buff = ""
        self.status = ConnectionStatus.disconnected
        self.on_open = on_open
        self.on_message = on_message
        self.on_close = on_close
        self.on_error = on_error

    def connect(self, remote_device="/dev/ttyAMA0"):
        self.device = remote_device
        self.serial = serial.Serial(self.device, 9600, timeout=0)
        self.status = ConnectionStatus.connected
        if self.on_open:
            self.on_open()

    def get_status(self):
        return self.status

    def disconnect(self):
        if self.on_close:
            self.on_close()

        self.serial = None
        self.status = ConnectionStatus.disconnected

    def send(self, message):
        self.serial.write(message)

    def recieve(self, size):
        return self.serial.read(size).decode(encoding="UTF-8")

    # message_size - wait for message_size buffer
    # and then call on_message callback
    def recieve_blocking(self, message_size):
        while self.status == ConnectionStatus.connected:
            self.buff = self.recieve(message_size)
            if len(self.buff) == message_size:
                self.on_message(self.buff)
