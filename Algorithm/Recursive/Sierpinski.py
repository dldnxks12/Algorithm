
'''
# Fractal : Sierpinski Triangle

1. 삼각형의 왼쪽 아래 시작점 -> 세 개의 꼭지점 A,B,C
2. 작은 삼각형 -> 세 개의 꼭지점 A-1 , A-2, A-3
3. 반복 

'''

from tkinter import * 

window = Tk()
canvas = Canvas(window, height = 1000, width = 1000, bg ='white')
canvas.pack()

# 삼각형 -> 꼭지점 잇기

def Seripinski(x,y,length, step):

    if step > 0:
        canvas.create_line(x,y,x+length,y, fill = 'red')
        canvas.create_line(x,y,x+(length//2),y-(0.86*length),fill = 'red')
        canvas.create_line(x+(length//2), y-(0.86*length),x+length,y,fill = 'red')

        # 왼쪽 아래 삼각형
        Seripinski(x,y,length//2,step-1)
        # 오른쪽 아래 삼각형
        Seripinski(x+(length//2),y,length//2,step-1)
        # 가운데 위 삼각형
        Seripinski(x+(length//4),y-((0.86*length)//2),length//2, step-1)
    else:
        return 

x = 100
y = 800
length = 800

Seripinski(x,y,length,10)

window.mainloop()




