import remote_controller
import bluetooth


class Carty:
    """ this is the main module of the application """
    def __init__(self):
        self.controller = remote_controller.RemoteController()
        self.bluetooth = bluetooth.Bluetooth(self.controller.on_open,
                                             self.controller.on_message,
                                             self.controller.on_close,
                                             self.controller.on_error)

    def start(self):
        self.bluetooth.connect()
        self.bluetooth.recieve_blocking(1)


if __name__ == "__main__":
    carty = Carty()
    carty.start()
