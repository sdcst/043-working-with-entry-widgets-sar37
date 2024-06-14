#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk 
from tkinter.constants import SUNKEN

def hypotenuse(event):
    SA = a.get()
    SB = b.get()

    try:
        SA = float(SA)
        SB = float(SB)
        H = ((SA**2)+(SB**2))**0.5
    except:
        text.config(text="Oh no! the entry was not valid")

    h = round(H)
    if H == h:
        c.delete(0,tk.END)
        c.insert(0,H)
        text.config(text ="Result will be here: the result of the hypotenuse is an exact number and didn't need to be rounded." )

    else:
        HH = round(H,2)
        c.delete(0,tk.END)
        text.config(text = "Results will be here:The result of the hypotenuse has been rounded off the teo decimals.")

w = tk.Tk()
w.geometry = "200x200"

instructions = tk.Label(w,text = " I can help you figure out thr hypotenuse of a triangle. Enter side A and side B into the given area.")

A = tk.Label(w, text = "Side A")
B = tk.Label(w, text = "Side B")
C = tk.Label(w, text = "Hypotenuse")

a = tk.Entry(w, text= " side a")
b = tk.Entry(w, text = "side b")


load = tk.Button(w, text = "LOAD", relief = SUNKEN)

text = tk.Label(w, text = "Results will be here")

c = tk.Entry(w, text = "hypotenuse")

load.bind("<Button-1>", hypotenuse)

instructions.grid(row = 1, column =1,columnspan = 4)

A.grid(row =2, column = 1)
B.grid(row=2, column=2)
C.grid(row=3, column=4)
a.grid(row=3, column=1)
b.grid(row=3, column=2)

load.grid(row=3, column=3)
c.grid(row=3, column=4)

text.grid(row=4,column = 1, columnspan=4)

w.mainloop()

    

    



window = tk.Tk
window.attributes('-topmost',True)



window.mainloop()