# Memory Map
Note: Description of blocks are placed between starting and ending addresses

FFFF_FFFF


BFFF_FFFF

EMIF0 SDRAM

8000_0000

481A_FFFF

GPIO3

481A_E000

481A_DFFF

GPIO2

481A_C000

4804_DFFF

GPIO1

4804_C000

44E0_8FFF

GPIO0

44E0_9000

1FFF_FFFF

512MB External Memory

0000_0000

# GPIO via mmap
Wiring guide:

LED 1: P8_24

LED 2: P98_18

BTN 1: P8_25

BTN 2: P8_07



Script to toggle gpio with buttons is at hw04/gpioToggle.py

Script to blink LED as fast as possible is at hw04/gpioFast.py

Script to blink LED quickly, while sleeping is at hw04/gpioSleep.py



GPIO toggling stats:

no usleep: 7.35us

with usleep: 100us


# i2c via the Kernel Driver
Wiring guide:

SCL: P9_19

SDA: P9_20



Script to check temperature is at hw04/tmp.sh

Note: This script checks the address of the TMP101 sensor at address 0x48, which has its address pin tied to ground


#  Control the LED matrix from a browser - Flask
Usage: EtchASketch.py


Wiring guide:

SCL: P9_19

SDA: P9_20


LED matrix can be manipulated from the host machine through 192.168.7.2:8081

To execute action, click respective button on the webpage


# TFT LCD Display
Note: media files contained in hw04/media


LCD Display is connected to SPI1. Wiring is as follows:

MISO: P9_29

LED: P9_16

SCK: P9_31

MOSI: P9_30

D/C: P9_27

RESET: P9_25

CS: P9_28

GND: P9_2

VCC: P9_4

### Display image:
sudo fbi -noverbose -T 1 -a ./media/boris.png

![image](./images/boris.jpg)

### Display image rotated 90 degrees:
convert ./media/boris.png -rotate 90 ./media/boris90.png;sudo fbi -noverbose -T 1 -a  ./media/boris90.png

Note: creates a new, rotated image and displays it

![image](./images/borisrot.jpg)

### Play video:
mplayer -vo fbdev2 -nolirc -framedrop -vf scale=320:240 ./media/yippee.gif

https://github.com/rhit-renc/ECE434/assets/92644174/d4980984-1c1d-410a-8ff4-01bf772e512b

### Play video rotated 90 degrees:
mplayer -vo fbdev2 -nolirc -framedrop -vf scale=240:320,rotate=1 ./media/yippee.gif

https://github.com/rhit-renc/ECE434/assets/92644174/fdf9eceb-96a9-4e37-91f5-cd36ef66fe88

### Repeat video indefinitely:
mplayer -vo fbdev2 -nolirc -framedrop -loop 0 -vf scale=320:240 ./media/yippee.gif

### Display Text:
Script to display text is at hw04/text.sh

![image](./images/boristext.jpg)

# hw04 grading

| Points      | Description | |
| ----------- | ----------- | - |
|  2/2 | Memory map 
|  4/4 | mmap()
|  4/4 | i2c via Kernel
|  5/5 | Etch-a-Sketch via flask
|  5/5 | LCD display
|      | Extras
| 20/20 | **Total**

*My comments are in italics. --may*
