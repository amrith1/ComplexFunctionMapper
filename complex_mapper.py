import numpy as np
import sys
from tkinter import *
import time

xmin = -1 * np.pi
xmax = np.pi
xstep = 0.05 * np.pi
ymin = -4 * np.pi
ymax = 4 *np.pi
ystep = 0.05 * np.pi

xvisible = int(np.floor((xmax - xmin)/xstep))
yvisible = int(np.floor((ymax - ymin)/ystep))

canvasWidth = 1800
canvasHeight = 1000

displayWindow = [-54000.0, -30000.0, 54000.0, 30000.0]

animation_steps = 10

def tkinterX(x_coord):
	return int(np.floor((x_coord - displayWindow[0])/(displayWindow[2] - displayWindow[0]) * canvasWidth))
def tkinterY(y_coord):
	return canvasHeight - int(np.floor((y_coord - displayWindow[1])/(displayWindow[3] - displayWindow[1]) * canvasHeight))
def function(value):
	return np.cos(value)

domain = [ [ ((xmin + xval*xstep) + (ymin + yval*ystep)*1j) for yval in range(yvisible + 1) ] for xval in range(xvisible + 1) ]
intermediate = [ [ ((xmin + xval*xstep) + (ymin + yval*ystep)*1j) for yval in range(yvisible + 1) ] for xval in range(xvisible + 1) ]
output = [[ function(domain[xval][yval]) for yval in range(yvisible + 1)] for xval in range(xvisible + 1)]
change_step = [[ (output[xval][yval] - domain[xval][yval])/animation_steps for yval in range(yvisible + 1)] for xval in range(xvisible + 1)]

master = Tk()
canvas = Canvas(master, width=canvasWidth, height=canvasHeight)
canvas.pack()

#canvas_points = [ [canvas.create_oval(tkinterX(point.real) - 1, tkinterY(point.imag) - 1, tkinterX(point.real) + 1, tkinterY(point.imag) + 1, fill = 'black') for point in array] for array in output]

canvas_lines = []
for xval in range(xvisible):
	canvas_lines.append([])
	for yval in range(yvisible):
		canvas_lines[xval].append([])
		canvas_lines[xval][yval].append(canvas.create_line(tkinterX(output[xval][yval].real), tkinterY(output[xval][yval].imag), tkinterX(output[xval + 1][yval].real), tkinterY(output[xval + 1][yval].imag)))
		canvas_lines[xval][yval].append(canvas.create_line(tkinterX(output[xval][yval].real), tkinterY(output[xval][yval].imag), tkinterX(output[xval][yval + 1].real), tkinterY(output[xval][yval + 1].imag)))

while True:
	for step in range(animation_steps):
		for xval in range(xvisible):
			for yval in range(yvisible):
				intermediate[xval][yval] += change_step[xval][yval]
		for xval in range(xvisible):
			for yval in range(yvisible):
				canvas.coords(canvas_lines[xval][yval], tkinterX(intermediate[xval][yval].real), tkinterY(intermediate[xval][yval].imag), tkinterX(intermediate[xval + 1][yval].real), tkinterY(intermediate[xval + 1][yval].imag))
				canvas.coords(canvas_lines[xval][yval], tkinterX(intermediate[xval][yval].real), tkinterY(intermediate[xval][yval].imag), tkinterX(intermediate[xval][yval + 1].real), tkinterY(intermediate[xval][yval + 1].imag))
		master.update()
		time.sleep(0.002)

		
	for xval in range(xvisible):
		for yval in range(yvisible):
			canvas.coords(canvas_lines[xval][yval], tkinterX(output[xval][yval].real), tkinterY(output[xval][yval].imag), tkinterX(output[xval + 1][yval].real), tkinterY(output[xval + 1][yval].imag))
			canvas.coords(canvas_lines[xval][yval], tkinterX(output[xval][yval].real), tkinterY(output[xval][yval].imag), tkinterX(output[xval][yval + 1].real), tkinterY(output[xval][yval + 1].imag))
	master.update()
	time.sleep(1.0)
	intermediate = [ [ ((xmin + xval*xstep) + (ymin + yval*ystep)*1j) for yval in range(yvisible + 1) ] for xval in range(xvisible + 1) ]


#master.mainloop()

