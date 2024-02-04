from tkinter import*
from tkinter import ttk
from turtle import bgpic
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")
        
        
        img3=Image.open(r"images\devi.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
 root=Tk()
 obj=developer(root)
 root.mainloop()
