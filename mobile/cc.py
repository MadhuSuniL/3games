#turtle(heart)
import turtle
t=turtle.Turtle()
t.color("red")
t.begin_fill()
#t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)
t.fillcolor("red")
t.end_fill()

#a=input()

#clock
from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("clock")
def time():
    string=strftime("%H : %M : %S  %P %a %Y %D")
    label.config(text=string)
    label.after(100,time)
label=Label(root,font=("digital-7",10),background="green",foreground="white")
label.pack(anchor="center")
time()
mainloop()