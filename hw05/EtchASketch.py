#!/usr/bin/env python3
# Clark Ren
# Date: 4 Dec 2023
# Usage: python EtchASketch.py [dimx] [dimy]
#import gpiod
import sys
import smbus
import time

# # Parse argumnts
# if len(sys.argv) == 3:
#     dimx = int(sys.argv[1])
#     dimy = int(sys.argv[2])
# else:
#     print("Usage: python EtchASketch.py [dimx] [dimy]")
#     quit()

# Since LED matrix is 8x8, I am defaulting to that here
dimx = 8
dimy = 8

# Initializations
coord = [0, 0]
penDown = True
canvas = []
color = [1, 1]

dimDir = "/sys/class/i2c-adapter/i2c-2/2-001d/iio:device0/"
f = open(dimDir + "in_accel_x_raw", "r")
xInit = int(f.read())
f = open(dimDir + "in_accel_y_raw", "r")
yInit = int(f.read())
f = open(dimDir + "in_accel_z_raw", "r")
zInit = int(f.read())


# Define rotary stuff
#COUNTERPATH_LR = '/dev/bone/counter/2/count0' # counterpath of left/right encoder
#COUNTERPATH_UD = '/dev/bone/counter/1/count0' # counterpath of up/down encoder

#ms = 1 # time between samples in ms
#maxCount = '1000000'

# set eQEP max count
#f = open(COUNTERPATH_LR + '/ceiling', 'w')
#f.write(maxCount)
#f.close()
#f = open(COUNTERPATH_UD + '/ceiling', 'w')
#f.write(maxCount)
#f.close()

# Enable
#f = open(COUNTERPATH_LR + '/enable', 'w')
#f.write('1')
#f.close()
#f = open(COUNTERPATH_UD + '/enable', 'w')
#f.write('1')
#f.close()

#f_LR = open(COUNTERPATH_LR + '/count', 'r')
#f_UD = open(COUNTERPATH_UD + '/count', 'r')

#f_LR.seek(0)
#f_UD.seek(0)
#olddata_LR = f_LR.read()[:-1]
#olddata_UD = f_UD.read()[:-1]

# olddata_LR = '1'
# olddata_UD = '1'

# Define LED matrix stuff
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 0.001; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

## Define button stuff
#CONSUMER='getset'
#CHIP='1'
#setoffests=[14, 15, 12, 13] # P8_16, P8_15, P8_12, P8_11
#getoffsets=[18, 28, 19, 17] # P9_14, P9_12, P9_16, P9_23
#debounce = [0, 0, 0, 0]

LEDCanvas = []

#chip = gpiod.Chip(CHIP)

#getlines = chip.get_lines(getoffsets)
#getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)

#setlines = chip.get_lines(setoffests)
#setlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

# Set up canvas
for i in range(dimy):
    canvas.append([0] * dimx)

# Clears current canvas
def clearCanvas():
    for i in range(dimx):
        for j in range(dimy):
            canvas[j][i] = 0
    printCanvas()

# Processes the canvas into a format that can be written to the LED matrix
def displayLED(row, LEDCanvas):
    ledGreen = []
    ledRed = []
    for i in row:
        if int(i) == 1 or int(i) == 3:
            ledGreen.append(1)
        else:
            ledGreen.append(0)
        if int(i) == 2 or int(i) == 3:
            ledRed.append(1)
        else:
            ledRed.append(0)
    greenStr = ''.join(map(str, ledGreen))
    redStr = ''.join(map(str, ledRed))
    greenHex = int(greenStr, 2)
    redHex = int(redStr, 2)
    # print("green:", greenStr, greenHex)
    # print("red:", redStr, redHex)
    LEDCanvas.append(greenHex)
    LEDCanvas.append(redHex)
    # print("weh", LEDCanvas)

# Displays current canvas
def printCanvas():
    LEDCanvas = []
    rotated = []
    for i in range(dimx):
        rotated.append([])
        for j in range(dimy):
            rotated[i].append(canvas[j][i])
    for i in range(dimy):
        # print(" ".join(str(canvas[i])))
        print(canvas[i])
        row = rotated[i]
        displayLED(row, LEDCanvas)
    # print(LEDCanvas)
    # print(type(LEDCanvas[0]))
    bus.write_i2c_block_data(matrix, 0, LEDCanvas) # Write to LED matrix
    print("\n")

print("Instructions: WASD => up, left, down, right; C => clear canvas; X => Toggle pen; Press enter after single key press to perform action")
printCanvas()

