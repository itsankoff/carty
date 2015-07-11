from serial import Serial
ser = Serial('/dev/ttyAMA0', 9600, timeout=0)
print("connected to: " + ser.portstr)
 
while True:
    # Read a line and convert it from b'xxx\r\n' to xxx
    letter = ser.read().decode('utf-8')
    if letter:  # If it isn't a blank line
        print(letter)

ser.close()

