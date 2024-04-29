from tkinter import*
from PIL import Image,ImageTk
from course import courseclass
from student import StudentClass
from result import resultclass
from report import reportclass
from tkinter import messagebox
import os 
from PIL import Image, ImageTk , ImageDraw 
import sqlite3 
from tkinter import messagebox , ttk
import time
import math

class RMS:
    def __init__(self, root) :
        self.root=root
        self.root.title("Student result system")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #=================title=========================#
        title= Label(self.root,text="Student Success Hub ",padx=50,compound=LEFT, font=("goudy old style",25,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
      
        #==================icons========================#
       # self.logo_dash = ImageTk.PhotoImage(file="image/Result.jpg")
       # image=self.logo_dash   -------> if need to use the image to top of the web then place this sent to title after compound


       #===================menu========================#
        M_Frame= LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1520,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=300,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=580,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=860,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1140,y=5,width=200,height=40)
        btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1400,y=5,width=100,height=40)

        #=====================content_window==========================================#
        self.bg_img=Image.open("image/s.jpg")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=1000,height=430)

        self.g_img=Image.open("image/G.jpg")
        self.g_img=self.g_img.resize((400,350),Image.ANTIALIAS)
        self.g_img=ImageTk.PhotoImage(self.g_img)

        self.lbl_g=Label(self.root,image=self.g_img).place(x=0,y=180,width=500,height=430)


        
        #===============update_details===============================#
        self.lbl_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=580,width=300,height=100)

        self.lbl_Student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_Student.place(x=740,y=580,width=300,height=100)

        self.lbl_Result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ab",fg="white")
        self.lbl_Result.place(x=1080,y=580,width=300,height=100)
#--------------------------------------------------------------------------------------------------=--------------------------------
#=================================================================================================================footer=========================#
        footer= Label(self.root,text="www.sanjivanicoe.org.in",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
#====================================================================================================================
    def update_details(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")
            #self.lbl_course.after(200,self.update_details)
            
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_Student.config(text=f"Total Student\n[{str(len(cr))}]")
            #self.lbl_Student.after(200,self.update_details)
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_Result.config(text=f"Total Result\n[{str(len(cr))}]")
            #self.lbl_Result.after(200,self.update_details)
            
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseclass(self.new_win)
   
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultclass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportclass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("Python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
           


if __name__=="__main__" :
    root = Tk()
    obj=RMS(root)
    root.mainloop()
