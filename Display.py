from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from pymongo import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title('Tiệm trà sữa NT')
        self.root.geometry("925x500+300+150")
        self.root.configure(bg="#fff")
        # self.root.resizable(False, False)

        # self.img = PhotoImage(file=r"C:\Users\USER\Downloads\boba.png")
        # Label(self.root, image=self.img, bg='white', width=300).place(x=60, y=70)

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

        Button(self.frame, width=39, pady=7, text='Đăng nhập', bg='#FE83C6', fg='white', border=0,
               font=('Arial', 9), command= self.order).place(x=35, y=204)
        Label(self.frame, text='Bạn chưa có tài khoản?', fg='black', bg='white', font=('Arial', 9)).place(x=75, y=270)

        # Hiển thị/ Không hiển thị mật khẩu
        # self.show_img = ImageTk.PhotoImage(file=r"C:\Users\USER\Downloads\show.png")
        # self.hide_img = ImageTk.PhotoImage(file=r"C:\Users\USER\Downloads\hide.png")

        # self.show_password = Button(self.frame, image=self.show_img, command=self.show, bg='white', cursor='hand2', border=0)
        # self.show_password.place(x=300, y=150)

        # Đăng ký
        self.sign_up = Button(self.frame, width=6, text='Đăng ký', border=0, bg='white', cursor='hand2', fg='#FF5C8D',
                              font=('Arial', 9), command=self.signup)
        self.sign_up.place(x=215, y=270)

    def on_enter(self, event):
        self.user.delete(0, 'end')

    def on_leave(self, event):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Tên đăng nhập')

    def show(self):
        self.hide_password = Button(self.frame, image=self.hide_img, command=self.hide, relief=FLAT, bg='white',
                                    cursor='hand2', border=0)
        self.hide_password.place(x=300, y=150)
        self.p.config(show='')

    def hide(self):
        self.show_password = Button(self.frame, image=self.show_img, command=self.show, relief=FLAT, bg="white",
                                    cursor="hand2", border=0)
        self.show_password.place(x=300, y=150)
        self.p.config(show='*')
    def signup(self):
        self.rootdangki = Tk()
        self.rootdangki.title('Tiệm trà sữa NT')
        self.rootdangki.geometry("925x900+300+150")
        self.rootdangki.configure(bg="#fff")

        self.mongo_client = MongoClient("mongodb://localhost:27017")
        self.db = self.mongo_client["FINALPROJECT"]
        self.col = self.db["user"]

        # img = ImageTk.PhotoImage(Image.open(r"C:\Users\Helloo\Downloads\111.png").resize ((300, 300), Image.ANTIALIAS))
        # Label(self.rootdangki, image=img, bg='white', width=300).place(x=60, y=70)
        # Label(self.rootdangki, text='Trà sữa NT', fg='#FE83C6', bg='white', font=('Arial', 26, 'bold')).place(x=30, y=20)

        self.frame = Frame(self.rootdangki, width=350, height=750, bg="white")
        self.frame.place(x=480, y=70)
        self.heading = Label(self.frame, text='Đăng ký', fg='#FF5C8D', bg='white', font=('Arial', 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Tên đăng nhập
        self.username = StringVar()
        self.user = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11), textvariable=self.username)
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Hãy nhập tên đăng nhập')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        def click(event):
            self.user.configure(state=NORMAL)
            self.user.delete(0, END)
            self.user.unbind('<Button-1>', clicked)

        clicked = self.user.bind('<Button-1>', click)

        # Mật khẩu
        self.mk=StringVar()
        self.password = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11), textvariable=self.mk)
        self.password.place(x=30, y=150)
        self.password.insert(0, 'Hãy nhập mật khẩu')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)
        #
        # def click(event):
        #     self.password.configure(state=NORMAL)
        #     self.password.delete(0, END)
        #     self.password.unbind('<Button-1>', clicked)
        #
        # clicked = self.password.bind('<Button-1>', click)

        # Mật khẩu
        self.password = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        self.password.place(x=30, y=220)
        self.password.insert(0, 'Hãy nhập lại mật khẩu')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=247)

        # def click(event):
        #     self.password.configure(state=NORMAL)
        #     self.password.delete(0, END)
        #     self.password.unbind('<Button-1>', clicked)
        #
        # clicked = self.password.bind('<Button-1>', click)

        # sđt
        self.phone = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        self.phone.place(x=30, y=290)
        self.phone.insert(0, 'Hãy nhập số điện thoại')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=317)

        clicked = self.phone.bind('<Button-1>', click)

        # địa chỉ
        self.address = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
        self.address.place(x=30, y=360)
        self.address.insert(0, 'Hãy nhập địa chỉ')
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=387)

        def click(event):
            self.address.configure(state=NORMAL)
            self.address.delete(0, END)
            self.address.unbind('<Button-1>', clicked)

        clicked = self.address.bind('<Button-1>', click)

        Button(self.frame, width=39, pady=7, text='Đăng ký tài khoản', bg='#FE83C6', fg='white', border=0,
               font=('Arial', 9)).place(x=35, y=400)
        # chưa xong chức năng
        Label(self.frame, text='Bạn đã đăng ký thành công', fg='black', bg='white', font=('Arial', 9)).place(x=75,
                                                                                                             y=440)
        Label(self.frame, text='Tên đăng nhập đã trùng, hãy nhập tên đăng nhập khác', fg='black', bg='white',
              font=('Arial', 9)).place(x=35, y=460)
        Label(self.frame, text='Số điện thoại đã trùng, hãy nhập số điện thoại đăng nhập khác', fg='black', bg='white',
              font=('Arial', 9)).place(x=35, y=490)

        self.rootdangki.mainloop()


    def order(self):
        self.root = Tk()
        self.root.title("NT COFFEE")
        self.root.geometry("1350x700")
        self.root.configure(background="#E9EFC0")
        # self.root.resizable(width=FALSE, height=FALSE)

        self.mongo_client = MongoClient("mongodb://localhost:27017")
        self.db = self.mongo_client["FINALPROJECT"]
        self.col = self.db["bill"]

        # Giao diện chính
        self.title = Label(self.root, text="NT COFFEE", fg="#EB5353", bg="#B4E197", font=("Blacklisted", 40, "bold")).place(x=540, y=10)
        # self.img_menu = PhotoImage(file=r"C:\Users\Admin\Downloads\2.png")
        # Label(self.root, image=self.img_menu).place(x=60, y=120)

        #Chọn đơn hàng

        self.name = Combobox(self.root, values=('Phin Đen', 'Phin Sữa', 'Bạc Xỉu', 'Cappuccino','Trà sữa Oreo', 'Trà sữa Olong','Matcha Macchiato','Matcha đá xay','Oreo Đá xay'), width=25)
        self.name.place(x=950, y=160)
        self.lb_name = Label(self.root, text="Name", fg="#EB5353", bg="#E9EFC0", font=("Arial", 20)).place(x=800, y=150)

        self.size = Combobox(self.root, values=('Size M', 'Size L'), width=25)
        self.size.place(x=950, y=240)
        self.lb_size = Label(self.root, text="Size", fg="#EB5353", bg="#E9EFC0", font=("Arial", 20)).place(x=800, y=230)
        self.varamount=StringVar()
        self.amount = Entry(self.root,width=30)
        self.amount.place(x=950, y=320)
        self.lb_amount = Label(self.root, text="Amount", fg="#EB5353", bg="#E9EFC0", font=("Arial", 20)).place(x=800, y=310)

        #Button chọn hàng + đặt hàng
        self.ordered_product = []
        self.bt_choose = Button(self.root, text='Choose', font=("Arial", 25, "bold"), activebackground="#B4E197", command=self.insert_product).place(x=1110, y=400)
        self.bt_end = Button(self.root, text='Chốt đơn', font=("Arial", 25, "bold"), activebackground="#B4E197", command=self.save).place(x=1110, y=500)



        self.tree = ttk.Treeview(self.root, columns=("name", "size", "amount"), height=10)
        # self.tree.bind('<Double-ButtonRelease-1>', self.selectItem)
        self.tree.heading("name", text="Name")
        self.tree.heading("size", text="size")
        self.tree.heading("amount", text="Amount")
        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.place(x=500, y=400)

    def insert_product(self):
        self.tree.insert('','end', values=(self.name.get(), self.size.get(), self.amount.get()))
        self.ordered_product.append({
            "name": self.name.get(),
            "size": self.size.get(),
            "amount": self.amount.get()
        })

    def save(self):
        # Name = self.NameEntry.get()
        # Price=self.PriceEntry.get()
        # Des= self.DescriptionText.get("1.0","end-1c")
        # self.tree.insert('','end',values=(Name,Price,Des))
        self.data = {"numsOfProducts": len(self.ordered_product),
                     "products": self.ordered_product
                    }
        self.doc = self.col.insert_one(self.data)
        if self.doc.inserted_id:
            messagebox.showinfo("Insert","Success!")
        self.delete_data()



    def delete_data(self):
        self.ordered_product.clear()
        for i in self.tree.get_children():
            self.tree.delete(i)

    def load_data(self):
        self.cur = self.col.find({})
        for d in self.cur:
            # self.tree_name = str(d['name'].encode('utf-8').decode('utf-8'))
            # self.tree_size = str(d['size'].encode('utf-8').decode('utf-8'))
            # self.tree_amount = d['amount']
            self.tree.insert("", "end", values=())

            # self.load_data()
    def close(self):
        self.rootdangki.destroy()

root = Tk()
t = Window(root)
root.mainloop()
