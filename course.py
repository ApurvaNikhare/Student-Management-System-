from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class courseclass:
    def __init__(self, root) :
        self.root=root
        self.root.title("Student result system")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=================title=========================#
        title = Label(self.root,text="Manage Course Detail",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1520,height=35)

        #==========================variable============================#
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_credits=StringVar()
         
        #=================== widget ======================#
        lbl_coursename=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_Duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=160)
        lbl_Credits=Label(self.root,text="Credits",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        lbl_Description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=280)

        #======================= Entry field =================================#

        self.txt_coursename = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_coursename.place(x=150, y=100, width=200)
        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_duration.place(x=150, y=160, width=200)
        self.txt_charges = Entry(self.root, textvariable=self.var_credits, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_charges.place(x=150, y=220, width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=280,width=500,height=180)

        #========================== Bottons =============================#

        self.btn_add=Button(self.root,text="Save", font= ("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=480,width=110,height=40)

        self.btn_update=Button(self.root,text="Update", font= ("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=480,width=110,height=40)

        self.btn_delete=Button(self.root,text="Delete", font= ("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=480,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear", font= ("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=480,width=110,height=40)

        #===================== search panel ==============================#
        self.var_search=StringVar()
        lbl_search_course=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=100)
        self.txt_search_coursename = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=100, width=180)
        btn_search=Button(self.root,text="Search", font= ("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=100,width=120,height=28)

        #=================== content ===========================#
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720,y=200,width=470,height=400)

        scrolly = Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid", "Name","Duration","Credits", "Description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)


        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("Duration",text="Duration")
        self.CourseTable.heading("Description",text="Description")
        self.CourseTable.heading("Credits",text="Credits")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("Name",width=150)
        self.CourseTable.column("Duration",width=150)
        self.CourseTable.column("Credits",width=150)
        self.CourseTable.column("Description",width=200)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#================================================clear button ====================================================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_credits.set("")
        self.var_search.set("")
        self.txt_coursename.config(state=NORMAL)
#============================================ delete button ==============================================
        
    def delete(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name should be required",parent=self.root)
            else:    
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error","Please select course from the list frist",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete ", "course deletd successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def get_data(self,ev):
        self.txt_coursename.config(state='readonly')
        self.txt_coursename
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_credits.set(row[3])
#==================================================== save button =============================================
    def add(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name should be required",parent=self.root)
            else:    
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","Course Name alredy present",parent=self.root)
                else:
                    cur.execute("insert into course(Name,duration,credit) values(?,?,?)", (  # if need add description and one ? to value 
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_credits.get(),
                        #self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course added successfully",parent=self.root)           
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  
#====================================update button ================================================
    def update(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name should be required",parent=self.root)
            else:    
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Select Course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,credit=? where name=?", (  # if need add description and one ? to value 
                        self.var_duration.get(),
                        self.var_credits.get(),
                        self.var_course.get()
                      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course update successfully",parent=self.root)           
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  


    def show(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)  
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")       
    

    def search(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)  
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")       
     

if __name__=="__main__" :
    root = Tk()
    obj=courseclass(root)
    root.mainloop()
