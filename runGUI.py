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
 # insert data to TR_OP
    c.execute("""INSERT INTO TR_OP VALUES (:op_year, :op_vessel, :op_serial, :tr_typeset,
                                           :tr_design, :tr_door, :tr_mesh, :tr_trawlid, 
                                           :tr_settime, :tr_towdur, :tr_speed, :tr_speedunit, 
                                           :tr_warp)""",
                {
                    'op_year': op_year.get(),
                    'op_vessel': op_vessel.get(),
                    'op_serial': op_serial.get(),
                    'tr_typeset': tr_typeset.get(),
                    'tr_design': tr_design.get(),
                    'tr_door': tr_door.get(),
                    'tr_mesh': tr_mesh.get(),
                    'tr_trawlid': tr_trawlid.get(),
                    'tr_settime': tr_settime.get(),
                    'tr_towdur': tr_towdur.get(),
                    'tr_speed': tr_speed.get(),
                    'tr_speedunit': tr_speedunit.get(),
                    'tr_warp': tr_warp.get()
                }              
              )   
    
    
    # Clear the text box
    op_serial.delete(0, END)
    op_lat.delete(0, END)
    op_lon.delete(0, END)
    op_endlat.delete(0, END)
    op_endlon.delete(0, END)
    op_beg_bot.delete(0, END)
    op_end_bot.delete(0, END)
    tr_settime.delete(0, END)
    tr_warp.delete(0, END)

    
    # comitt and close DB connection
    conn.commit()
    conn.close()

# Submit Catch to TR_CATCH
def submit_catch():
    # Connect
    conn = sqlite3.connect('mtr20_data.db')
    c = conn.cursor() 

    # check whether serial + life + spc exists prior to submit
    # return onscreen error message before c.execute

    # insert in to TR_CATCH
    c.execute("""INSERT INTO TR_CATCH VALUES (:op_year, :op_vessel, :op_serial, 
                                             :cat_life, :cat_spc, :cat_Number, 
                                             :cat_weight)""",
                {
                    'op_year': op_year.get(),
                    'op_vessel': op_vessel.get(),
                    'op_serial': op_serial.get(),
                    'cat_life': cat_life.get(),
                    'cat_spc': cat_spc.get(),
                    'cat_Number': cat_Number.get(),
                    'cat_weight': cat_weight.get()
                }              
              )   
    
    # Clear the text box
    cat_spc.delete(0, END)
    cat_Number.delete(0, END)
    cat_weight.delete(0, END)

    # comitt and close DB connection
    conn.commit()
    conn.close()




########### Build the GUI for data entry
# Divide root in to 3 panes
frame_011 = LabelFrame(root, text = "FN011")
frame_011.grid(row = 0, column = 0)

frame_121 = LabelFrame(root, text = "FN121")
frame_121.grid(row=1, column = 0)



# Build label and entry boxes
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

## create frame_121
sam = Entry(frame_121, width = 5)
sam.grid(row = 1, column = 1)
sam_label = Label(frame_121, text = "SAM")
sam_label.grid(row = 1, column = 0)

sam_lat = Entry(frame_121, width = 10)
sam_lat.grid(row = 1, column = 3)
sam_lat_label = Label(frame_121, text = "LAT")
sam_lat_label.grid(row = 1, column = 2)

sam_lon = Entry(frame_121, width = 10)
sam_lon.grid(row = 1, column = 5)
sam_lon_label = Label(frame_121, text = "LAT")
sam_lon_label.grid(row = 1, column = 4)


# Create FN121 buttons
def start_trawl():
    frame_121['bg'] = '#49A'
    startcoords = get_coords()
    print(startcoords)

def end_trawl():
    frame_121['bg'] = 'grey'
    endcoords = get_coords()
    print(endcoords)
    


TrawlStart = Button(frame_121, text = "Start Trawl", command = start_trawl)
TrawlStart.grid(row = 2, column = 0, padx = 20, pady = 20)
TrawlEnd = Button(frame_121, text = "End Trawl", command = end_trawl)
TrawlEnd.grid(row = 2, column = 1, padx = 20, pady = 20)



# Create submit button
submit_btn = Button(root, text = "Add Record", command = submit)
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

