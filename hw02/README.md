# Questions
## Schell script questions

1. min voltage: -30mV, max voltage: 3.14V

2. frequency: 980mHz, period: 1.02s

3. blinkLED.sh uses between 0% and 1.3% of the CPU, usually hovering at around 0.6%

4. shortest period is around 17ms

| Sleep time | Period | Consistency | Processor Usage |
| ---------- | ------ | ----------- | --------------- |
| 0.1s | 218-230ms | Consistent | 1.9% |
| 0.01s | 38.5ms | Consistent | 1.9% |
| 0.05s | 118.5ms | Consistent | 3.8% |
| 0.0001s | 25ms | Inconsistent | 20.1% |
| 0.00001s | 23ms | Inconsistent | 21% |
| 0.000001s | 17ms | Inconsistent | 21% |

5. the period is very unstable and can range from arounf 17ms to around 44ms

6. period is still unstable

7. Removing the setup code did not impact the period and removing the sleeps caused the period to look like noise

8. the shortest period I can get is around 17ms

## Python script questions

1. 3.3kHz, 300us

2. 70% CPU usage

3. 
| Script | Min Period | CPU Usage |
| ------ | ---------- | --------- |
| Shell | 17ms | 21% |
| Python | 300us | 70% |

## C script questions

# Etch-A-Sketch
Usage: python EtchASketch.py [dimx] [dimy] dimx: number of horizontal characters used in the canvas dimy: number of vertical characters used in the canvas

Pen location starts at [0, 0] (top left corner)

The following wiring guide assumes the following schema: [left, up, down, right]

LED wirings: [P9_14, P9_15, P8_12, P8_11]

Button wirings: [P8_16, P8_15, P8_12, P8_11]

Keyboard function has been removed to implement button control. Note that as a result, the functionality to clear the canvas and raise or lower the pen has also ben removed.

To move the pen across the canvas, use the buttons. The pen should move as soon as the button is pressed and additional inputs for the same direction must be input after the release of the button.
