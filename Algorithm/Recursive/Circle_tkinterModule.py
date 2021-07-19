# tkinter : GUI module

from tkinter import *

window = Tk() # window 창 생성 
canvas = Canvas(window, height = 1000, width = 1000, bg = 'white') # Window 창 안에 도화지 생성 
canvas.pack()

cx = 1000//2 # Center X
cy = 1000//2 # Center Y
r = 400

canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width =2, outline="red")

window.mainloop() # window 창 생성 -> loop라는 건 아마 OpenCV의 imshow 처럼 계속 띄워놓기 위함일 것 


