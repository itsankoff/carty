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
