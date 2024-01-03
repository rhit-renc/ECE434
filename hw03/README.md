# TMP101
Usage: python temp.py

To use, hook up 2 TMP101 sensors in the folloing configuration: SCL -> P9_19, SDA -> P9_20. Tie the address pins of one of them to gnd and the other fr +3.3V
tmp 1 refers to the sensor tied to gnd and tmp 2 refers to the sensor tied to +3.3V
Temperatures recorded by the sensors are in the format: temp 1: <tmp 1 temperature> temp 2: <tmp 2 temperature>

# Etch-a-Sketch
Usage: python EtchASketch.py
Note: dimensions are no longer arguments as they have been hard coded to 8x8, which is the LED matrix resolution

Left/Right rotary encoder is connected to eQEP2 on P8_11 and P8_12
Up/Down rotary encoder is connected to eQEP1 on P8_33 and P8_35
Buttons 1-4 are connected to P9_14, P9_12, P9_16, P9_23 respectively
LED matrix is connected to P9_19 (SCL) and P9_20 (SDA)

The behavior of the burrons are as follows:
Button 1 (P9_14): toggle green LED
Button 2 (P9_12): toggle red LED
Button 3 (P9_16): clear canvas
Button 4 (P9_23): toggle pen

LED color is default to yellow
Pen location starts at [0, 0] (top left corner)

To move the pen across the canvas, rotate the rotary encoders
Drawn pixels are not able to be overwritten unless the canvas is cleared first

# hw03 grading

| Points      | Description | |
| ----------- | ----------- |-|
|  6/8 | TMP101 | Didn't use /sys/class/i2c-adapter/i2c-2/new_device 
|  2/2 |   | Documentation 
|  5/5 | Etch-a-Sketch
|  0/3 |   | setup.sh | Missing
|  2/2 |   | Documentation
| 15/20 | **Total**

*My comments are in italics. --may*
