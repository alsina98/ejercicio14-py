import tkinter
from tkinter import *

def sel():
    label.config(text = var.get())

def reset():
    label.config(text =var.set("Si"))
    label.config(text =var.get())

window = tkinter.Tk()
window.geometry("450x450")
var = StringVar()
var.set("Si")
lista = ["Si", "No", "Blanco"]

texto_inicial = tkinter.Label(window, text="Elige una opción:")
texto_inicial.grid(column=1, row=0, padx=20, pady=20, sticky=tkinter.W)

for x in lista:
    radio1 = tkinter.Radiobutton(window, text=lista[0], variable=var, value="Si", command=sel)
    radio1.grid(column=1, row=1, padx=20, pady=20)
    radio2 = tkinter.Radiobutton(window, text=lista[1], variable=var, value="No", command=sel)
    radio2.grid(column=1, row=2, padx=20, pady=20)
    radio3 = tkinter.Radiobutton(window, text=lista[2], variable=var, value="Blanco", command=sel)
    radio3.grid(column=1, row=3, padx=20, pady=20)

buttonDeselect = tkinter.Button(window, text="Reset", command=reset)
buttonDeselect.grid(column=2, row=3, padx=20, pady=20)

label = Label(window)
label.grid(column=2, row=2, padx=20, pady=20)
label.config(text = var.get())
window.mainloop()