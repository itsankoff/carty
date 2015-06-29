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
  5. bluetooth communication - remote controller will communicate with the firmware through bluetooth module. It can be replaced with wifi communication.


Installation guide:
  1. clone this repo to your raspberry

  2. Bluetooth module installation (Raspbian)
    This step will remove bluetooth console option to free the bluetooth for carty
    2.1 Backup /boot/cmdline.txt - sudo cp /boot/cmdline.txt /boot/cmdline.txt.backup
    2.2 Go and edit file /boot/cmdline.txt - remove "console=ttyAMA0, 115200 kgboc=ttyAMA0, 115200"
    2.4 Backup /etc/inittab - sudo cp /etc/inittab /etc/inittab.backup
    2.3 Go and edit file /etc/inittab - comment the line below the line "#Spawn a getty on Raspberry Pi serial line"
    2.4 Reboot the Raspberry Pi


Troubleshooting: (Raspbian)
  1. Bluetooth connection problems.
    1.1. If you have problem with bluetooth comminucation, install minicom tool (sudo apt-get install minicom).
    1.2. Try to connect with other bluetooth device to Raspberry Pi.
    1.3. Start minicom -b 9600 -o -D /dev/ttyAMA0 and send some messages between devices.
    1.4. If you CAN'T recieve messages between 2 sides check jumpers of serial bluetooth.
        ----------------------------------
        | bluetooth    | Raspberry       |
        ----------------------------------
        |   VCC        | 5V power supply |
        |   GND        | Ground (0)      |
        |   TDX        | RXD             |
        |   RDX        |      TDX        |
        ----------------------------------

