#!/usr/bin/env python3
# Clark Ren
# Date: 4 Dec 2023
# Usage: python EtchASketch.py [dimx] [dimy]
import gpiod
import sys

# Parse argumnts
if len(sys.argv) == 3:
    dimx = int(sys.argv[1])
    dimy = int(sys.argv[2])
else:
    print("Usage: python EtchASketch.py [dimx] [dimy]")
    quit()

# Initializations
coord = [0, 0]
penDown = True
canvas = []

CONSUMER='getset'
CHIP='1'
getoffsets=[14, 15, 12, 13] # P8_16, P8_15, P8_12, P8_11
setoffests=[18, 16, 19, 17] # P9_14, P9_15, P9_16, P9_23
debounce = [0, 0, 0, 0]

chip = gpiod.Chip(CHIP)

getlines = chip.get_lines(getoffsets)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)

setlines = chip.get_lines(setoffests)
setlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

# Set up canvas
for i in range(dimy):
    canvas.append(['o'] * dimx)

# Clears current canvas
def clearCanvas():
    for i in range(dimx):
        for j in range(dimy):
            canvas[j][i] = 'o'

# Displays current canvas
def printCanvas():
    for i in range(dimy):
        print(" ".join(canvas[i]))
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
    if(penDown):
        canvas[coord[1]][coord[0]] = 'x'
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
            canvas[coord[1]][coord[0]] = 'x'
    if key.lower() == 'q':
        quit()

# with keyboard.Listener(on_release=on_key_release) as listener:
#     listener.join()

# loop
while True:
    # keypress = input()
    # on_key_release(keypress)
    ev_lines = getlines.event_wait(sec=1)
    if ev_lines:
        for line in ev_lines:
            event = line.event_read()
            # print_event(event)
    vals = getlines.get_values()
    
    for val in vals:
        print(val, end=' ')
    print('\r', end='')

    setlines.set_values(vals)
    if(vals[0] == 1 and not debounce[0]):
        movePen(1)
        debounce[0] = 1
    elif(vals[0] == 0):
        debounce[0] = 0

    if(vals[1] == 1 and not debounce[1]):
        movePen(3)
        debounce[1] = 1
    elif(vals[1] == 0):
        debounce[1] = 0

    if(vals[2] == 1 and not debounce[2]):
        movePen(4)
        debounce[2] = 1
    elif(vals[2] == 0):
        debounce[2] = 0

    if(vals[3] == 1 and not debounce[3]):
        movePen(2)
        debounce[3] = 0
    elif(vals[3] == 0):
        debounce[3] = 0

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


