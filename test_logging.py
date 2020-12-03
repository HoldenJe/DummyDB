from tkinter import *
import time

root = Tk()
root.title('My trawl logger')
root.geometry("400x400")

logging = False

def logtrawl():
	print('begin')
	global logging
	logging = True

def logtrawlend():
	print("all done")
	global logging
	logging = False

def keeplog():
	if logging:
		print("logging")
	root.after(1000, keeplog)	

start = Button(root, text = "start", command = logtrawl).pack(padx = 20, pady =20)
end = Button(root, text = "end", command = logtrawlend).pack(padx = 20, pady =20)

root.after(100, keeplog)

root.mainloop()
