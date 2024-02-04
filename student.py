from email.mime import image
from tkinter import*
from tkinter import ttk
from turtle import bgpic
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")
        
        
        #===variables=====
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
      
        
        
        
        
                # bg image
        img=Image.open(r"images\stbg.jpg")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=200,width=1350,height=600)
        
        
        # left label frame     
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=550)
        
        img_left=Image.open(r"images\4521307.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img_left)

        bg_img=Label(Left_frame,image=self.photoimg1)
        bg_img.place(x=10,y=0,width=650,height=130)
        
        
        
        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=135,width=650,height=110)
        
        # department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # course
        
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","CS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        
        
        # Year
        
        Year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        Year_combo["values"]=("Select Year","2k19","2k20","2k21","2k22")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        
      # Semester
        
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        Semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        # Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=250,width=650,height=290)
        #student id
        StudentID_label=Label(class_student_frame,text="First Name:",font=("times new roman",12,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        StudentName_label=Label(class_student_frame,text="Last Name:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        

         # reg no
        REG_NO_label=Label(class_student_frame,text="REG NO:",font=("times new roman",12,"bold"),bg="white")
        REG_NO_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        REG_NO_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        REG_NO_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        

        # gender
        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        # Mobile num
        Mobile_label=Label(class_student_frame,text="Mobile Num:",font=("times new roman",12,"bold"),bg="white")
        Mobile_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        Mobile_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        Mobile_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # Email
        Email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # adress
        Address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        # Batch
        Batch_label=Label(class_student_frame,text="Batch:",font=("times new roman",12,"bold"),bg="white")
        Batch_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Batch_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        Batch_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        # button frame
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=640,height=40)
        
        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,)
        
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,)    
       
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=225,width=640,height=40) 
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take photo sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,)
        
        
        update_photo_btn=Button(btn_frame1,text="Update photo sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,)
        
        
        
        
        # right label frame     
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=700,y=10,width=600,height=550)
        
        
        img_right=Image.open(r"images\stid.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        bg_img=Label(right_frame,image=self.photoimg1)
        bg_img.place(x=10,y=0,width=650,height=130)
        
        
        
        # =========search system=======
        
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=135,width=580,height=70)
        
        search_label=Label(search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=11)
        Search_combo["values"]=("Select Roll No","Phone No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(search_frame,width=10,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        Search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)
        
        ShowAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)        
        
        #=======table frame======
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=580,height=320)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","roll","gender","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

# ===========function declaration=====


    def add_data(self):
     if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
     else:
          try:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="facerecognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                      
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_std_id.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_radio1.get()
                                                                                        
                                                                                        
                                                                                      )) 
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","Student details has been added Successfuly",parent=self.root)
          except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    # ==========fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="facerecognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                    self.student_table.insert("",END,values=i)
              conn.commit()
        conn.close()             
    
    
    # ===========get cursor==========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_radio1.set(data[11])   
     
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)   
        else:
            try:
                  Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                  if Upadate>0:
                      conn=mysql.connector.connect(host="localhost",username="root",password="",database="facerecognizer")
                      my_cursor=conn.cursor()
                      my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                        
                        
                                                                                                                                  self.var_dep.get(),
                                                                                                                                  self.var_course.get(),
                                                                                                                                  self.var_year.get(),
                                                                                                                                  self.var_semester.get(),
                                                                                                                                  self.var_std_name.get(),
                                                                                                                                  self.var_roll.get(),
                                                                                                                                  self.var_gender.get(),
                                                                                                                                  self.var_email.get(),
                                                                                                                                  self.var_phone.get(),
                                                                                                                                  self.var_address.get(),
                                                                                                                                  self.var_radio1.get(),
                                                                                                                                  self.var_std_id.get()
                                                                                                                                  ))
                  else:
                        if not Upadate:
                              return
                  messagebox.showinfo("Success","Student details successfully update complete",parent=self.root)
                  conn.commit()
                  self.fetch_data()
                  conn.close()
            except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    
    #delete function
    def delete_data(self):
          if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student id must be required",parent=self.root)
          else:
               try:
                   delete=messagebox.askyesno("Student delete Page","Do you want to delete this student",parent=self.root)
                   if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="facerecognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                   else:
                     if not delete:
                       return
                    
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)         
               except Exception as es:
                      messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    
    # reset
    def reset_data(self):
          self.var_dep.set("Select Department")
          self.var_course.set("Select Course") 
          self.var_year.set("Select Year")
          self.var_semester.set("Select Semester")
          self.var_std_id.set("")
          self.var_std_name.set("")
          self.var_roll.set("")
          self.var_gender.set("Male")
          self.var_email.set("")
          self.var_phone.set("")
          self.var_address.set("")
          self.var_radio1.set("")
     
     
     # generate data set take photo sample
    def generate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)   
         else:
              try:
                
                  conn=mysql.connector.connect(host="localhost",username="root",password="",database="facerecognizer")
                  my_cursor=conn.cursor()
                  my_cursor.execute("select * from student")
                  myresult=my_cursor.fetchall()
                  id=0
                  for x in myresult:
                        id+=1
                  my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                        
                        
                                                                                                                                  self.var_dep.get(),
                                                                                                                                  self.var_course.get(),
                                                                                                                                  self.var_year.get(),
                                                                                                                                  self.var_semester.get(),
                                                                                                                                  self.var_std_name.get(),
                                                                                                                                  self.var_roll.get(),
                                                                                                                                  self.var_gender.get(),
                                                                                                                                  self.var_email.get(),
                                                                                                                                  self.var_phone.get(),
                                                                                                                                  self.var_address.get(),
                                                                                                                                  self.var_radio1.get(),
                                                                                                                                  self.var_std_id.get()==id+1
                                                                                                                                  ))
                  conn.commit()
                  self.fetch_data()
                  self.reset_data()
                  conn.close()
                  
                  #======load predefined data on face from frontals from opencv
                  face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                  
                  def face_cropped(img):
                      gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                      faces=face_classifier.detectMultiScale(gray,1.3,5)
                      #scaling factor=1.3
                      #minimum neighbor=5
                      
                      for(x,y,w,h) in faces:
                         face_cropped=img[y:y+h,x:x+w]
                         return face_cropped
                        
                  cap=cv2.VideoCapture(0)
                  img_id=0
                  while True:
                      ret,my_frame=cap.read()
                      if face_cropped(my_frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(my_frame),(450,450))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Croped Face",face)
                       
                      if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                  cap.release()
                  cv2.destroyAllWindows()
                  messagebox.showinfo("Result","Generating data sets completed!!!!")          
              
              except Exception as es:
                      messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           
     
         
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
          

        
         
if __name__ == "__main__":
  root=Tk()
  obj=Student(root)
  root.mainloop()
