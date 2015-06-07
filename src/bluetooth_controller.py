class BluetoothController:
    def __init__(self, name, on_open, on_message, on_close, on_error):
        self.name = name
        self.buff = ""
        self.on_open = on_open
        self.on_message = on_message
        self.on_close = on_close
        self.on_error = on_error
    
    def discover(self, timeout):
        pass

    def connect(self, remote_device):
        pass

    def disconnect(self):
        pass

    def send(self, message):
        # send the message as byte string
        pass

    def recieve(self, num_of_bytes):
        # return message
        pass
