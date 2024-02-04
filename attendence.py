from tkinter import*
from tkinter import ttk
from turtle import bgpic
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")
        
        
        # variables
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()
        
        
        img3=Image.open(r"images\ats.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=230,width=1350,height=550)
        
         # left label frame     
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=550)
        
        img_left=Image.open(r"images\4521307.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img_left)
        
        bg_img=Label(Left_frame,image=self.photoimg1)
        bg_img.place(x=10,y=0,width=650,height=130)
        
        leftinside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        leftinside_frame.place(x=0,y=135,width=660,height=370) 
        
        # label entry
        
        #Attendance id
        attendanceID_label=Label(leftinside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(leftinside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #name
        roll_label=Label(leftinside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(leftinside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,pady=8)
        
        
        #date
        name_label=Label(leftinside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        name_entry=ttk.Entry(leftinside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=8)
        
        
        #Department
        deplabel=Label(leftinside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        deplabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        depentry=ttk.Entry(leftinside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        depentry.grid(row=1,column=3,pady=8)
        
        
        
        #time
        time_label=Label(leftinside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(leftinside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,pady=8)
        
        
        #date
        Date_label=Label(leftinside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Date_entry=ttk.Entry(leftinside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        Date_entry.grid(row=2,column=3,pady=8)
        
        # attendance
        Attendance_label=Label(leftinside_frame,text="Attendance status",font=("comicsansna 11 bold"),bg="white")
        Attendance_label.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(leftinside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        # button frame
        btn_frame=Frame(leftinside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=640,height=40)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,)
        
        
        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data_,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,)
        
        
        
        
        
        
        
        
        
        
        # right label frame     
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=700,y=10,width=600,height=550)
        
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=590,height=455)
        
        # scroll bar table
        
        scrol_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)
        
        scrol_x.config(command=self.AttendanceReportTable.xview)
        scrol_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
        
        
     # fetch data
     
     
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    # import csv        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
        
        
     # export csv
     
     
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                            
    
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()   
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0]) 
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])
        
        
        
    def reset_data_(self):
        cursor_row=self.AttendanceReportTable.focus()   
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set("") 
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")    
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()