# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:37:07 2020
Allows the creation and/or connection to a template database
@author: jeremy
"""
from tkinter import *
import sqlite3

# Create/Connect to DB
conn = sqlite3.connect('data.db')
c = conn.cursor()


# Create FN011 table - 1 time only
c.execute("""CREATE TABLE IF NOT EXISTS FN011 (
    YEAR  integer,
    PRJ_CD text,
    PRJ_LDR text    
    ) """)


# Create FN121 Table
c.execute("""CREATE TABLE IF NOT EXISTS FN121 (
    PRJ_CD text,
    SAM integer UNIQUE,
    AREA text,
    DATE text,
    LAT real,
    LON real
    )""")


# Do commit
conn.commit()

# close DB connection
conn.close()

root.mainloop()

print("FN011 created")
print("FN121 created")

