# python 2
# the addition of line.decode makes it work in py3, but not always and breaks it in py2

# create a function that prints coordinates

import serial
import datetime
def get_coords():
    ser = serial.Serial('/dev/ttyS0')
    ser.baudrate = 4800
    ser.timeout = 10
    
    while 1:
        line = ser.readline()
        line = line.decode()
        data = line.split(",")
        if data[0] == "$GPRMC":
            #print (data)
            #mytime = datetime.datetime.now()
            #mytimestamp = mytime.strftime("%B %d %Y %I:%M%p")
            #print (mytimestamp, data[3], data[5])
            # data[1] gives UTC, EDT = UTC-40000
            #print (data[9],data[1], data[3:7])
            #return(data)
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
    
