# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:01:46 2020
Create GUI for data entry in to MTR20 database
@author: jeremy
"""

from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import sqlite3
import serial
import datetime
import time
import statistics
#from create_import_csv import *

root = Tk()
root.title('FishNEED')
root.geometry("600x600+10+10")

# Create the "is running" variable    
running = False
global trawldone
trawldone = False

# Create/Connect to DB
conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS FN121 (
    SAM integer UNIQUE,
    AREA text,
    EFFDATE text,
    LAT real,
    LON real,
    END_LAT real,
    END_LON real,
    HEADING real,
    SPEED_KTS real
    )""")

# Do commit
conn.commit()

# in here - query the database to get max SAM and autofill the SAM value so that it is max(SAM) + 1

def get_coords():
    ser = serial.Serial('/dev/ttyS0')
    ser.baudrate = 4800
    ser.timeout = 10
    
    """# test connection - this causes issues when run here. 
    ch = ser.read()
    if len(ch) == 0:
        # create an global variable that can report the error
        # global gps_connection
        # gps_connection = FALSE
        pass"""

    while 1:
        line = ser.readline()
        line = line.decode()
        data = line.split(",")
        if data[0] == "$GPRMC":
            coords = {'LAT': float(data[3]),'LON': float(data[5]), 'SPEED_KTS': float(data[7]), 'HEADING': float(data[8])}
            return(coords)
            break

def clear_contents():
    sam.delete(0,END) 
    area.delete(0,END)
    sam_lat.delete(0,END)
    sam_lon.delete(0,END)
    sam_endlat.delete(0,END)
    sam_endlon.delete(0,END)
    start_time.delete(0, END)
    end_time.delete(0,END)
    heading.delete(0, END)
    speed.delete(0,END)
    effdate.delete(0,END)

def submit():
    current_sam = int(sam.get())
    next_sam = current_sam + 1
    clear_contents()            
    sam.insert(0, next_sam)
              

########### Build the GUI for data entry
# Divide root in to 3 panes
#frame_011 = LabelFrame(root, text = "FN011")
#frame_011.grid(row = 0, column = 0)

frame_121 = LabelFrame(root, text = "FN121")
frame_121.grid(row=1, column = 0, pady = 50, padx = 50)

## create frame_121
sam = Entry(frame_121, width = 5)
sam.grid(row = 1, column = 1)
sam_label = Label(frame_121, text = "SAM")
sam_label.grid(row = 1, column = 0)
sam.focus_set()

area = Entry(frame_121, width = 5)
area.grid(row = 2, column = 1)
area_label = Label(frame_121, text = "AREA")
area_label.grid(row = 2, column = 0)

effdate = Entry(frame_121, width = 10, bg = 'grey')
effdate.grid(row = 4, column = 1)
effdate_label = Label(frame_121, text = "EFFDATE")
effdate_label.grid(row = 4, column = 0)

start_time = Entry(frame_121, width = 10, bg = 'grey')
start_time.grid(row = 5, column = 1)
start_time_label = Label(frame_121, text = "EFFTIME")
start_time_label.grid(row = 5, column= 0)

sam_lat = Entry(frame_121, width = 10, bg = 'grey')
sam_lat.grid(row = 6, column = 1)
sam_lat_label = Label(frame_121, text = "LAT")
sam_lat_label.grid(row = 6, column = 0)

sam_lon = Entry(frame_121, width = 10, bg = 'grey')
sam_lon.grid(row = 7, column = 1)
sam_lon_label = Label(frame_121, text = "LON")
sam_lon_label.grid(row = 7, column = 0)

heading = Entry(frame_121, width = 5, bg = 'grey')
heading.grid(row = 3, column = 4)
heading_label = Label(frame_121, text = "HEADING")
heading_label.grid(row = 3, column = 3)

speed = Entry(frame_121, width = 5, bg = 'grey')
speed.grid(row = 4, column = 4)
speed_label = Label(frame_121, text = "SPEED")
speed_label.grid(row = 4, column = 3)

