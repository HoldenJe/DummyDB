from tkinter import *
import time

root = Tk()
root.title('My trawl logger')
root.geometry("400x400")

logging = False

def logtrawl(event):
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


entry1 = Entry(root, width = 5)
start = Button(root, text = "start", command = logtrawl)
end = Button(root, text = "end", command = logtrawlend)
entry2 = Entry(root, width = 5, bg = 'grey')

entry1.pack(padx = 20, pady =20)
entry1.focus_set()
entry2.pack(padx = 20, pady =20)
start.pack(padx = 20, pady =20)
end.pack(padx = 20, pady =20)
root.after(100, keeplog)

start.bind("<Return>", logtrawl) # not working

root.mainloop()
