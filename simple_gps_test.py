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
    line = line.decode()
    print(line)
    time.sleep(1)
    data = line.split(",")
    print(data)

#	if data[0]=="$GPRMC":
#		print(data)
#   	break

#coords = {'LAT': float(data[3]),'LON': float(data[5]), 'SPEED_KTS': float(data[7]), 'HEADING': float(data[8])}
#print(coords)