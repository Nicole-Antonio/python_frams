import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from home import Face_Recognition_System
from register import Registration

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recognition System")
        self.root.configure(bg='white')
        self.root.resizable(width=False, height=False)

        app_width = 1000
        app_height = 650
        

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)

        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


        label = Label(self.root, text="SIGN IN",font=("Corbel Light",32),bg="white",fg="#717171")
        label.place(x=610,y=145,width=160,height=45)

        img=Image.open('gui_images\guii.png')
        img=img.resize((400,420), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg, bg="white")
        f_lb1.place(x=70,y=110)

        label = Label(self.root, text="SIGN IN",font=("Corbel Light",32),bg="white",fg="#717171")
        label.place(x=610,y=145,width=160,height=45)

        username = StringVar()
        password = StringVar()

        username_label = Label(self.root, text="Username",font=("Corbel Light",12,"normal"),bg="white",fg="black")
        username_label.place(x=527, y=230, width=80, height =20)
        self.username = Entry(self.root, textvariable=username, bg="#f2f2f2", fg="#717171", bd=0, font=("Poppins",12,"normal"), relief=RIDGE)
        self.username.place(x=527, y=255, width=340, height=40)

        password_label = Label(self.root, text="Password",font=("Corbel Light",12,"normal"),bg="white",fg="black")
        password_label.place(x=527, y=320, width=80, height=18)
        self.password = Entry(self.root, textvariable=password, bg="#F2F2F2", fg="#717171", bd=0, font=("Poppins",12,"normal"), relief=RIDGE, show='●')
        self.password.place(x=527, y=350, width=340, height=40)

        check_btn = Checkbutton(bg='white', font=("Corbel Light",11), command=self.show_password)
        check_btn.place(x=875, y=355)

        login_bt1 = Button(text="Sign In",command=self.login,cursor="hand2",font=("Poppins",12,"normal"),bg="#B779B9",fg="white",bd=0)
        login_bt1.place(x=527,y=430,width=165,height=40)
        register_btn = Button(text="Register",command=self.register, cursor="hand2",font=("Poppins",12,"normal"),bg="#B779B9",fg="white",bd=0)
        register_btn.place(x=700,y=430,width=165,height=40)
        
#==============================================================#
    def login(self):

        if (self.username.get()=="" or self.password.get()==""):
            messagebox.showerror("Error","Fill in required fields.")
        else:
            conn = mysql.connector.connect(user='root', password='',host='localhost',
                                           database='kaonashi',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from users where username=%s and password=%s",(
                self.username.get(),
                self.password.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("Log in","Log in to Admin?")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Registration(self.new_window)

    def show_password(self):
        if self.password.cget('show') == '●':
            self.password.config(show='')
        else:
            self.password.config(show='●')



    


if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
        

