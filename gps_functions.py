# python 2
# the addition of line.decode makes it work in py3, but not always and breaks it in py2

# create a function that prints coordinates

import serial
import datetime
import time
import statistics

def get_coords():
    ser = serial.Serial('/dev/ttyS0')
    ser.baudrate = 4800
    ser.timeout = 10
    
    while 1:
        line = ser.readline()
        line = line.decode()
        data = line.split(",")
        if data[0] == "$GPRMC":
            break
    coords = {'LAT': data[3],'LON': data[5], 'SPEED_KTS': data[7], 'HEADING': data[8]}
    return(coords)

'''
while 1:
    get_coords()
'''
def get_UTCtime():
    allcoords = get_coords()
    UTCtime = int(allcoords[1])
    # EST = UTC - 50000
    return(UTCtime)

def get_UTCdate():
    allcoords = get_coords()
    UTCdate = allcoords[9]
    return(UTCdate)

def get_localdate():
    mytime = datetime.datetime.now()
    mytimestamp = mytime.strftime("%d-%b-%Y")
    print (mytimestamp)
    
def get_localtime():
    mytime = datetime.datetime.now()
    mylocaltime = mytime.strftime("%T")
    return(mylocaltime)
    
def log_trawl():
    speed = []
    heading = []
    for i in range(5):
            coords = get_coords()
            speed.append(float(coords['SPEED_KTS']))
            heading.append(float(coords['HEADING']))                
            time.sleep(15)
            #return(coords['SPEED_KTS'])    
    mean_speed = statistics.mean(speed)
    mean_heading = statistics.mean(heading)
    logged_trawl = {'SPEED': mean_speed, 'HEADING': mean_heading}
    return(logged_trawl)