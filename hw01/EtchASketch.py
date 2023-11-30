#!/usr/bin/env python3
# Clark Ren
# Date: 4 Dec 2023
# Usage: python EtchASketch.py [dimx] [dimy]
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

# Set up canvas
for i in range(dimy):
    canvas.append(['o'] * dimx)

# Clears current canvas
def clearCanvas():
    for i in range(dimx):
        for j in range(dimy):
            canvas[i][j] = 'o'

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
    keypress = input()
    on_key_release(keypress)
    printCanvas()


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


