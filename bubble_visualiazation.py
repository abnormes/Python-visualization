import random as ran
from re import X
import time
from tkinter import BOTH, Tk, Canvas, Frame
from turtle import color

array = [ran.randint(1,100) for _ in range(1000)]
heightScreen = max(array)
widthScreen = len(array)
root = Tk()
canvas = Canvas(root, width=widthScreen, height=heightScreen)

# bubble sort - O(n^2)
def sort(array, line_array) :
    size = len(array) 
    
    for i in range(size - 1):
        for i in range(size):
            if (i > 0):
                if (array[i - 1] > array[i]):
                    pivot = array[i - 1]
                    array[i - 1] = array[i]
                    array[i] = pivot
                    root.update()
                    canvas.coords(line_array[i], i - 1, 0, i - 1, array[i])
                    canvas.coords(line_array[i - 1], i, 0, i, array[i - 1])
                    

def draw():
    line_array = []
    for i in range(len(array)):
        line_array.append(canvas.create_line(i, 0, i, array[i], fill="black", width=1))
    canvas.pack(fill = BOTH)
    return line_array


root.configure(background="white")
sort(array, draw())
root.mainloop()