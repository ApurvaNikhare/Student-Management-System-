from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class StudentClass:
    def __init__(self, root) :
        self.root=root
        self.root.title("Student result system")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=================title=========================#
        title = Label(self.root,text="Manage Student Detail",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1520,height=35)

        #==========================variable============================#
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
    
         
        #=================== widget ======================#
        #========================= coloumn 1======================================
        lbl_roll=Label(self.root,text="Roll Number",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=160)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=280)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=340)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=340, width=150)

        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=340)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=360, y=340, width=130)

        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=530,y=340)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=570, y=340, width=100)





        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=400)


        #======================= Entry field =================================#

        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=100, width=200)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_name.place(x=150, y=160, width=200)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_email.place(x=150, y=220, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Other"), font=("goudy old style", 15, "bold"), state="raedonly",justify=CENTER)
        self.txt_gender.place(x=150, y=280, width=200)
        self.txt_gender.current(0)

        #======================= coloumn 2 ================================
        lbl_dob=Label(self.root,text="Date-Of-Birth",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=100)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=160)
        lbl_a_date=Label(self.root,text="Admission_D",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=220)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=280)

        self.course_list=[]
        #fuction to opearte the list
        self.fetch_course()

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=500, y=100, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=500, y=160, width=200)
        txt_a_date = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=500, y=220, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list, font=("goudy old style", 15, "bold"), state="raedonly",justify=CENTER)
        self.txt_course.place(x=500, y=280, width=200)
        self.txt_course.set("Select")



#==================== txt address ==========================================================
        
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=400,width=550,height=100)

        #========================== Bottons =============================#

        self.btn_add=Button(self.root,text="Save", font= ("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=520,width=110,height=40)

        self.btn_update=Button(self.root,text="Update", font= ("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=520,width=110,height=40)

        self.btn_delete=Button(self.root,text="Delete", font= ("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=520,width=110,height=40)

        self.btn_clear=Button(self.root,text="Clear", font= ("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=520,width=110,height=40)

        #===================== search panel ==============================#
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=780,y=100)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=100, width=180)
        btn_search=Button(self.root,text="Search", font= ("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=100,width=120,height=28)

        #=================== content ===========================#
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720,y=200,width=470,height=400)

        scrolly = Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll", "Name","email","gender", "dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)


        self.CourseTable.heading("roll",text="Roll No")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact No")
        self.CourseTable.heading("admission",text="Admission Date")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="Pin")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("Name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=200)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#================================================clear button ====================================================
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
#============================================ delete button ==============================================
        
    def delete(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required",parent=self.root)
            else:    
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error","Please select student from the list frist",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete ", "Student deletd successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[11])
#==================================================== save button =============================================
    def add(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required",parent=self.root)
            else:    
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","Roll Number alredy present",parent=self.root)
                else:
                    cur.execute("insert into student( roll ,  Name , email , gender ,  dob , contact , admission , course , state , city , pin , address ) values(?,?,?,?,?,?,?,?,?,?,?,?)", (  # if need add description and one ? to value 
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student added successfully",parent=self.root)           
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  
#====================================update button ================================================
    def update(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required",parent=self.root)
            else:    
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set Name=? , email=? , gender=? ,  dob=? , contact=? , admission=?  , course=?  , state=?  , city=?  , pin=?  , address=?  where roll=?", (  
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get()
                      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update successfully",parent=self.root)           
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  


    def show(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)  
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   


    def fetch_course(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
    

    def search(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor() 
        try:
            cur.execute(f"select * from student where roll=?",(self.var_search.get(),) )
            row=cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)  
            else:
                messagebox.showerror("Error","No record found",parent=self.root)       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")       
     

if __name__=="__main__" :
    root = Tk()
    obj=StudentClass(root)
    root.mainloop()
