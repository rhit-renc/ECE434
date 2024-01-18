## Make
#### make
This portion is just an intro to makefile. To compile, run the following command to clean and compile:

make clean; make

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
