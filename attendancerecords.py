from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import os
import csv
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib import colors

mydata=[]

class Attendance_Records:
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
        
        #variables
        self.id = StringVar()
        self.studNo = StringVar()
        self.fullname = StringVar()
        self.subject = StringVar()
        self.status = StringVar()
        self.time = StringVar()
        self.date = StringVar()
        self.search = StringVar()

        #Logo
        img=Image.open('gui_images\guii.png')
        img=img.resize((60,60), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb2 = Label(self.root, image=self.photoimg, bg="white")
        f_lb2.place(x=40,y=25, width=60,height=60)

        title_lb1 = Label(self.root, text="Attendance Records",font=("Arial",18),bg="white",fg="#717171")
        title_lb1.place(x=105,y=40,width=240,height=33)

        #DB Connection
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="kaonashi")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM attendance_records")


        #============GUI====================

        #ID
        studNo_label = Label(self.root, text="Attendance ID",font=("Arial",12,"normal"),bg="white",fg="#717171")
        studNo_label.place(x=40, y=115, width=112, height =17)
        studNo_entry = Entry(self.root, textvariable=self.id, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        studNo_entry.place(x=40, y=135, width=340, height=35)

        #Student Number 
        studNo_label = Label(self.root, text="Student Number",font=("Arial",12,"normal"),bg="white",fg="#717171")
        studNo_label.place(x=40, y=175, width=112, height =17)
        studNo_entry = Entry(self.root, textvariable=self.studNo, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        studNo_entry.place(x=40, y=195, width=340, height=35)


        #Full Name
        fullname_label = Label(self.root, text="Full Name",font=("Arial",12,"normal"),bg="white",fg="#717171")
        fullname_label.place(x=40, y=235, width=79, height =20)
        fullname_entry = Entry(self.root,textvariable=self.fullname, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        fullname_entry.place(x=40, y=255, width=340, height=35)

        #Subject
        subject_label = Label(self.root, text="Subject",font=("Arial",12,"normal"),bg="white",fg="#717171")
        subject_label.place(x=40, y=295, width=60, height =20)
        subject_entry = Entry(self.root,textvariable=self.subject, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        subject_entry.place(x=40, y=315, width=340, height=35)


        #Time
        time_label = Label(self.root, text="Time",font=("Arial",12,"normal"),bg="white",fg="#717171")
        time_label.place(x=40, y=355, width=40, height =17)
        time_entry = Entry(self.root, textvariable=self.time, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        time_entry.place(x=40, y=375, width=340, height=35)

        #Date
        date_label = Label(self.root, text="Date",font=("Arial",12,"normal"),bg="white",fg="#717171")
        date_label.place(x=40, y=415, width=40, height =17)
        date_entry = DateEntry(self.root, selectmode='day', date_pattern='mm/dd/yyyy',textvariable=self.date, bg="#F2F2F2", fg="#717171", bd=0, font=("Poppins",12,"normal"), relief=RIDGE)
        date_entry.place(x=40, y=435, width=340, height=35)

        #Attendance Status
        status_label = Label(self.root, text="Attendance Status",font=("Arial",12,"normal"),bg="white",fg="#717171")
        status_label.place(x=40, y=475, width=130, height =20)
        status_combo=ttk.Combobox(self.root, textvariable=self.status,width=127,font=("Arial",12,"normal"),state="readonly")
        status_combo.place(x=40, y=495, width = 340, height=35)

        add_btn = Button(self.root, text="Add",cursor="hand2",command=self.add_data,font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        add_btn.place(x=40,y=550,width=110,height=40)

        update_btn = Button(self.root, text="Update",cursor="hand2",command=self.update_data,font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        update_btn.place(x=158,y=550,width=110,height=40)

        delete_btn = Button(self.root, text="Delete",cursor="hand2",command=self.delete_data,font=("Arial",12,"normal"),bg="#FF6E54",fg="white",bd=0)
        delete_btn.place(x=275,y=550,width=110,height=40)

        import_btn = Button(self.root, text="Import CSV", command=self.importCsv, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        import_btn.place(x=673,y=100,width=150,height=30)

        save_btn = Button(self.root, text="Save", command=self.saveCSVData, cursor="hand2",font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        save_btn.place(x=830,y=100,width=116,height=30)

        #SearchTextBox
        search_entry = Entry(self.root, textvariable=self.search, bg="#F2F2F2", fg="#717171", bd=0, font=("Arial",12,"normal"), relief=RIDGE)
        search_entry.place(x=430, y=139, width=400, height=35)

        #SearchButton
        search_btn = Button(self.root, text="Search",cursor="hand2",command=self.search_data,font=("Arial",12,"normal"),bg="#B779B9",fg="white",bd=0)
        search_btn.place(x=830,y=139,width=116,height=35)

        #=============FOR DATAGRIDVIEW=========================
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 10))

        self.table_tree = ttk.Treeview(self.root)
        self.table_tree.place(x=430,y=195,width=520,height=390)
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
                "Attendance_ID",
                "Student_No",
                "Full_Name",
                "Subject",
                "Status",
                "Time",
                "Date",
            )
        )

         #Headings
        self.table_tree.heading("Attendance_ID",text="ID", anchor=W)
        self.table_tree.heading("Student_No",text="Student No.", anchor=W)
        self.table_tree.heading("Full_Name",text="Full Name", anchor=W)
        self.table_tree.heading("Subject",text="Subject", anchor=W)
        self.table_tree.heading("Status",text="Status", anchor=W)
        self.table_tree.heading("Time", text="Time", anchor=W)
        self.table_tree.heading("Date", text="Date", anchor=W)
        
                #Column Format
        self.table_tree.column('#0', stretch=NO, minwidth=25, width=0)
        self.table_tree.column('#1', stretch=NO, minwidth=0, width=50)
        self.table_tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.table_tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.table_tree.column('#4', stretch=NO, minwidth=0, width=190)
        self.table_tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.table_tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.table_tree.column('#7', stretch=NO, minwidth=0, width=100)
      

        global count
        count = 0

        for record in mycursor:
                self.table_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
                count += 1

        self.table_tree.bind("<ButtonRelease>",self.get_cursor)

    #=======================FUNCTIONS=================================
    #SAVE DATA
    def add_data(self):
        if self.time.get()=="" or self.date.get()=="":
            messagebox.showerror("Error","Fill in all required fields.",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into attendance_records values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.id.get(),
                    self.studNo.get(),
                    self.fullname.get(),
                    self.subject.get(),
                    self.status.get(),
                    self.time.get(),
                    self.date.get(),
                     ))

                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                messagebox.showinfo("Success","All records are saved.",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to: {str(e)}",parent=self.root)

    #UPDATE DATA
    def update_data(self):
            if self.time.get()=="" or self.date.get()=="" or self.status.get()=="":
                messagebox.showerror("Error","Fill in all required fields.",parent=self.root)
            else:
                try:
                    Update=messagebox.askyesno("Warning","Do you want to save changes?",parent=self.root)
                    if Update > 0:
                        conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)                        
                        mycursor = conn.cursor()
                        mycursor.execute("UPDATE attendance_records SET student_no=%s,full_name=%s, subject=%s,attendance_status=%s,time=%s,date=%s where attendance_id=%s",( 
                        self.studNo.get(),
                        self.fullname.get(),
                        self.subject.get(),
                        self.status.get(),
                        self.time.get(),
                        self.date.get(),
                        self.id.get(),
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

    #DELETE BUTTON
    def delete_data(self):
        if self.id.get()=="":
            messagebox.showerror("Error","No selection made.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete selected items?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)                        
                    mycursor = conn.cursor()
                    sql="delete from attendance_records where attendance_id=%s"
                    val=(self.id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                messagebox.showinfo("Delete","Item deleted successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

#=======================================================

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
        mycursor = conn.cursor()
        mycursor.execute("select * from attendance_records")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.table_tree.delete(*self.table_tree.get_children())
            for i in data:
                self.table_tree.insert("",END,values=i)
            conn.commit()
        conn.close()

    def reset(self):
        self.id.set(""),
        self.studNo.set(""),
        self.fullname.set(""),
        self.subject.set(""),
        self.status.set("Present"),
        self.time.set(""),
        self.date.set(""),

    def get_cursor(self,event=""):
            cursor_focus = self.table_tree.focus()
            content = self.table_tree.item(cursor_focus)
            data = content["values"]
            
            self.id.set(data[0])
            self.studNo.set(data[1]),
            self.fullname.set(data[2]),
            self.subject.set(data[3]),
            self.status.set(data[4]),
            self.time.set(data[5]),
            self.date.set(data[6])

    def fetchCSVData(self,rows):
        self.table_tree.delete(*self.table_tree.get_children())
        for i in rows:
            self.table_tree.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        global fln
        fln =filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchCSVData(mydata)

    def saveCSVData(self):
            if messagebox.askyesno("Save Data?", "Do you want to save this?"):
                mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="kaonashi")
                mycursor = mysqldb.cursor()
                with open(fln) as myfile:
                    csvread=csv.reader(myfile,delimiter=",")
                    all_value = []
                    for row in csvread:
                        value =(row[0],row[1],row[2],row[3],row[4],row[5], row[6])
                        all_value.append(value)
                query = "INSERT INTO attendance_records(`attendance_id`, `student_no`, `full_name`,`subject`, `attendance_status`, `time`, `date`) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                mycursor.executemany(query, all_value)
                mysqldb.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Data saved successfully.")
            else:
                return False
    
    def search_data(self):
        if self.search.get()=="":
            messagebox.showerror("Error", "Item not specified.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM attendance_records where full_name LIKE '%"+self.search.get()+"%' OR student_no LIKE '%"+self.search.get()+"%' OR date LIKE '%"+self.search.get()+"%' OR time LIKE '%"+self.search.get()+"%'")
                row = mycursor.fetchall()
                if len(row)>0:
                    self.table_tree.delete(*self.table_tree.get_children())
                    for i in row:
                        self.table_tree.insert('',END, values=i)
                else:
                    self.table_tree.delete(*self.table_tree.get_children())
            except Exception as e:   
                messagebox.showerror("Error", f"Error due to {str(e)}")
         

if __name__ == "__main__":
    root=Tk()
    obj=Attendance_Records(root)
    root.mainloop()