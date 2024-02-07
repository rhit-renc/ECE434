# HW07

## One Wire
The relevant files are in hw07/oneWire

To connect the one wire temperature sensors to P9_14, follow the following instructions:
1. Copy hw07/BB-W1-P9.14-00A0.dts to /opt/source/bb.org-overlays/src/arm
2. To generate the .dtbo file, run the command "make; sudo make install" from /opt/source/bb.org-overlays
3. Now the .dtbo file is generated at /opt/source/bb.org-overlays/src/arm/BB-W1-P9.14-00A0.dtbo. Copy this file to /lib/firmware
4. copy hw07/uEnv.txt to /boot and reboot
5. To check the temperature of the sensor(s), run the command "cat /sys/class/hwmon/hwmonX/temp1_input", where X is the id associated with the specific sensor to check

## systemd
The relevant files are in hw07/flask

To run the flask server on startup, follow the following instructions:
1. Since the service file has already been prepared, it can be copied to /lib/systemd/system
2. To start the service, run the command "sudo systemctl start flask"
3. To start the service on startup, run the command "sudo systemctl enable flask"
4. To confirm that this works, restart the beaglebone and on the host machine, connect to http://192.168.7.2:8081/

# hw07 grading

| Points      | Description | | |
| ----------- | ----------- |-|-|
|  2/2  | Project Template | | 
|  2/2  | | Names | 
|  2/2  | | Executive Summary | 
| 10/10 | Dallas 1-wire
|  4/4  | systemd auto start |
|  0    | Blynk - Etch-a-sketch - extra
| 20/20 | **Total**

*My comments are in italics. --may*