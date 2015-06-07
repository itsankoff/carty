from bluetooth_controller import BluetoothController
from collections import defaultdict

class RemoteController:
    def __init__(self):
        self.channel = BluetoothController("toothy")
        self.handlers = defaultdict(list)  # dictionary with default values [] of handlers
        self.connected = False

    def register_handler(event, handler):
        self.handlers[event].append(hanlder)

    def deregister_handler(event, handler):
        handlers = self.handlers[event]
        handlers.remove(handler)

    def on_open(self):
        self.connected = True

    def dispatch(self, message):
        handlers = self.handlers[message] 
        for handler in handlers:
            handler.handle(message)

    def on_close(self):
        self.connected = False

    def on_error(self):
        self.connected = False

