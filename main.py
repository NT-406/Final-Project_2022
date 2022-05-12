from cgitb import grey
from tkinter import*
from tkinter import ttk
import math
from tkinter.font import BOLD
from turtle import width
import os

root = Tk()
root.title("Đơn giá")
root.geometry("600x500")

def register():
    global screen1
    screen1 = Toplevel()
    screen1.title("Register")
    screen1.geometry("900x500")
    Label(screen1, text = "ĐƠN HÀNG",fg = "green" ,font = ("calibri", 20, BOLD)).place(x=250, y = 0)
    #Creat a treeview:
    my_tree = ttk.Treeview(screen1)
    #Define columns
    my_tree['columns']= ("Name", "Price", "Decription")
    #Formate of columns
    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column("Name",  anchor= CENTER, width= 120)
    my_tree.column("Price", anchor = CENTER, width= 80)
    my_tree.column("Decription", anchor=CENTER, width= 120)
    #Creat a heading
    my_tree.heading('#0', text='', anchor= CENTER)
    my_tree.heading("Name", text = "Name", anchor= CENTER)
    my_tree.heading("Price", text = "Price", anchor= CENTER)
    my_tree.heading("Decription", text = "Decription", anchor= CENTER)
    #Add data
    data= [
        ["Heineken", 19000.0, "Test"],
        ["Tiger", 18000.0, "Test"],
        ["Corona Extra", 25000.0, "Test"]
    ]
    global count
    count = 0
    for record in data:
        my_tree.insert(parent = '', index =0 , iid=count, text = '', values = (record[0], record[1], record[2]))
        count += 1
    my_tree.place(x = 500, y= 120)
    global frameButton
    frameButton = Frame(screen1)
    Label(frameButton, text= "Tổng số tiền: " + str("2 tỷ")).pack()
    Button(frameButton, text="Xác nhận đơn hàng", command=Buy_Sucess).pack()
    
    frameButton.place(x=200,y=120)

    
def Buy_Sucess():
    Label(frameButton, text = "Đặt hàng thành công", fg = "green" ,font = ("calibri", 11)).pack()




res = Button(text = "Đơn hàng",height = "2", width = "30", command = register).pack()



root.mainloop()