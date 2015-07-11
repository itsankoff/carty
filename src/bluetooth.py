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

    def disconnect(self):
        if self.on_close:
            self.on_close()

        self.serial = None
        self.status = ConnectionStatus.disconnected

    def get_status(self):
        return self.status

    def connected(self):
        return self.status == ConnectionStatus.connected

    def send(self, message):
        if self.status != ConnectionStatus.connected:
            return -1

        return self.serial.write(message.encode(encoding="ascii"))

    def recieve(self, size):
        if self.status != ConnectionStatus.connected:
            return -1

        if size < 0:
            return -2

        if size == 0:
            return ""

        return self.serial.read(size).decode(encoding="UTF-8")

    # message_size - wait for message_size buffer
    # and then call on_message callback
    def recieve_blocking(self, size):
        if self.status != ConnectionStatus.connected:
            return -1

        if size < 0:
            return -2

        if size == 0:
            return ""

        while self.status == ConnectionStatus.connected:
            self.buff = self.recieve(size)
            if len(self.buff) == size:
                if self.on_message:
                    self.on_message(self.buff)
