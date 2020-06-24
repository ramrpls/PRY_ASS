import tkinter as tk
from tkinter import ttk, Label
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry('1300x700')
root.configure(background='#b3ccff')
tabControl= ttk.Notebook(root)
tab1=ttk.Frame(tabControl)
tab2=ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab #1')
tabControl.add(tab2, text='Tab #2')
tabControl.pack(expand=1,fill="both")


frame = tk.Frame(tab1, bg='#cc3300', bd=1)
frame.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.1)
load=Image.open('293.JPG')
render = ImageTk.PhotoImage(load)
img = Label(tab1, image=render)
img.image = render
img.place(x=0,y=0)

image = Image.open('293.JPG')
image = image.resize((int((image.width)-((image.width)*0.32)),int((image.height)-((image.height)*0.32))), Image.ANTIALIAS)
render = ImageTk.PhotoImage(image)
img = Label(tab2, image=render)
img.place(x=0,y=0)
# int((image.height)-((image.height)*0.32))
root.mainloop()