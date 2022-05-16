from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox


class Display:
    def __init__(self, root):
        self.root = root
        self.root.title("NT COFFEE")
        self.root.geometry("700x500")
        self.root.configure(background="#E9EFC0")
        # self.root.resizable(width=FALSE, height=FALSE)

        self.title = Label(text="NT COFFEE", fg="#EB5353",bg="#B4E197", font=("Blacklisted",30, "bold")).place(x=250, y=10)
        self.bt_transfer1 = Button(width=0, height=0, bg="#B4E197").place(x=310, y=80)
        self.bt_transfer2 = Button(width=0,bg="#B4E197").place(x=330, y=80)
        self.bt_transfer3 = Button(width=0,bg="#B4E197").place(x=350, y=80)
        self.bt_transfer4 = Button(width=0,bg="#B4E197").place(x=370, y=80)

        self.img = PhotoImage(file=r"C:\Users\Admin\Downloads\1.png")
        Label(self.root,image=self.img).place(x=60, y=120)
        Label(self.root, image=self.img).place(x=300, y=120)
        Label(self.root, image=self.img).place(x=540, y=120)

        self.entry_1 = Entry().place(x=120, y=260, width=55)
        self.amount_1 = Label(text="Số lượng", fg="#EB5353", bg="#E9EFC0", font=("Arial",10)).place(x=117, y=240)
        self.entry_2 = Entry().place(x=361, y=260, width=55)
        self.amount_2 = Label(text="Số lượng", fg="#EB5353", bg="#E9EFC0", font=("Arial", 10)).place(x=360, y=240)
        self.entry_3 = Entry().place(x=600, y=260, width=55)
        self.amount_3 = Label(text="Số lượng", fg="#EB5353", bg="#E9EFC0", font=("Arial", 10)).place(x=599, y=240)

        self.size_1 = Combobox(values = ['Size M', 'Size L'], width=7).place(x=47, y=261)
        self.lb_size_1 = Label(text="Size", fg="#EB5353", bg="#E9EFC0", font=("Arial", 10)).place(x=60, y=240)
        self.size_2 = Combobox(values=['Size M', 'Size L'], width=7).place(x=287, y=261)
        self.lb_size_2 = Label(text="Size", fg="#EB5353", bg="#E9EFC0", font=("Arial", 10)).place(x=300, y=240)
        self.size_3 = Combobox(values=['Size M', 'Size L'], width=7).place(x=526, y=261)
        self.lb_size_3 = Label(text="Size", fg="#EB5353", bg="#E9EFC0", font=("Arial", 10)).place(x=540, y=240)

        self.bt_choose_1 = Button(text = 'Chọn', bg="#B4E197").place(x=85, y=290)
        self.bt_choose_2 = Button(text='Chọn', bg="#B4E197").place(x=325, y=290)
        self.bt_choose_3 = Button(text='Chọn', bg="#B4E197").place(x=565, y=290)



root = Tk()
t = Display(root)
root.mainloop()
