import serial
import sys


# supported commands for HC-06 bluetooth serial module
commands = {"AT": "check connectivity",
            "AT+NAME": "set name of device (no space between cmd and name",
            "AT+BAUD": "set baudrate of device (e.g 9600) (no space again)",
            "AT+PIN": "set pin code of device (no space again",
            "AT+VERSION": "get version"}


def print_help():
    commands["exit"] = "exit"
    commands["help"] = "show this section"

    for command, description in commands.items():
        print("{} - {}".format(command, description))


def main(dev):
    s = serial.Serial(dev, 9600, timeout=1)
    print("connected to: " + s.portstr)
    print("insert commands:")

    while True:
        command = input(">>")
        if command == "exit":
            break

        if command == "help":
            print_help()
            continue

        # commands to bluetooth
        s.write(command.encode("ascii"))

        buff = s.read(50).decode(encoding='UTF-8')
        if buff:
            print(buff)

    s.close()


if __name__ == "__main__":
    device = "/dev/ttyAMA0"

    if(len(sys.argv) >= 2):
        device = sys.argv[1]

    main(device)
