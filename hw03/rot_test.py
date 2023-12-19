#!/usr/bin/env python3

import time

eQEP = '2'
COUNTERPATH = '/dev/bone/counter/' + eQEP + '/count0'

eQEP2 = '1'
COUNTERPATH1 = '/dev/bone/counter/' + eQEP2 + '/count0'

ms = 100 # time between samples in ms
maxCount = '1000000'

# set eQEP max count
f = open(COUNTERPATH+ '/ceiling', 'w')
f.write(maxCount)
f.close()

f = open(COUNTERPATH1+ '/ceiling', 'w')
f.write(maxCount)
f.close()

# Enable
f = open(COUNTERPATH + '/enable', 'w')
f.write('1')
f.close()
f = open(COUNTERPATH1 + '/enable', 'w')
f.write('1')
f.close()

f = open(COUNTERPATH + '/count', 'r')
f1 = open(COUNTERPATH1 + '/count', 'r')

olddata = '1'
olddata1 = '1'
while True:
    f.seek(0)
    f1.seek(0)
    data = f.read()[:-1]
    data1 = f1.read()[:-1]
    # print only if data changes
    # print("data: " + data + " " + str(type(data)))
    # print("olddata: " + str(olddata) + " " + str(type(olddata)))
    if data != olddata:
        print(data > olddata)
        olddata = data
        print("data = " + data)
    if data1 != olddata1:
        olddata1 = data1
        print("data1 = " + data1)
    time.sleep(ms/1000)