from itertools import count
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import os
import numpy as np


class Student_Records:
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

        #DB Connection
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="kaonashi")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM student_information")


        #variables
        self.fullname= StringVar()
        self.program = StringVar()
        self.studentno = StringVar()
        self.studentid = StringVar()
        self.subject = StringVar()
        self.search = StringVar()

        #Icon and Label
        img=Image.open('gui_images\guii.png')
        img=img.resize((60,60), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb2 = Label(self.root, image=self.photoimg, bg="white")
        f_lb2.place(x=40,y=25, width=60,height=60)

        title_lb1 = Label(self.root, text="Student Records",font=("Arial",18),bg="white",fg="#717171")
        title_lb1.place(x=105,y=40,width=220,height=33)


        #=======Labels and Textboxes

        title_label = Label(self.root, text="Student Details",font=("Corbel Light",16,"normal"),bg="white",fg="#505050")
        title_label.place(x=40, y=115, width=130, height =20)

        #StudentID
        studentid_label = Label(self.root, text="Student ID",font=("Arial",11,"normal"),bg="white",fg="#717171")
        studentid_label.place(x=40, y=155, width=79, height =18)
        studentid_entry = Entry(self.root,textvariable=self.studentid,bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",11,"normal"), relief=RIDGE, state="disabled")
        studentid_entry.place(x=40, y=175, width=300, height=30)
        

        #StudentNo 
        studentno_label = Label(self.root, text="Student No.",font=("Arial",11,"normal"),bg="white",fg="#717171")
        studentno_label.place(x=40, y=210, width=79, height =18)
        studentno_entry = Entry(self.root,textvariable=self.studentno, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",11,"normal"), relief=RIDGE)
        studentno_entry.place(x=40, y=235, width=300, height=30)
        
       
        #full name
        fullname_label = Label(self.root, text="Full Name",font=("Arial",11,"normal"),bg="white",fg="#717171")
        fullname_label.place(x=40, y=275, width=79, height =20)
        fullname_entry = Entry(self.root, textvariable=self.fullname, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",11,"normal"), relief=RIDGE)
        fullname_entry.place(x=40, y=295, width=300, height=30)
        
        #Program
        program_label = Label(self.root, text="Program",font=("Arial",12,"normal"),bg="white",fg="#717171")
        program_label.place(x=40, y=335, width=76, height =20)
        program_entry = Entry(self.root, textvariable=self.program, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        program_entry.place(x=40, y=355, width=300, height=30)

        #Subject
        subject_label = Label(self.root, text="Subject",font=("Arial",12,"normal"),bg="white",fg="#717171")
        subject_label.place(x=40, y=395, width=76, height =20)
        subject_entry = Entry(self.root, textvariable=self.subject, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        subject_entry.place(x=40, y=415, width=300, height=30)

        take_photo_btn = Button(self.root, text="Capture Images", command=self.generate_dataset, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        take_photo_btn.place(x=40,y=460,width=300,height=30)

        train_photo_btn = Button(self.root, text="Train Images", command=self.train_classifier, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        train_photo_btn.place(x=40,y=500,width=300,height=30)

        open_photo_btn = Button(self.root, text="Open Files", command=self.faceData, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        open_photo_btn.place(x=40,y=540,width=300,height=30)
    
        clear_btn = Button(self.root, text="Clear", command=self.clearBtn, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        clear_btn.place(x=475,y=580,width=116,height=30)
       
        save_btn = Button(self.root, text="Save", command=self.add_data, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        save_btn.place(x=600,y=580,width=116,height=30)
        
        update_btn = Button(self.root, text="Update",command=self.update_data, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        update_btn.place(x=725,y=580,width=116,height=30)

        delete_btn = Button(self.root, text="Delete",command=self.delete_data, cursor="hand2",font=("Arial",12,"normal"),bg="#FF6E54",fg="white", bd=0)
        delete_btn.place(x=850,y=580,width=116,height=30)
        
        

        #SearchTextBox
        search_entry = Entry(self.root, textvariable=self.search, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        search_entry.place(x=380, y=175, width=470, height=30)

        #SearchButton
        search_btn = Button(self.root, text="Search",command=self.search_data,cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        search_btn.place(x=850,y=175,width=116,height=30)
        
#=============FOR DATAGRIDVIEW=========================

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 10))

        self.table_tree = ttk.Treeview(self.root)
        self.table_tree.place(x=380,y=220,width=585,height=350)
        scroll_x = ttk.Scrollbar(self.table_tree,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.table_tree,orient=VERTICAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.table_tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.table_tree.configure(selectmode="extended")
        
        scroll_x.configure(command=self.table_tree.xview)
        scroll_y.configure(command=self.table_tree.yview)

        self.table_tree.configure(
            columns=(
                "ID",
                "Student_No",
                "Full_Name",
                "Program",
                "Subject"
            )
        )

        #Headings
        self.table_tree.heading("ID",text="ID", anchor=W)
        self.table_tree.heading("Student_No",text="Student No.", anchor=W)
        self.table_tree.heading("Full_Name",text="Full Name", anchor=W)
        self.table_tree.heading("Program",text="Program", anchor=W)
        self.table_tree.heading("Subject",text="Subject", anchor=W)


        #Column Format
        self.table_tree.column('#0', stretch=NO, minwidth=25, width=0)
        self.table_tree.column('#1', stretch=NO, minwidth=0, width=85)
        self.table_tree.column('#2', stretch=NO, minwidth=0, width=130)
        self.table_tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.table_tree.column('#4', stretch=NO, minwidth=0, width=100)

        #Display Data into Treeview        
        global count
        count = 0

        for record in mycursor:
                self.table_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4]))
                count += 1

        self.table_tree.bind("<ButtonRelease>",self.get_cursor)


#=============FUNCTIONS FOR BUTTONS====================

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
        mycursor = conn.cursor()
        mycursor.execute("select * from student_information")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.table_tree.delete(*self.table_tree.get_children())
            for i in data:
                self.table_tree.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus = self.table_tree.focus()
        content = self.table_tree.item(cursor_focus)
        data = content["values"]

        self.studentid.set(data[0])
        self.studentno.set(data[1]),
        self.fullname.set(data[2]),
        self.program.set(data[3]),
        self.subject.set(data[4])

    #SAVE BUTTON

    def add_data(self):
        if self.program.get()=="" or self.studentno.get()=="":
            messagebox.showerror("Error","Fill in all required fields.",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student_information values(%s,%s,%s,%s,%s)",(
                self.studentid.get(),
                self.studentno.get(),
                self.fullname.get(),
                self.program.get(),
                self.subject.get()
                     ))

                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                messagebox.showinfo("Success","All records are saved.",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to: {str(e)}",parent=self.root)

    def update_data(self):
            if self.program.get()=="" or self.studentno.get()=="":
                messagebox.showerror("Error","Fill in all required fields.",parent=self.root)
            else:
                try:
                    Update=messagebox.askyesno("Warning","Do you want to save changes?",parent=self.root)
                    if Update > 0:
                        conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)                        
                        mycursor = conn.cursor()
                        mycursor.execute("UPDATE student_information SET student_no=%s,full_name=%s,program=%s, subject=%s where student_id=%s",(
                        self.studentno.get(), 
                        self.fullname.get(),
                        self.program.get(),
                        self.subject.get(),
                        self.studentid.get()
                        ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success","Changes saved.",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    self.reset()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                    
                    
    def delete_data(self):
        if self.studentno.get()=="":
            messagebox.showerror("Error","No selection made.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete selected items?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)                        
                    mycursor = conn.cursor()
                    sql="delete from student_information where student_id=%s"
                    val=(self.studentid.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

               
                messagebox.showinfo("Delete","Item deleted successfully.",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    def search_data(self):
        if self.search.get()=="":
            messagebox.showerror("Error", "Item not specified.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM student_information where last_name LIKE '%"+self.search.get()+"%' OR student_no LIKE '%"+self.search.get()+"%' OR full_name LIKE '%"+self.search.get()+"%'")
                row = mycursor.fetchall()
                if len(row)>0:
                    self.table_tree.delete(*self.table_tree.get_children())
                    for i in row:
                        self.table_tree.insert('',END, values=i)
                else:
                    self.table_tree.delete(*self.table_tree.get_children())
            except Exception as e:   
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def disable_entry(self):
        Entry.config(state= "disabled")

    def hide_entry(self):
        self.pack_forget()

    def reset(self):
        self.studentid.set(""),
        self.studentno.set(""),
        self.fullname.set(""), 
        self.program.set(""),
        self.subject.set(""),
        self.search.set("")
        
    def clearBtn(self):
        self.reset()
        self.fetch_data()

    def faceData(self):
        os.startfile("data_img")

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset complete.",parent=self.root) 

    # ==================================Generate Data set=========================
    def generate_dataset(self):
        if self.program.get()=="" or self.studentno.get()=="":
            messagebox.showerror("Error","Fill in all required fields.",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM student_information ")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("UPDATE student_information SET student_no=%s,full_name=%s,program=%s,subject=%s where student_id=%s",( 
                    self.studentno.get(),
                    self.fullname.get(),
                    self.program.get(),
                    self.subject.get(),
                    self.studentid.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/stdudent."+str(self.studentid.get())+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

if __name__ == "__main__":
    root=Tk()
    obj=Student_Records(root)
    root.mainloop()