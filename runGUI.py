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
#from create_import_csv import *

root = Tk()
root.title('FishNEED')
root.geometry("800x600")


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



def submit():
    # Connect
    conn = sqlite3.connect('mtr20_data.db')
    c = conn.cursor() 
    
    # insert data to OP
    c.execute("""INSERT INTO OP VALUES (:op_year, :op_date, :op_vessel, :op_serial, :op_samplety, 
                                        :op_lake, :op_port, :op_target, :op_lat, :op_lon, :op_endlat, 
                                        :op_endlon, :op_beg_bot, :op_end_bot, :op_depunit, 
                                        :op_vessdir, :op_winddir, :op_windspeed, :op_seacond, :op_surftemp)""",
                {
                    'op_year': op_year.get(),
                    'op_date': op_date.get(),
                    'op_vessel': op_vessel.get(),
                    'op_serial': op_serial.get(),
                    'op_samplety': op_samplety.get(),
                    'op_lake': op_lake.get(),
                    'op_port': op_port.get(),
                    'op_target': op_target.get(),
                    'op_lat': op_lat.get(),
                    'op_lon': op_lon.get(),
                    'op_endlat': op_endlat.get(),
                    'op_endlon': op_endlon.get(),
                    'op_beg_bot': op_beg_bot.get(),
                    'op_end_bot': op_beg_bot.get(),
                    'op_depunit': op_depunit.get(),
                    'op_vessdir': op_vessdir.get(),
                    'op_winddir': op_winddir.get(),
                    'op_windspeed': op_windspeed.get(),
                    'op_seacond': op_seacond.get(),
                    'op_surftemp': op_surftemp.get()
                }              
              )

########### Build the GUI for data entry
# Divide root in to 3 panes
#frame_011 = LabelFrame(root, text = "FN011")
#frame_011.grid(row = 0, column = 0)

frame_121 = LabelFrame(root, text = "FN121")
frame_121.grid(row=1, column = 0)


# Build label and entry boxes
"""
prjyear = Entry(frame_011, width = 5)
prjyear.grid(row = 1, column = 1)
prjyear_label = Label(frame_011, text = "YEAR")
prjyear_label.grid(row = 1, column = 0)


prjcd = Entry(frame_011, width = 5)
prjcd.grid(row = 2, column = 1)
prjcd_label = Label(frame_011, text = "PRJ_CD")
prjcd_label.grid(row = 2, column = 0)


prjld = Entry(frame_011, width = 5)
prjld.grid(row = 3, column = 1)
prjld_label = Label(frame_011, text = "PRJ_LEAD")
prjld_label.grid(row = 3, column = 0)
"""
## create frame_121
sam = Entry(frame_121, width = 5)
sam.grid(row = 1, column = 1)
sam_label = Label(frame_121, text = "SAM")
sam_label.grid(row = 1, column = 0)

sam_lat = Entry(frame_121, width = 10)
sam_lat.grid(row = 2, column = 1)
sam_lat_label = Label(frame_121, text = "LAT")
sam_lat_label.grid(row = 2, column = 0)

sam_lon = Entry(frame_121, width = 10)
sam_lon.grid(row = 3, column = 1)
sam_lon_label = Label(frame_121, text = "LON")
sam_lon_label.grid(row = 3, column = 0)

sam_endlat = Entry(frame_121, width = 10)
sam_endlat.grid(row = 2, column = 4)
sam_endlat_label = Label(frame_121, text = "END_LAT")
sam_endlat_label.grid(row = 2, column = 3)

sam_endlon = Entry(frame_121, width = 10)
sam_endlon.grid(row = 3, column = 4)
sam_endlon_label = Label(frame_121, text = "END_LON")
sam_endlon_label.grid(row = 3, column = 3)


# Create FN121 buttons
def start_trawl():
    frame_121['bg'] = 'green'
    startcoords = get_coords()
    #print(startcoords)
    sam_lat.insert(0, startcoords['LAT'])
    sam_lon.insert(0, startcoords['LON'])

def end_trawl():
    frame_121['bg'] = 'lightgrey'
    endcoords = get_coords()
    #print(endcoords)
    sam_endlat.insert(0, endcoords['LAT'])
    sam_endlon.insert(0, endcoords['LON'])



TrawlStart = Button(frame_121, text = "Start Trawl", command = start_trawl)
TrawlStart.grid(row = 4, column = 0, padx = 20, pady = 20)
TrawlEnd = Button(frame_121, text = "End Trawl", command = end_trawl)
TrawlEnd.grid(row = 4, column = 3, padx = 20, pady = 20)


def do_submit():
    pass

# Create submit button
submit_btn = Button(root, text = "Add Record", command = do_submit)
submit_btn.grid(row = 13, column = 0, pady = 20)
submit_btn['font'] = font.Font(size = 18)

# Create exit button
exit_btn = Button(root, text = "End Program", command = root.destroy)
exit_btn.grid(row = 14, column = 0, pady = 20)
exit_btn['font'] = font.Font(size = 14)

# bind CTRL + ENTER to Submit Record
# code not complete - keep investigating
# root.bind('<Control-p>')

# Create/Connect to DB
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Do commit
conn.commit()

# close DB connection
conn.close()

# Runs the window
root.mainloop()

