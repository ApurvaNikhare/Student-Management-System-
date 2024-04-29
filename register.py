from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os 
class Register:
        def __init__(self,root):
                self.root=root
                self.root.title("Regiseration Window")
                self.root.geometry("1350x700+0+0")
                self.root.config(bg="indigo")
                self.root.focus_force()

#==================================================== IMAGE ==================================================================================================
        
                self.bg=ImageTk.PhotoImage(file="image/reg_2.jpeg")
                bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

#================================================== left image ==========================================================================================================
        
                self.Left=ImageTk.PhotoImage(file="image/Background.jpeg")
                Left=Label(self.root,image=self.Left).place(x=80,y=100,width=400,height=500)

#======================================= Register frame ======================================================================================================
        
                frame1=Frame(self.root,bg="white")

                frame1.place(x=480,y=100,width=700,height=500)
                title=Label(frame1,text="REGISTER HERE ",font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=250,y=30)
#-----------------------------------------------------------row1 -----------------------------------------------------------------------------------------------s
        

                fname=Label(frame1,text="Frist Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=100)
                self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
                self.txt_fname.place(x=50,y=130,width=250)

                lname=Label(frame1,text="Last Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=370,y=100)
                self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
                self.txt_lname.place(x=370,y=130,width=250)

#----------------------------------------------------------row2------------------------------------------------------------------------------------------
        
                contact=Label(frame1,text="Contact ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=170)
                self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
                self.txt_contact.place(x=50,y=200,width=250)

                email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=370,y=170)
                self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
                self.txt_email.place(x=370,y=200,width=250)

#----------------------------------------------------------row3 ---------------------------------------------------------------------------------------
        
                quetion=Label(frame1,text="Security Quetion",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=240)
                self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
                self.cmb_quest["values"]=("Select","Your Frist Pet Name","Your Birth Place","Your Best Friend Name")
                self.cmb_quest.place(x=50,y=270,width=250)
                self.cmb_quest.current(0)

                answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=370,y=240)
                self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
                self.txt_answer.place(x=370,y=270,width=250)

#----------------------------------------------------------------row4 -------------------------------------------------------------------------------------------
        
                password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=310)
                self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
                self.txt_password.place(x=50,y=340,width=250)

                cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=370,y=310)
                self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
                self.txt_cpassword.place(x=370,y=340,width=250)

        #-------------------------------------------- term -------------------------------------------------------
                self.var_chk=StringVar()
                chk=Checkbutton(frame1,text="I Agree The Term & Conditions",variable=self.var_chk,bg="white",offvalue=0,onvalue=1,font=("times new roman",12)).place(x=50,y=380)

        

                self.btn_img= ImageTk.PhotoImage(file="image/registration.webp")  
                btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=60,y=420,height=50)

                btn_login=Button(self.root,text="Sing In",command=self.Login_window,font=("times new roman",20),bg="white",bd=0,cursor="hand2").place(x=200,y=350,width=180)

        def Login_window(self): 
                self.root.destroy()             
                os.system("Python login.py")  

        def clear(self):
                self.txt_fname.delete(0,END),
                self.txt_lname.delete(0,END),
                self.txt_contact.delete(0,END),
                self.txt_email.delete(0,END),
                self.txt_answer.delete(0,END),
                self.txt_password.delete(0,END),
                self.txt_cpassword.delete(0,END),
                self.cmb_quest.current(0)
                


        def register_data(self):
                if self.txt_fname.get()=="" or self.txt_email.get()==""  or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.cmb_quest.get()=="Select" :
                        messagebox.showerror("Error","All Feilds Are Required",parent=self.root)
                        
                elif self.txt_password.get()!= self.txt_cpassword.get():
                        messagebox.showerror("Error","Password & confirm password should be same ",parent=self.root)

                #elif self.var_chk.get() == 0:
                #messagebox.showerror("Error","Please Agree Our Term & Conditions",parent=self.root)

                else:
                        try:
                                con=sqlite3.connect(database="project.db")
                                cur=con.cursor()
                                cur=con.execute("Select * from employee where email=?",(self.txt_email.get(),))
                                row=cur.fetchone()
                                if row != None:
                                        messagebox.showinfo("Success","User Already Exist, Please Try With Another Email",parent=self.root)
                                else:

                                        cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                                (self.txt_fname.get(),
                                                self.txt_lname.get(),
                                                self.txt_contact.get(),
                                                self.txt_email.get(),
                                                self.cmb_quest.get(),
                                                self.txt_answer.get(),
                                                self.txt_password.get()    
                                                ))
                                        con.commit()
                                        con.close()
                                        messagebox.showinfo("Success","Register Successful",parent=self.root)
                                        self.clear()
                                        self.Login_window()

                        
                        except Exception as es:
                                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


if __name__=="__main__" :
        root=Tk()
        obj=Register(root)
        root.mainloop()