'''
is my gps connected
'''

import serial
import time

ser = serial.Serial('/dev/ttyS0')
ser.baudrate = 4800
print("ctrl+c to exit")
while 1:
    line = ser.readline()
    print(line)
    time.sleep(1)
