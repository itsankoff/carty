# carty

# carty is python project for rc controlled car.
It is actually a firmware for raspberry pi car
which uses bluetooth for communication between remote controller and the car.

Version 1.0:
  1. light controller for controlling lights of the car.
  2. move controller for controlling movement of the car.
  3. extension manager for adding sensors.
  4. different modes:
    * real time mode - the car is controlled by remote controller in real time
    * programmable mode - the user predifines set of instruction and send it to the car.
  5. bluetooth communication - remote controller will communicate with the
        firmware through bluetooth module. It can be replaced with wifi communication.


Installation guide:

1. Clone this repo to your raspberry

2. Bluetooth module installation (Raspbian).
   This step will remove bluetooth console option to free the bluetooth for carty
  1. Backup /boot/cmdline.txt - sudo cp /boot/cmdline.txt /boot/cmdline.txt.backup
  2. Go and edit file /boot/cmdline.txt - remove "console=ttyAMA0, 115200 kgboc=ttyAMA0, 115200"
  3. Backup /etc/inittab - sudo cp /etc/inittab /etc/inittab.backup
  4. Go and edit file /etc/inittab -
     comment the line below the line "#Spawn a getty on Raspberry Pi serial line"
  5. Reboot the Raspberry Pi

3. Controller
  1. Download Arduino Bluetooth RC Car (Android) (you can use other software
        for communication but, it will require code modifications)
  2. Start the android application and go to gear and connect to raspberry pi
     (if you have problems see Throubleshoot section)


Troubleshooting: (Raspbian) Bluetooth connection problems.
  1. If you have problem with bluetooth comminucation, install minicom tool (sudo apt-get install minicom).
  2. Try to connect with other bluetooth device to Raspberry Pi.
  3. Start minicom -b 9600 -o -D /dev/ttyAMA0 and send some messages between devices.
  4. If you CAN'T recieve messages between 2 sides check jumpers of serial bluetooth.

Bluetooth | Raspberry 
--------- | -----------------
VCC       | 5V power supply
GND       | Ground (0)
TDX       | RXD
RDX       | TDX

  1.5 [For more information see here](http://blog.miguelgrinberg.com/post/a-cheap-bluetooth-serial-port-for-your-raspberry-pi)


