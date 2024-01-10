#!/bin/sh
cd /sys/class/i2c-adapter/i2c-2
sudo chown debian:debian *
echo tmp101 0x48 > new_device
cd 2-0048/hwmon/hwmon0
cat temp1_input
