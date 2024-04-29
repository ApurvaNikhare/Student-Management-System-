from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os 
class Login_window:
    def __init__(self, root) :
        self.root=root
        self.root.title("Login System ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#7B68EE")
#==================================================== image add ====================================================
        self.co_img=Image.open("image/login.jpeg")
        self.co_img=self.co_img.resize((400,350),Image.ANTIALIAS)
        self.co_img=ImageTk.PhotoImage(self.co_img)
        self.lbl_bg=Label(self.root,image=self.co_img).place(x=0,y=180,width=500,height=430)
#=============================================== login frame ======================================================= 
        login_frame=Frame(self.root,bg="#483D8B")
        login_frame.place(x=520,y=150,width=800,height=500)
        title=Label(login_frame,text="LOGIN HERE",font=("times new romon",20,"bold"),bg="#483D8B",fg="yellow").place(x=300,y=30)
       
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new romon",15,"bold"),bg="#483D8B",fg="white").place(x=300,y=100)
        self.txt_email=Entry(login_frame,font=("times new romon",15,"bold"),bg="lightgray")
        self.txt_email.place(x=200,y=130,width=350,height=30)    

        Pass= Label(login_frame,text="PASSWORD",font=("times new romon",15,"bold"),bg="#483D8B",fg="white").place(x=300,y=200)
        self.txt_Pass=Entry(login_frame,font=("times new romon",15,"bold"),bg="lightgray")
        self.txt_Pass.place(x=200,y=230,width=350,height=30)   

        btn_reg=Button(login_frame,cursor="hand2",text="Register new Account?",command=self.register_window,font=("times new roman ", 14),bg="#483D8B",bd=0,fg="white").place(x=100,y=300) 
        btn_forget=Button(login_frame, cursor="hand2",text="Forgot Password?",command=self.forgot_password_window,font=("times new roman ", 14),bg="#483D8B",bd=0,fg="white").place(x=500,y=300) 
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman ",20,"bold"),bg="#7B68EE",fg="white").place(x=300,y=360,width=180,height=40) 
   
   
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_Pass.delete(0,END)
        self.txt_email.delete(0,END)  

    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root2)

        else:
            try:
                con=sqlite3.connect(database="project.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=? ",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select the currect security question / Enter Answer" ,parent=self.root2)
                   
        
                else:
                    cur.execute("update employee set password=? where email=? ",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset , Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es :
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)
    

 
    def forgot_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter email to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="project.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter valid email to reset your password",parent=self.root)
                   
                   
        
                else:
                    con.close()
                    self.root2=Toplevel() 
                    self.root2.title("Forgot Password")
                    self.root2.geometry("400x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forgot Password",font=("times new romon",20,"bold"),bg="white",fg="red").place(x=80,y=10)

#============================================== forgot page==============================================
    
                    quetion=Label(self.root2,text="Security Quetion",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=100)
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
                    self.cmb_quest["values"]=("Select","Your Frist Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)     
                
            except Exception as es :
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


    def register_window(self):
        self.root.destroy()
        os.system("Python register.py")


    def login(self):

        if self.txt_email.get()==""or self.txt_Pass.get()=="":
            messagebox.showerror("Error","All fileds are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="project.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_Pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD" ,parent=self.root)
                    self.root.destroy()
                    os.system("Python register.py")        
        
                else:
                    messagebox.showinfo("Success",f"Welcome {self.txt_email.get()}" ,parent= self.root)
                    self.root.destroy()
                    os.system(" Python dashboard.py ")
                con.close()
         
     
            except Exception as es :
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


if __name__=="__main__" :
    root = Tk()
    obj=Login_window(root)
    root.mainloop()