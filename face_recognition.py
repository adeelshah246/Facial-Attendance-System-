from tkinter import*
from tkinter import ttk
from turtle import bgpic
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")
        
        
        
        
        img3=Image.open(r"images\lums.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        
        
        # button
        b1_1=Button(bg_img,text="Face Recognizer",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=690,y=720,width=200,height=40)
    
    # attendence
    def  mark_attendence(self,r,n,d):
         with open("Alpha.csv","r+",newline="\n") as f:
             myDataList=f.readlines()
             name_list=[]
             for line in myDataList:
                 entry=line.split((","))
                 name_list.append(entry[0])
             if((r not in name_list) and (n not in name_list) and (d not in name_list)  ):
                 now=datetime.now()
                 d1=now.strftime("%d/%m/%Y")
                 dtstring=now.strftime("%H:%M:%S")
                 f.writelines(f"\n{r},{n},{d},{dtstring},{d1},Present")
                    
             
    
        
        
        
        
    #  face recognition
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+y,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="facerecognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                
                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendence(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+y,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,y]
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                           
                    
                        
        
                
if __name__ == "__main__":
  root=Tk()
  obj=Face_Recognition(root)
  root.mainloop()        