# carty
Firmware for rc controlled raspberry-pi car.

* [Introduction](#intro)
* [Install](#install)
* [Troubleshooting](#troubleshooting)
* [License](#license)
* [References](#references)

---

<a name="intro">

## Introduction

### Version 1
  1. light controller for controlling lights of the car.
  2. move controller for controlling movement of the car.
  3. extension manager for adding sensors.
  4. different modes:
    * real time mode - the car is controlled by remote controller in real time
    * programmable mode - the user predefines set of instruction and send it to the car.
  5. bluetooth communication - remote controller will communicate with the
        firmware through bluetooth module. It can be replaced with wifi communication.

<a name="install">

## Install
1. Clone this repo to your raspberry

2. Bluetooth module installation (Raspbian). This step will remove bluetooth console option
    to free the bluetooth for the carty controller.
    * Backup /boot/cmdline.txt - `sudo cp /boot/cmdline.txt /boot/cmdline.txt.backup`
    * Go and edit file /boot/cmdline.txt - `remove "console=ttyAMA0, 115200 kgboc=ttyAMA0, 115200"`
    * Backup /etc/inittab - `sudo cp /etc/inittab /etc/inittab.backup`
    * Go and edit file /etc/inittab -
        comment the line below the line "#Spawn a getty on Raspberry Pi serial line"
    * Reboot the Raspberry Pi

3. Controller
    * Download Arduino Bluetooth RC Car (Android). You can use other software for communication but most probably,
        it will require code modifications)
    * Start the android application and go to gear button t connect to raspberry-pi.
        If you have any problems see [troubleshoot section](#troubleshooting))

4. Motors
    * You will need breadboard and motor driver (In this project I use L293DNE search in google)
    * Cable the motor driver as described below: (start from left up to down of motor driver if you
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

5. Install raspberry-pi `gpio` lib
    * `sudo pip install rpi.gpio`

6. You need pyserial for python3
    * `git clone -b python3 https://github.com/makerbot/pyserial.git`
    * `cd pyserial`
    * `python3.4 setup.py install`

7. Install boot script
    * `edit /etc/rc.local`
    * `/path/to/carty/run.sh`
    * `reboot`

8. PWM lib for raspberry PI
    * `git clone https://github.com/metachris/RPIO.git)`
    * `cd RPIO`
    * `sudo python3.4 setup.py install`

<a name="troubleshooting">

## Troubleshooting

### (Raspbian) Bluetooth connection problems.
If you have problem with bluetooth communication:
1. Install minicom tool `sudo apt-get install minicom`
2. Try to connect with another bluetooth device to Raspberry Pi.
3. `minicom -b 9600 -o -D /dev/ttyAMA0`
4. Try to send some messages between the raspberry-pi and the other device.
5. If you __can't__ rx/tx messages from/to one of the sides check the jumpers on the serial bluetooth.

Bluetooth | Raspberry 
--------- | -----------------
VCC       | 5V power supply
GND       | Ground (0)
TDX       | RXD
RDX       | TDX

<a name="license">

## License

[GPL](https://github.com/itsankoff/carty/blob/master/LICENSE)

<a name="references">

## References:

[For more information see here](http://blog.miguelgrinberg.com/post/a-cheap-bluetooth-serial-port-for-your-raspberry-pi)