end_time = Entry(frame_121, width = 10, bg = 'grey')
end_time.grid(row = 5, column = 4)
end_time_label = Label(frame_121, text = "ENDTIME")
end_time_label.grid(row = 5, column= 3)

sam_endlat = Entry(frame_121, width = 10, bg = 'grey')
sam_endlat.grid(row = 6, column = 4)
sam_endlat_label = Label(frame_121, text = "END_LAT")
sam_endlat_label.grid(row = 6, column = 3)

sam_endlon = Entry(frame_121, width = 10, bg = 'grey')
sam_endlon.grid(row = 7, column = 4)
sam_endlon_label = Label(frame_121, text = "END_LON")
sam_endlon_label.grid(row = 7, column = 3)


# Create FN121 buttons
def get_localdate():
    mytime = datetime.datetime.now()
    mytimestamp = mytime.strftime("%d-%b-%Y")
    return (mytimestamp)
    
def get_localtime():
    mytime = datetime.datetime.now()
    mylocaltime = mytime.strftime("%T")
    return(mylocaltime)

def start_trawl(*args):
    global running
    running = True
    frame_121['bg'] = 'green'
    startcoords = get_coords()
    #print(startcoords)
    sam_lat.insert(0, startcoords['LAT'])
    sam_lon.insert(0, startcoords['LON'])
    effdate.insert(0, get_localdate())
    start_time.insert(0, get_localtime())
    
def end_trawl():
    global running
    running = False
    global trawldone
    trawldone = True
    frame_121['bg'] = root.cget('bg')
    endcoords = get_coords()
    #print(endcoords)
    sam_endlat.insert(0, endcoords['LAT'])
    sam_endlon.insert(0, endcoords['LON'])
    end_time.insert(0, get_localtime())
    heading.insert(0, endcoords['HEADING'])
    speed.insert(0, endcoords['SPEED_KTS'])

"""
# for logging
def log_trawl(*args):
    global trawldone
    trawldone = False
    speed = []
    heading = []
    if running:
        frame_121['bg'] = 'red'
        print('logging')               
        time.sleep(15)
        #coords = get_coords()
        #speed.append(float(coords['SPEED_KTS']))
        #heading.append(float(coords['HEADING'])) 
        
    if trawldone:
        print('done')
        #mean_speed = statistics.mean(speed)
        #mean_heading = statistics.mean(heading)
        #logged_trawl = {'SPEED': mean_speed, 'HEADING': mean_heading}
        #print(logged_trawl)
        frame_121['bg'] = root.cget('bg')
        trawldone = False
    
    root.after(1000, log_trawl)

root.after(10, log_trawl)
"""

TrawlStart = Button(frame_121, text = "Start Trawl", command = start_trawl)
TrawlStart.grid(row = 10, column = 0, padx = 20, pady = 20)
TrawlEnd = Button(frame_121, text = "End Trawl", command = end_trawl)
TrawlEnd.grid(row = 10, column = 3, padx = 20, pady = 20)


def do_submit():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    #### need to add time start and time end here and table, then check order
    c.execute("INSERT INTO FN121 VALUES (:sam, :area, :effdate, :sam_lat, :sam_lon, :sam_endlat, :sam_endlat, :heading, :speed)",
                {
                    'sam': int(sam.get()),
                    'area': area.get(),
                    'effdate': effdate.get(),
                    'var_species': int(var_species.get())
                }              
              )
    
# Create clear contents button
clear_btn = Button(root, text = "Clear Contents", command = clear_contents)
clear_btn.grid(row = 15, column = 0, pady = 5)

# Create submit button
submit_btn = Button(root, text = "Add Record", command = submit) # submit is a pass function, fix do_submit
submit_btn.grid(row = 13, column = 0, pady = 5)
#submit_btn['font'] = font.Font(size = 18)

# Create exit button
exit_btn = Button(root, text = "End Program", command = root.destroy)
exit_btn.grid(row = 14, column = 0, pady = 5)
#exit_btn['font'] = font.Font(size = 14)

# bind CTRL + ENTER to Submit Record
# code not complete - keep investigating
# root.bind('<Control-p>')


# close DB connection
conn.close()

# Runs the window
root.mainloop()

