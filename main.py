from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import bgpic
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developers import developer
from help import help


class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")
        
     
        
        
        
        # bg image
        img=Image.open(r"images\bg img.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        #time
        
        


        # student button
        img1=Image.open(r"images\stu.jpg")
        img1=img1.resize((220,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=230,width=220,height=150)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=370,width=220,height=40)




  # detect face button
        img2=Image.open(r"images\ty.webp")
        img2=img2.resize((220,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        b1=Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=230,width=220,height=150)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=370,width=220,height=40)
      

 # attendence button
        img3=Image.open(r"images\att.jpg")
        img3=img3.resize((220,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        b1=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.attendence_data)
        b1.place(x=700,y=230,width=220,height=150)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=370,width=220,height=40)




 # help button
        img4=Image.open(r"images\help.webp")
        img4=img4.resize((220,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=230,width=220,height=150)
        
        b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=370,width=220,height=40)



 # train face button
        img5=Image.open(r"images\train.jpeg")
        img5=img5.resize((220,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=500,width=220,height=150)
        
        b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=650,width=220,height=40)



 # photos button
        img6=Image.open(r"images\photo.webp")
        img6=img6.resize((220,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)


        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=500,width=220,height=150)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=650,width=220,height=40)



 # developers button
        img7=Image.open(r"images\dev.jpg")
        img7=img7.resize((220,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)


        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=500,width=220,height=150)
        
        b1_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=650,width=220,height=40)


 # EXIt button
        img8=Image.open(r"images\exit.png")
        img8=img8.resize((220,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)


        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=500,width=220,height=150)
        
        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=650,width=220,height=40)

    def open_img(self):
        os.startfile("data")
        
        
    def iExit(self):
           self.iExit=messagebox.askyesno("Face Recognition","Are you sure exit this project")
           if self.iExit >0:
              self.root.destroy()
           else:
                return         
                     



       # =================function buttons===============
       
    def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)
       
       
       
       
       
    def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)
       
       
       
    def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_Recognition(self.new_window)
              
        
    def attendence_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Attendence(self.new_window)
       
       
       
       
    def developer_data(self):
       self.new_window=Toplevel(self.root)
       self.app=developer(self.new_window)
       
       
       
       
    def help_data(self):
       self.new_window=Toplevel(self.root)
       self.app=help(self.new_window)   































if __name__ == "__main__":
  root=Tk()
  obj=Face_Recognition_system(root)
  root.mainloop()




