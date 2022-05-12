from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title('Tiệm trà sữa NT')
        self.root.geometry("925x500+300+150")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.img = PhotoImage(file=r"C:\Users\USER\Downloads\boba.png")
        Label(self.root, image=self.img, bg='white', width=300).place(x=60, y=70)

        Label(self.root, text='Trà sữa NT', fg='#FE83C6', bg='white', font=('Arial', 26, 'bold')).place(x=120, y=20)

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        self.heading = Label(self.frame, text='Đăng nhập', fg='#FF5C8D', bg='white', font=('Arial', 23, 'bold'))
        self.heading.place(x=100, y=5)

        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Tên đăng nhập')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)
        self.user.bind('<FocusIn>', self.on_enter)
        self.user.bind('<FocusOut>', self.on_leave)

        self.p = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        self.p.place(x=30, y=150)
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(self.frame, width=39, pady=7, text='Đăng nhập', bg='#FE83C6', fg='white', border=0, font=('Arial', 9)).place(x=35, y=204)
        Label(self.frame, text='Bạn chưa có tài khoản?', fg='black', bg='white', font=('Arial', 9)).place(x=75, y=270)

        self.sign_up = Button(self.frame, width=6, text='Đăng ký', border=0, bg='white', cursor='hand2', fg='#FF5C8D', font=('Arial', 9))
        self.sign_up.place(x=215, y=270)

    def on_enter(self, event):
        self.user.delete(0, 'end')
    
    def on_leave(self, event):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Tên đăng nhập')
            
        
root = Tk()
t = Window(root)
root.mainloop()
