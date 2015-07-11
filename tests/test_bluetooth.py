import unittest
import sys
import types

sys.path.append("../src")
from bluetooth import *

opened = False
closed = False

class BluetoothTest(unittest.TestCase):
    def setUp(self):
        self.bluetooth = Bluetooth(None, None, None, None)

    def test_connect_without_callback(self):
        self.bluetooth.connect()

    def test_connect_with_callback(self):
        def on_open(self):
            print("on open callback called")
            global opened
            opened = True

        self.bluetooth.on_open = types.MethodType(on_open, self.bluetooth)
        self.bluetooth.connect()
        self.assertEqual(opened, True)

    def test_get_status_not_connected(self):
        self.assertEqual(self.bluetooth.get_status(),
                         ConnectionStatus.disconnected)

    def test_get_status_connected(self):
        self.bluetooth.connect()
        self.assertEqual(self.bluetooth.get_status(),
                         ConnectionStatus.connected)

    def test_connected_not_connected(self):
        self.assertEqual(self.bluetooth.connected(), False)

    def test_connected_connected(self):
        self.bluetooth.connect()
        self.assertEqual(self.bluetooth.connected(), True)

    def test_disconnect_without_callback(self):
        self.bluetooth.disconnect()
        self.assertEqual(self.bluetooth.connected(), False)

    def test_disconnect_with_callback(self):
        def on_close(self):
            print("on close callback called")
            global closed
            closed = True

        self.bluetooth.on_close = types.MethodType(on_close, self.bluetooth)
        self.bluetooth.connect()
        self.bluetooth.disconnect()
        self.assertEqual(closed, True)

    def test_disconnect_status(self):
        self.assertEqual(self.bluetooth.get_status(),
                         ConnectionStatus.disconnected)

        self.bluetooth.connect()
        self.assertEqual(self.bluetooth.get_status(),
                         ConnectionStatus.connected)

        self.bluetooth.disconnect()
        self.assertEqual(self.bluetooth.get_status(),
                         ConnectionStatus.disconnected)

    def test_send_message_not_connected(self):
        sent = self.bluetooth.send("213")
        self.assertEqual(sent, -1)

    def test_send_message_connected(self):
        self.bluetooth.connect()
        sent = self.bluetooth.send("123")
        self.assertEqual(sent, 3)

    def test_recieve_not_connected(self):
        buff = self.bluetooth.recieve(10)
        self.assertEqual(buff, -1)

    def test_recieve_connected_zero(self):
        self.bluetooth.connect()
        buff = self.bluetooth.recieve(0)
        self.assertEqual(buff, "")

    def test_recieve_connected_negative_size(self):
        self.bluetooth.connect()
        buff = self.bluetooth.recieve(-1)
        self.assertEqual(buff, -2)

    def test_recieve_blocking_not_connected(self):
        buff = self.bluetooth.recieve_blocking(1)
        self.assertEqual(buff, -1)

    def test_recieve_blocking_negative_size(self):
        self.bluetooth.connect()
        buff = self.bluetooth.recieve_blocking(-1)
        self.assertEqual(buff, -2)

# serial communication will block forever on read 
#     def test_recieve_blocking_without_callback(self):
#         self.bluetooth.connect()
#         self.bluetooth.recieve_blocking(1)

#     def test_recieve_blocking_with_callback(self):
#         message = ""
#         def on_message(self, msg):
#             print("on message callback called {}".format(msg))
#             global message
#             message = msg
#             self.bluetooth.disconnect()
# 
#         self.bluetooth.on_message = types.MethodType(on_message, self.bluetooth)
#         self.bluetooth.connect()
#         self.bluetooth.send("123")
#         self.bluetooth.recieve_blocking(3)
# 
#         self.assertEqual(message, "123")


if __name__ == "__main__":
    unittest.main()