# Moves pen and draws if pen is down
def movePen(direction): # using a function because it's too cluttered otherwise
    match direction:
        case 1: # left
            if coord[0] > 0:
                coord[0] -= 1
        case 2: # right
            if coord[0] < dimx - 1:
                coord[0] += 1
        case 3: # up
            if coord[1] > 0:
                coord[1] -= 1
        case 4: # down
            if coord[1] < dimy - 1:
                coord[1] += 1
    # print(coord[0], coord[1])
    if(penDown and canvas[coord[1]][coord[0]] == 0):
        canvas[coord[1]][coord[0]] = color[0] + 2*color[1]
    printCanvas()

# Performs a task based off of key input
# Remenant code from previous experimentation. Can probably be merged with movePen
def on_key_release(key):
    global penDown
    if key.lower() == 'a':
        movePen(1)
    if key.lower() == 'd':
        movePen(2)
    if key.lower() == 'w':
        movePen(3)
    if key.lower() == 's':
        movePen(4)
    if key.lower() == 'c':
        clearCanvas()
    if key.lower() == 'x':
        penDown = not penDown
        if(penDown):
            canvas[coord[1]][coord[0]] = 1
    if key.lower() == 'q':
        quit()

# with keyboard.Listener(on_release=on_key_release) as listener:
#     listener.join()

# loop
#while True:
#    # keypress = input()
#    # on_key_release(keypress)
#    ev_lines = getlines.event_wait(sec=1)
#    if ev_lines:
#        for line in ev_lines:
#            event = line.event_read()
#            # print_event(event)
#    vals = getlines.get_values()
#    
#    for val in vals:
#        print(val, end=' ')
#    print('\r', end='')
#
#    f_LR.seek(0)
#    f_UD.seek(0)
#    data_LR = f_LR.read()[:-1]
#    data_UD = f_UD.read()[:-1]
#
#    # print("data: " + data_LR + " " + str(type(data_LR)))
#    # print("olddata: " + str(olddata_LR) + " " + str(type(olddata_LR)))
#
#    # if data_LR != olddata_LR:
#    #     olddata_LR = data_LR
#
#    # Process rotary encoder
#    if data_LR > olddata_LR:
#        olddata_LR = data_LR
#        movePen(1)
#    elif data_LR < olddata_LR:
#        olddata_LR = data_LR
#        movePen(2)
#    if data_UD > olddata_UD:
#        olddata_UD = data_UD
#        movePen(3)
#    elif data_UD < olddata_UD:
#        olddata_UD = data_UD
#        movePen(4)
#    # time.sleep(ms/1000)
#
#    # Button stuff
#    setlines.set_values(vals)
#    if(vals[0] == 1 and not debounce[0]):
#        color[0] = color[0] ^ 1 # toggle green LED
#        print("color: " + str(color))
#        debounce[0] = 1
#    elif(vals[0] == 0):
#        debounce[0] = 0
#
#    if(vals[1] == 0 and not debounce[1]):
#        color[1] = color[1] ^ 1 # Toggle red LED
#        print("color: " + str(color))
#        debounce[1] = 1
#    elif(vals[1] == 1):
#        debounce[1] = 0
#
#    if(vals[2] == 1 and not debounce[2]):
#        clearCanvas()
#        debounce[2] = 1
#    elif(vals[2] == 0):
#        debounce[2] = 0
#
#    if(vals[3] == 1 and not debounce[3]):
#        penDown = not penDown
#        if(penDown):
#            canvas[coord[1]][coord[0]] = color[0] + 2*color[1]
#            printCanvas()
#        debounce[3] = 0
#    elif(vals[3] == 0):
#        debounce[3] = 0

    # printCanvas()

# while(True):
#     for evenement in pygame.event.get():
#         if evenement.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         if evenement.type == KEYDOWN:
#             if evenement.key == K_RIGHT:
#                 movePen(1)
#             if evenement.key == K_RIGHT:
#                 movePen(2)
#             if evenement.key == K_UP:
#                 movePen(3)
#             if evenement.key == K_DOWN:
#                 movePen(4)
#             if evenement.key == K_c:
#                 clearCanvas()
#             if evenement.key == K_d:
#                 penDown = not penDown

while(True):
    f = open(dimDir + "in_accel_x_raw", "r")
    x = int(f.read())
    f = open(dimDir + "in_accel_y_raw", "r")
    y = int(f.read())
    f = open(dimDir + "in_accel_z_raw", "r")
    z = int(f.read())
    if(x - xInit >= 40):
        movePen(2)
    elif(x - xInit <= -40):
        movePen(1)
    if(y - yInit >= 40):
        movePen(3)
    elif(y - yInit <= -40):
        movePen(4)
    time.sleep(0.5)
