#!/usr/bin/env python3

import smbus
import time

bus = smbus.SMBus(2)
addr = 0x1d

while True:
    data = bus.read_byte_data(addr, 0)
    print("accel:", data, end="\r")
    time.sleep(0.2)
