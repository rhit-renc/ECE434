## Make
#### make
This portion is just an intro to makefile. To compile, run the following command to clean and compile:

make clean; make

## Installing the kernel source

uname -a returns the following:

Linux BeagleBone 5.10.168-ti-r75 #1xross SMP PREEMPT Sun Jan 14 18:03:22 EST 2024 armv7l GNU/Linux

## Kernel Modules
#### ebbchar
To run the script, the ebbchar module must first be inserted. From hw05/ebbchar, run the following command:

sudo insmod ebbchar.ko

To run the test script, run the following command:

sudo ./test

This script prompts the user to send a message to the kernel module and outputs verification that the message has been received

#### gpio_test
For this portion, I combined the 2 requirements and added 2 buttons that can both trigger on rising and falling edges.

Usage:
1. Connect button 1 to P8_15, button 2 to P8_18, LED 1 to P9_12, and LED 2 to P9_14
2. To view the kernel log, run the command: dmesg --follow
3. From hw05/gpio_test, run the command: sudo insmod gpio_test.ko 
4. When satisfied from pressing buttons, run the command: sudo rmmod gpio_test

## ADXL345 Accelerometer/Etch-A-Sketch

LED matrix is at i2c address 0x70

Accelerometer is at 2c address 0x53

To wire the i2c, connect SDA to P9_20 and SCL P9_19 to

To use the accelerometer to control the Etch-A-Sketch, run the following commands:
1. cd /sys/class/i2c-adapter/i2c-2
2. sudo echo adxl345 0x1d > new_device
3. sudo chown debian:debian *
Now the accelerometer data can be read from /sys/class/i2c-adapter/i2c-2/2-001d/iio:device0/in_accel_N_raw, where N is x, y, or z

To use the accelerometer with EtchASketch, run hw05/EtchASketch.py. The controls are as the following:

Tilt in the positive x axis: move right

Tilt in the negative x axis: move left

Tilt in the positive y axis: move up

Tilt in the negative y axis: move down

Tilt controls have a threshold of 40 degrees from the initial accelerometer readings from the start of the program

## led
Usage:
1. Connect button 1 to P8_15, button 2 to P8_18, LED 1 to P9_12, and LED 2 to P9_14
2. To view the kernel log, run the command: dmesg --follow
3. From hw05/led, run the command: sudo insmod led.ko
4. When satisfied from pressing buttons, run the command: sudo rmmod led.ko

# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  0/0 | Project 
|  2/2 | Makefile
|  6/6 | Kernel Source
|  6/6 | Kernel Modules: hello, ebbchar, gpio_test, led
|  4/4 | Etch-a-Sketch
|  2/2 | Blink at different rates
| 20/20 | **Total**

*My comments are in italics. --may*

