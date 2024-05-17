from cProfile import label
from ctypes import alignment
from tkinter import*
from tkinter import ttk
from tokenize import String
from turtle import width
from PIL import Image,ImageTk
import cv2
import mysql.connector
from datetime import datetime
import os

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

class Face_Recognition:
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

        img=Image.open('gui_images\guii.png')
        img=img.resize((60,60), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb2 = Label(self.root, image=self.photoimg, bg="#EFF5F6")
        f_lb2.place(x=40,y=25, width=60,height=60)

        title_lb1 = Label(self.root, text="Face Recognition",font=("Arial",18),bg="#EFF5F6",fg="#717171")
        title_lb1.place(x=105,y=40,width=220,height=33)

        attendance_panel = Frame(self.root, bg="white")
        attendance_panel.place(x=80, y=110, width=355, height=220)

        img2=Image.open('gui_images\\facerec.png')
        img2=img2.resize((95,95), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1 = Label(attendance_panel, image=self.photoimg2, bg="white")
        f_lb1.place(x=40,y=40)

        attendance_label = Label(attendance_panel, text="Face Recognition", font=("Arial",14, "bold"), bg="white",fg="#717171")
        attendance_label.place(x=150, y=50, width=160, height=25)

        attendance_label2 = Label(attendance_panel, text="Click here to take \n attendance", font=("Arial",12), bg="white",fg="#717171")
        attendance_label2.place(x=150, y=80, width=160, height=58)

        attendance_button = Button(attendance_panel, text="Take Attendance",command= self.face_recog, cursor="hand2",font=("Arial",12,"bold"),bg="#B779B9",fg="white",bd=0)
        attendance_button.place(x=0, y=180, width=355, height=40)

        directory_panel = Frame(self.root, bg="white")
        directory_panel.place(x=80, y=360, width=355, height=220)

        img3=Image.open('gui_images\\folder.png')
        img3=img3.resize((95,95), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lb3 = Label(directory_panel, image=self.photoimg3, bg="white")
        f_lb3.place(x=40,y=40)

        directory_label = Label(directory_panel, text="Attendance List", font=("Arial",14, "bold"), bg="white",fg="#717171")
        directory_label.place(x=150, y=50, width=160, height=25)

        directory_label2 = Label(directory_panel, text="Click here to locate \n CSV file", font=("Arial",12), bg="white",fg="#717171")
        directory_label2.place(x=150, y=80, width=160, height=58)

        directory_button = Button(directory_panel, text="Locate File", command=self.locateFolder,cursor="hand2",font=("Arial",12,"bold"),bg="#B779B9",fg="white",bd=0)
        directory_button.place(x=0, y=180, width=355, height=40)

        img4=Image.open('gui_images\\guii.png')
        img4=img4.resize((375,375), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lb4 = Label(self.root, image=self.photoimg4, bg="#EFF5F6")
        f_lb4.place(x=540,y=135)

    #=======================================================================================
    
    def locateFolder(self):
        os.startfile("attendance")


    def mark_attendance(self,i,n,o):
        now = datetime.now().strftime('%m-%d-%Y')
        csvname = 'attendance//Attendance_' + now + '.csv'
        if os.path.exists(csvname):
            with open(csvname, 'r+', newline= '\n') as f:
                DataList = f.readlines()
                knownNames = []
                for data in DataList:
                    ent = data.split(',')
                    knownNames.append(ent[1])

            with open(csvname, 'a+', newline= '\n') as f:
                if((i not in knownNames)) and ((n not in knownNames)):
                    now=datetime.now()
                    d1=now.strftime("%m/%d/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f'{""},{i}, {n}, {o}, Present, {dtString}, {d1}\n')
        else:
            open(csvname, 'w')

            #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(user='root', password='',host='localhost',database='kaonashi',port=3306)
                cursor = conn.cursor()

                cursor.execute("SELECT full_name FROM student_information where student_id="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select student_no from student_information where student_id="+str(id))
                i=cursor.fetchone()
                i="+".join(i)

                cursor.execute("select subject from student_information where student_id="+str(id))
                o=cursor.fetchone()
                o="+".join(o)


                if confidence > 82:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Student No:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Subject:{o}",(x,y-105),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,n,o)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()       