# carty
Firmware for rc controlled car.

It is actually a firmware for raspberry pi car
which uses bluetooth for communication between remote controller and the car.

* [Intro](#intro)
* [Install](#install)
* [Troubleshooting](#troubleshooting)
* [License](#license)

<a name="intro">
## Intro
### Version 1
  1. light controller for controlling lights of the car.
  2. move controller for controlling movement of the car.
  3. extension manager for adding sensors.
  4. different modes:
    * real time mode - the car is controlled by remote controller in real time
    * programmable mode - the user predifines set of instruction and send it to the car.
  5. bluetooth communication - remote controller will communicate with the
        firmware through bluetooth module. It can be replaced with wifi communication.

<a name="install">
## Install
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
     (if you have problems see [troubleshoot section](#troubleshooting))

4. Motors
  1. You will need breadboard and motor driver (In this project I use L293DNE search in google)
  2. Cable the motor driver as described below: (start from left up to down of motor driver if you
        watch it with hole on top)

        Motor driver    |Raspberry 
        :--------------:|:-----------------:
        Left     Right  |Left      Right
        PWM      VCC    |pin 26    pin 2
        LEFT     RIGHT  |pin 24    pin 11
        MOTOR    MOTOR  |       
        GND      GND    |pin 25    pin 25
        GND      GND    |pin 25    pin 25
        MOTOR    MOTOR  |       
        RIGHT    LEFT   |pin 22    pin 13
        VCC      PWM    |pin 2     pin 15

5. sudo pip install rpi.gpio

6. You need pyserial for python3
  1. git clone -b python3 https://github.com/makerbot/pyserial.git
  2. cd pyserial
  3. python3.4 setup.py install

7. Install boot script
  1. edit /etc/rc.local
  2. /path/to/carty/run.sh
  3. reboot

8. PWM lib for raspberry PI
  1. clone RPIO repo (git clone https://github.com/metachris/RPIO.git)
  2. cd RPIO
  3. sudo python3.4 setup.py install

<a name="troubleshooting">
## Troubleshooting
### (Raspbian) Bluetooth connection problems.
If you have problem with bluetooth comminucation:
1. install minicom tool (sudo apt-get install minicom).
2. Try to connect with other bluetooth device to Raspberry Pi.
3. Start minicom -b 9600 -o -D /dev/ttyAMA0 and send some messages between devices.
4. If you CAN'T recieve messages between 2 sides check jumpers of serial bluetooth.

Bluetooth | Raspberry 
--------- | -----------------
VCC       | 5V power supply
GND       | Ground (0)
TDX       | RXD
RDX       | TDX

<a name="license">
## License
[GPL](https://github.com/itsankoff/carty/blob/master/LICENSE)

## References:
[For more information see here](http://blog.miguelgrinberg.com/post/a-cheap-bluetooth-serial-port-for-your-raspberry-pi)
