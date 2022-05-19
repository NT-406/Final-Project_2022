from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from pymongo import *
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["example"]
col = db["NTN"]

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Tiệm trà sữa NT')
        self.root.geometry('1166x718')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.img = PhotoImage(file=r"C:\Users\Helloo\Downloads\111.png")
        Label(self.root, image=self.img, bg='white', width=300).place(x=60, y=70)

        Label(self.root, text='Trà sữa NT', fg='#FE83C6', bg='white', font=('Arial', 26, 'bold')).place(x=120, y=20)

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        self.heading = Label(self.frame, text='Đăng nhập', fg='#FF5C8D', bg='white', font=('Arial', 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Nhập tên đăng nhập
        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Tên đăng nhập')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)
        self.user.bind('<FocusIn>', self.on_enter)
        self.user.bind('<FocusOut>', self.on_leave)
        
        # Nhập mật khẩu
        self.p = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        self.p.place(x=30, y=150)
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)


        # Hiển thị/ Không hiển thị mật khẩu
        self.show_img = ImageTk.PhotoImage(file=r"C:\Users\Helloo\Downloads\111.png")
        self.hide_img = ImageTk.PhotoImage(file=r"C:\Users\Helloo\Downloads\111.png")

        self.show_password = Button(self.frame, image=self.show_img, command=self.show, bg='white', cursor='hand2', border=0)
        self.show_password.place(x=300, y=150)

        def login():
            username=self.user.get()
            password=self.p.get()
            if(username =="" or username=='Tên đăng nhập'):
                messagebox.showinfo("","Bạn quên nhập tên đăng nhập")
            elif(password =="" ):
                messagebox.showinfo("","Bạn quên nhập mat khau")
            elif self.value_exist_in_coll("name_find", username, "NTN"):
                if self.value_exist_in_coll("password_find", password, "NTN"):
                    messagebox.showinfo("", "Đăng nhập thành công")
                    self.opmain()
            else:
                messagebox.showinfo("","Mật khẩu hoặc tên đăng nhập sai!")

        # Đăng ký
        Button(self.frame, width=39, pady=7, text='Đăng nhập', bg='#FE83C6', fg='white', border=0, font=('Arial', 9),command=login).place(x=35, y=204)
        
        Label(self.frame, text='Bạn chưa có tài khoản?', fg='black', bg='white', font=('Arial', 9)).place(x=75, y=270)

        self.sign_up = Button(self.frame, width=6, text='Đăng ký', border=0, bg='white', cursor='hand2', fg='#FF5C8D', font=('Arial', 9),command=self.new)
        self.sign_up.place(x=215, y=270)
        self.root.mainloop()
        
    def value_exist_in_coll(self, key, value, collection):
        for i in db[collection].find():
            if i[key] == value:
                return True
        return False


    def on_enter(self, event):
        self.user.delete(0, 'end')

    def on_leave(self, event):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Tên đăng nhập')

    def show(self):
            self.hide_password = Button(self.frame, image=self.hide_img, command=self.hide, relief=FLAT, bg='white', cursor='hand2', border=0)
            self.hide_password.place(x=300, y=150)
            self.p.config(show='')

    def hide(self):
            self.show_password = Button(self.frame, image=self.show_img, command=self.show, relief=FLAT, bg="white", cursor="hand2", border=0)
            self.show_password.place(x=300, y=150)
            self.p.config(show='*')
    



    def new(self):
        self.root.destroy()
        self.rootdangki=Tk()
        #self.rootdangki.winfo_toplevel()
        self.rootdangki.title('Tiệm trà sữa NT')
        self.rootdangki.geometry("925x900+300+150")
        self.rootdangki.configure(bg="#fff")

        img = ImageTk.PhotoImage(Image.open(r"C:\Users\Helloo\Downloads\111.png").resize ((300, 300), Image.ANTIALIAS))
        Label(self.rootdangki, image=img, bg='white', width=300).place(x=60, y=70)
        Label(self.rootdangki, text='Trà sữa NT', fg='#FE83C6', bg='white', font=('Arial', 26, 'bold')).place(x=30, y=20)

        self.frame = LabelFrame(self.rootdangki, width=350, height=550, bg="white")
        self.frame.place(x=480, y=70)
        self.heading = Label(self.frame, text='Đăng ký', fg='#FF5C8D', bg='white', font=('Arial', 23, 'bold'))
        self.heading.place(x=100, y=5)

            # Tên đăng nhập
        self.user_var=StringVar() 
        self.userr=Label(self.frame, text='Tên đăng nhập',bg='white',font=('Arial', 12,'bold')).place(x=30,y=55)
        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 8),textvariable=self.user_var)
        self.user.place(x=30, y=85)
        self.user.insert(0, 'Hãy nhập tên đăng nhập')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        def click(event):
            self.user.configure(state=NORMAL)
            self.user.delete(0, END)
            self.user.unbind('<Button-1>', clicked)
        clicked = self.user.bind('<Button-1>', click)


            # Mật khẩu
        self.password_var=StringVar() 
        self.passwordd=Label(self.frame, text='Mật khẩu',bg='white',font=('Arial', 12,'bold')).place(x=30,y=125)
        self.password = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 8),textvariable=self.password_var)
        self.password.place(x=30, y=155)
        #self.password.insert(0, 'Hãy nhập mật khẩu')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        # def click(event):
        #     self.password.configure(state=NORMAL)
        #     self.password.delete(0, END)
        #     self.password.unbind('<Button-1>', clicked)
        # clicked = self.password.bind('<Button-1>', click)


            # Mật khẩu
        self.again_password_var=StringVar() 
        self.again_passworddd=Label(self.frame, text='Nhập lại mật khẩu',bg='white',font=('Arial', 12,'bold')).place(x=30,y=195)
        self.again_password = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 8),textvariable=self.again_password_var)
        self.again_password.place(x=30, y=225)
        #self.password.insert(0, 'Hãy nhập lại mật khẩu')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=247)
        # def click(event):
        #     self.password.configure(state=NORMAL)
        #     self.password.delete(0, END)
        #     self.password.unbind('<Button-1>', clicked)
        # clicked = self.password.bind('<Button-1>', click)

            #sđt
        self.phone_var=StringVar() 
        self.phonee=Label(self.frame, text='Số điện thoại',bg='white',font=('Arial', 12,'bold')).place(x=30,y=265)
        self.phone = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 8),textvariable=self.phone_var)
        self.phone.place(x=30, y=295)
        # self.phone.insert(0, 'Hãy nhập số điện thoại')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=317)
        # def click(event):
        #     self.phone.configure(state=NORMAL)
        #     self.phone.delete(0, END)
        #     self.phone.unbind('<Button-1>', clicked)
        # clicked = self.phone.bind('<Button-1>', click)


            #địa chỉ
        self.address_var=StringVar() 
        self.addresss=Label(self.frame, text='Địa chỉ',bg='white',font=('Arial', 12,'bold')).place(x=30,y=335)
        self.address = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 8),textvariable=self.address_var)
        self.address.place(x=30, y=365)
        #self.address.insert(0, 'Hãy nhập địa chỉ')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=387)
        # def click(event):
        #     self.address.configure(state=NORMAL)
        #     self.address.delete(0, END)
        #     self.address.unbind('<Button-1>', clicked)
        # clicked = self.address.bind('<Button-1>', click)
        def checkdata():
            username_login=self.user.get()
            password_login=self.password.get()
            again_password_login=self.again_password.get()
            phone_login=self.phone.get()
            address_login=self.address.get()
           
            if(username_login =="" or username_login=='Hãy nhập tên đăng nhập'):
                messagebox.showinfo("","Bạn quên nhập tên đăng nhập")
            elif(password_login ==""):
                messagebox.showinfo("","Bạn quên nhập mật khẩu")
            elif len(password_login)<=7 :
                messagebox.showinfo("","Hãy nhập mật khẩu từ 8 kí tự trở lên")
            elif(again_password_login ==""):
                messagebox.showinfo("","Bạn quên nhập lại mật khẩu")
            elif(password_login !=again_password_login):
                messagebox.showinfo("","Bạn nhập mật khẩu không khớp")
            elif(phone_login ==""):
                messagebox.showinfo("","Bạn quên nhập số điện thoại")
            elif(phone_login!=""):
                try:
                    n = int(self.phone.get())
                    if len(phone_login)!=10:
                        messagebox.showinfo("","Số điện thoại phải gồm 10 số")
                    elif(address_login ==""):
                        messagebox.showinfo("","Bạn quên nhập địa chỉ liên lạc")
                    elif(username_login!=""and password_login!=""and again_password_login!="" and phone_login!="" and address_login!=""):
                        messagebox.showinfo("","Bạn đã đăng kí thành công")
                        self.closerootdangki()
                        self.save()
                        Window()
                except ValueError or AttributeError:
                    messagebox.showinfo("Kết quả","Dữ liệu không đúng! Vui lòng chỉ nhập số ở ô số điện thoại!")
                


        Button(self.frame, width=39, pady=7, text='Đăng ký tài khoản', bg='#FE83C6', fg='white', border=0, font=('Arial', 9),command=checkdata).place(x=35, y=400)
    
        #chưa xong chức năng
        Label(self.frame, text='Bạn đã đăng ký thành công', fg='black', bg='white', font=('Arial', 9)).place(x=75, y=440)
        Label(self.frame, text='Tên đăng nhập đã trùng, hãy nhập tên đăng nhập khác', fg='black', bg='white', font=('Arial', 9)).place(x=35, y=460)
        Label(self.frame, text='Số điện thoại đã trùng, hãy nhập số điện thoại đăng nhập khác', fg='black', bg='white', font=('Arial', 9)).place(x=35, y=490)

        self.rootdangki.mainloop()

    
        
    def closerootdangki(self):
        self.rootdangki.destroy()
    def opmain(self): 
        self.root.destroy()
        self.main=Tk()
        self.main.mainloop()
    def save(self):
        data = {"name_find": self.user_var.get(), "password_find": self.password_var.get(), "phone": self.phone_var.get(),"address": self.address_var.get()}
        doc = col.insert_one(data)


Window()

