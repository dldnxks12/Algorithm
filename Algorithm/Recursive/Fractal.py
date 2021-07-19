from tkinter import *

# Make Fractal

window = Tk()
canvas = Canvas(window, height = 1000, width = 1000, bg = 'white')
canvas.pack()

def fractal(centerX, centerY, radius, step):
    
    if step > 0 :
        canvas.create_oval(centerX-radius, centerY-radius, centerX+radius, centerY+radius, width = 2, outline = 'red')
        fractal((centerX+(radius//2)), centerY, radius//2, step-1)
        fractal((centerX-(radius//2)), centerY, radius//2, step-1)
        
    else:
        return 

fractal(500,500,200,4)

window.mainloop()




