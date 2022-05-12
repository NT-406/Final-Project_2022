from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Tiệm trà sữa NT')
root.geometry("925x500+300+150")
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file=r"C:\Users\USER\Downloads\boba.png")
Label(root, image=img, bg='white', width=300).place(x=60, y=70)

Label(root, text='Trà sữa NT', fg='#FE83C6', bg='white', font=('Arial', 26, 'bold')).place(x=120, y=20)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Đăng nhập', fg='#FF5C8D', bg='white', font=('Arial', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0, 'Tên đăng nhập')



# Tên đăng nhập
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
user.place(x=30, y=80)
user.insert(0, 'Tên đăng nhập')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

def sign_in():
    username = user.get()
    password = p.get()



# Mật khẩu
p = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
p.place(x=30, y=150)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#
Button(frame, width=39, pady=7, text='Đăng nhập', bg='#FE83C6', fg='white', border=0, font=('Arial', 9)).place(x=35, y=204)
Label(frame, text='Bạn chưa có tài khoản?', fg='black', bg='white', font=('Arial', 9)).place(x=75, y=270)

sign_up = Button(frame, width=6, text='Đăng ký', border=0, bg='white', cursor='hand2', fg='#FF5C8D', font=('Arial', 9))
sign_up.place(x=215, y=270)

rewfaw
root.mainloop()
