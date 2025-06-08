from tkinter import *
from tkinter_def import *

global värv
värv = "white" # начальный цвет

def värvi_valik():
    global värv # указание глобальной переменной
    if tekst.get() != "":
        tekst.configure(bg = "cyan")
        värv = tekst.get() # .get - получение информации
    else:
        tekst.configure(bg = "lightblue")
    
    figuur(värv) # перерисовывание фигуры с новым цветом

def figuur(värv:str):
    valik=var.get()
    # värv=värvi_valik()
    if valik == 1:
        Vaal(värv)
    elif valik == 2:
        Liblikas(värv)
    else:
        Prillid()
        print("Joonestan hiljem")

aken = Tk()
aken.geometry("800x400") # размер
aken.title("Graafikud")
pealkiri = Label(aken,text = "Erinevad piltid Matplotlib abil", font = "Poppins 24", fg = "purple", bg = "cyan", pady = 20, width = 200)

var = IntVar()
r1 = Radiobutton(aken, text = "Vaal", font = "Poppins 18", variable = var, value = 1, command = lambda:figuur(värv))
r2 = Radiobutton(aken, text = "Liblikas", font = "Poppins 18",variable = var, value = 2,command = lambda:figuur(värv))
r3 = Radiobutton(aken, text = "Prillid", font = "Poppins 18", variable = var, value = 3,command = lambda:figuur(värv))
tekst = Entry(aken,font = "Poppins 24", fg = "purple", bg = "cyan", width = 100)
nupp = Button(aken, text = "Värvi valik", font = "Poppins 18", fg = "cyan", bg = "purple", command = värvi_valik)

# расположение    # place(x=...,y=...), grid(column=...,row=...)
pealkiri.pack() 
tekst.pack()
nupp.pack( )
r1.pack()
r2.pack()
r3.pack()

aken.mainloop()