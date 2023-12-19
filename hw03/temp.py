#!/usr/bin/env python3
# Read tmp101 sensors

import smbus
import time

bus = smbus.SMBus(2)
addr1 = 0x48
addr2 = 0x4a

while True:
    temp1 = bus.read_byte_data(addr1, 0)
    temp2 = bus.read_byte_data(addr2, 0)
    print("temp 1:", temp1, "temp 2:", temp2, end="\r")
    time.sleep(0.25)