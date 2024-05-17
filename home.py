import os
from cProfile import label
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from attendancerecords import Attendance_Records
from studentrecords import Student_Records
from facerecognition import Face_Recognition
import time
from datetime import date
from tkinter import messagebox
import mysql.connector
import numpy as np
import cv2

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recognition System")
        self.root.configure(bg='#EFF5F6')
        self.root.resizable(width=False, height=False)

        app_width = 1000
        app_height = 650

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)

        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}') 

       #==============================SIDEBAR==========================
        
        

        panel = Frame(self.root, bg="white")
        panel.place(x=0,y=0, width=245, height=650)


        img=Image.open('gui_images\guii.png')
        img=img.resize((140,147), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1 = Label(panel, image=self.photoimg, bg="white")
        f_lb1.place(x=55,y=15)


        
        #Student Records Button
        std_b1_1 = Button(panel, text="Student Records", command=self.studentList,cursor="hand2",font=("Arial",12,"normal"),bg="white",fg="#B779B9",bd=0, anchor=W)
        std_b1_1.place(x=30,y=200,width=200,height=40)

        #Face Recognition Button
        facerec_bt1 = Button(panel, text="Face Recognition",command = self.faceRecognition, cursor="hand2",font=("Arial",12,"normal"),bg="white",fg="#B779B9",bd=0, anchor=W)
        facerec_bt1.place(x=30,y=240,width=200,height=40)

        #Attendance Button
        records_bt1 = Button(panel, text="Attendance Records",command=self.attendanceRecords,cursor="hand2",font=("Arial",12),bg="white",fg="#B779B9",bd=0, anchor=W)
        records_bt1.place(x=30,y=280,width=200,height=40)

        #Log Out Button
        logout_bt1 = Button(panel, text="Log Out",command=self.close, cursor="hand2",font=("Arial",12),bg="white",fg="#FF6E54",bd=0, anchor=W)
        logout_bt1.place(x=30,y=600,width=200,height=40)

    
        #================================MAIN PAGE===================================

        paneltop = Frame(self.root, bg="#B779B9")
        paneltop.place(x=246,y=0,width=754,height=30)
        
        title_lb1 = Label(self.root, text="Home",font=("Arial",20, "bold"),bg="#EFF5F6",fg="#B779B9")
        title_lb1.place(x=275,y=45,width=90,height=38)

        time_panel = Frame(self.root, bg="white")
        time_panel.place(x=280, y=95, width=670, height=155)

        
        img2=Image.open('gui_images\clock.jpg')
        img2=img2.resize((115,115), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb2 = Label(time_panel, image=self.photoimg2, bg="white")
        f_lb2.place(x=25,y=17)
        
        
        today = date.today()
        f_today = today.strftime("%B %d, %Y")
        dayname = today.strftime("%A")

        date_label = Label(time_panel, text=f'Today is {f_today}',font=("Arial",16), bg="white", fg="#B779B9", anchor=W)
        date_label.place(x=170, y=40, width=290, height =30)

        daylabel = Label(time_panel, text=f'{dayname}',font=("Arial",16), bg="white", fg="#B779B9", anchor=W)
        daylabel.place(x=170, y=70, width=150, height =30)

        time_label = Label(time_panel, font=("Arial",16), bg="white", fg="#B779B9", anchor = W)
        time_label.place(x=170, y=105, width=135, height =20)

        def mytime():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm = time.strftime("%p")

            time_label.config(text=hour + ":" + minute + ":"+ second + " " + am_pm)
            time_label.after(200,mytime)

        mytime()


        title_lb2 = Label(self.root, text="Information",font=("Arial",20, "bold"),bg="#EFF5F6",fg="#B779B9")
        title_lb2.place(x=280,y=280,width=150,height=38)

        student_panel = Frame(self.root, bg="white")
        student_panel.place(x=280, y=335, width=230, height=175)

        stdpanel_label = Label(student_panel, text="Total Students", font=("Arial",12, "bold"), bg="white",fg="#B779B9")
        stdpanel_label.place(x=60, y=35, width=110, height=12)

        img3=Image.open('gui_images\student.png')
        img3=img3.resize((45,45), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lb3 = Label(student_panel, image=self.photoimg3, bg="white")
        f_lb3.place(x=60,y=75)


        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="kaonashi")
        mycursor = mysqldb.cursor()
        mycursor.execute("Select *  from student_information")
        rows=mycursor.fetchall()

        res = 0
        for i in rows:
            res+=1

        number_label = Label(student_panel, text=res, font=("Arial",20, "bold"), bg="white",fg="#B779B9")
        number_label.place(x=110, y=90, width=50,height=25)

        #====================================================================================

        attendance_panel = Frame(self.root, bg="white")
        attendance_panel.place(x=540, y=335, width=230, height=175)

        stdpanel_label = Label(attendance_panel, text="Attendance Records", font=("Arial",12, "bold"), bg="white",fg="#B779B9")
        stdpanel_label.place(x=40, y=35, width=155, height=12)

        img4=Image.open('gui_images\checkbox.png')
        img4=img4.resize((45,45), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lb4 = Label(attendance_panel, image=self.photoimg4, bg="white")
        f_lb4.place(x=55,y=75)


        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="kaonashi")
        mycursor = mysqldb.cursor()
        mycursor.execute("Select *  from attendance_records")
        rows=mycursor.fetchall()

        res = 0
        for i in rows:
            res+=1

        number_label = Label(attendance_panel, text=res, font=("Arial",20, "bold"), bg="white",fg="#B779B9")
        number_label.place(x=110, y=90, width=50,height=25)



#FUNCTION FOR BUTTONS
    def studentList(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Records(self.new_window)
        
    
    def faceRecognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendanceRecords(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Records(self.new_window)

    def close(self):
        answer=messagebox.askyesno("Log Out","Do you want to log out?",parent=self.root)
        if answer> 0:
            (
            self.root.destroy()
            )
        else:
            if answer <0:
                return

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()