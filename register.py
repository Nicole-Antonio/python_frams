import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

class Registration:
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

        label = Label(self.root, text="SIGN UP",font=("Corbel Light",30),bg="white",fg="black")
        label.place(x=40,y=39,width=190,height=80)

        self.uname = StringVar()
        self.pword = StringVar()
        self.fullname = StringVar()
        self.mobilenum = StringVar()
        self.id = StringVar()

        img=Image.open('gui_images\picture.jpg')
        img=img.resize((450,450), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg, bg="white")
        f_lb1.place(x=500,y=140)

        label2 = Label(self.root, text="Please provide all the required information.",font=("Corbel Light",16),bg="white",fg="black")
        label2.place(x=40,y=100,width=400,height=80)

        name_label = Label(self.root, text="Full Name",font=("Corbel Light",11,"normal"),bg="white",fg="black")
        name_label.place(x=70, y=190, width=82, height =18)
        self.name = Entry(self.root, textvariable=self.fullname, bg="#f7f7f7", fg="#505050", bd=0, font=("Corbel Light",12,"normal"), relief=RIDGE)
        self.name.place(x=70, y=216, width=340, height=35)

        number_label = Label(self.root, text="Mobile No.",font=("Corbel Light",11,"normal"),bg="white",fg="black")
        number_label.place(x=70, y=266, width=82, height =18)
        self.number = Entry(self.root, textvariable=self.mobilenum, bg="#f7f7f7", fg="#505050", bd=0, font=("Corbel Light",12,"normal"), relief=RIDGE)
        self.number.place(x=70, y=292, width=340, height=35)

        username_label = Label(self.root, text="Username",font=("Corbel Light",11,"normal"),bg="white",fg="black")
        username_label.place(x=70, y=342, width=79, height =18)
        self.username = Entry(self.root, textvariable=self.uname, bg="#f7f7f7", fg="#505050", bd=0, font=("Corbel Light",12,"normal"), relief=RIDGE)
        self.username.place(x=70, y=368, width=340, height=35)

        password_label = Label(self.root, text="Password",font=("Corbel Light",11,"normal"),bg="white",fg="black")
        password_label.place(x=70, y=418, width=79, height=18)
        self.password = Entry(self.root, textvariable=self.pword, bg="#f7f7f7", fg="#505050", bd=0, font=("Corbel Light",12,"normal"), relief=RIDGE)
        self.password.place(x=70, y=444, width=340, height=35)

        register_bt1 = Button(self.root, text="Register",cursor="hand2",command=self.insert_record, font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        register_bt1.place(x=70,y=520,width=160,height=38)
        cancel_btn = Button(self.root, text="Cancel",cursor="hand2", command=self.close, font=("Arial",12,"normal"),bg="#FF6E54",fg="white",bd=0)
        cancel_btn.place(x=245,y=520,width=160,height=38)

        forgotPassword = Button(self.root, text='Already have an account?', command=self.close,font=("Corbel Light", 16, "underline"), bg='white', fg="#904392",
                borderwidth=0, activebackground='#f8f8f8', cursor="hand2")
        forgotPassword.place(x= 420, y=120)
        


    def insert_record(self):
            check_counter=0
            warn = ""

            if self.fullname.get() == "":

                warn = "Please enter your name."
            else:
                check_counter += 1
                
            if self.mobilenum.get() == "":
                warn = "Please enter your contact number."
            else:
                check_counter += 1

            if self.uname.get() == "":
                warn = "Please enter your username."
            else:
                check_counter += 1
            
            if  self.pword.get() == "":
                warn = "Please enter your password."
            else:
                check_counter += 1

            if check_counter == 4:        
                try:
                    conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("INSERT INTO users VALUES (%s,%s,%s,%s,%s)", (
                        self.id.get(),
                        self.fullname.get(),
                        self.mobilenum.get(),
                        self.uname.get(),
                        self.pword.get()

                    ))
                    conn.commit()
                    messagebox.showinfo('Success', 'Sign up success. You may now login')
                    conn.close()
                    self.root.destroy()

                except Exception as ep:
                    messagebox.showerror('', ep) 
            else:
                messagebox.showerror('Error', warn)

    def close(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Registration(root)
    root.mainloop()        