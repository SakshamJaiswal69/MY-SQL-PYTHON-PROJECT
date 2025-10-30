from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql

class loginclass:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightblue")
    #=============image===========
        self.bg_img = Image.open("images/re.png")
        # self.bg_img = self.bg_img.resize((1350, 720), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        lbl_bg = Label(self.root, image=self.bg_img)
        lbl_bg.place(x=10, y=10, relwidth=1, relheight=1)
    #=============Side image===========
        self.left_img = Image.open("images/reg.png")
        # self.left_img = self.left_img.resize((400, 500), Image.LANCZOS)
        self.left_img = ImageTk.PhotoImage(self.left_img)
        left = Label(self.root, image=self.left_img)
        left.place(x=80, y=100, width=400, height=500)
        
        # Title 
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Login Window", font=("Georgia", 18, "bold"), bg="lightgreen", fg="black")
        title.place(x=45, y=20)
        
        #==========================contact details==========================

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=50, y=60)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=50, y=90, width=250, height=35)


        #=============================password===============================
        password= Label(frame1, text="Password", font=("comicsans", 15, "bold"), bg="white", fg="black")
        password.place(x=50, y=160)
        self.txt_pass = Entry(frame1, font=("times new roman", 15,), bg="lightgray", show='*')
        self.txt_pass.place(x=50, y=200, width=250, height=35)

        #========================checkBox==========================
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree the Terms & Conditions", variable=self.var_chk,onvalue=1, offvalue=0, bg="lightblue", activebackground="lightyellow", font=("georgia", 12, "bold"))
        chk.place(x=50, y=330)

        btn_log = Button(frame1, text="Login", font=("georgia", 15, "bold"), cursor="hand2", bg="red", activebackground="lightgreen", fg="white" ,command=self.Login_data)
        btn_log.place(x=60, y=400, width=180, height=35)

        btn_forget = Button(frame1, text="Forget Password", font=("georgia", 15, "bold"), cursor="hand2", bg="green", activebackground="lightgreen", fg="white" ,command=self.forget_password_window)
        btn_forget.place(x=50, y=260, width=270, height=35)

        btn_reg = Button(frame1, text="Register New Account", font=("georgia", 10, "bold"), cursor="hand2", bg="yellow", activebackground="lightgreen", fg="black",command=self.register_window)
        btn_reg.place(x=400, y=400, width=180, height=35)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_l_name.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_con_pass.delete(0, END)
        self.var_chk.set(0) 

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="resultmanage")
                cur=con.cursor()                              #SQL queries help
                
                cur.execute("select * from college where email=%s and question=%s and answer =%s", (self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please select the correct Security Question", parent=self.root2)
                    self.clear()
                else:
                cur.execute("update college set password=%s where email=%s ", (self.txt_new_password.get(),self.txt_email.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Succes","your Password has been changed",parent=self.root2)
                self.reset()
                self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter the email first.",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="resultmanage")
                cur=con.cursor()                              #SQL queries help
                
                cur.execute("select * from college where email=%s", (self.txt_email.get()))

                row=cur.fetchone()
    
                if row==None:
                    messagebox.showerror("Error", "Enter valid Email to reset your Password", parent=self.root)
                    self.clear()
                    
                else:

                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")
                    t=Label(self.root2,text="Forget Password",font=("comicsans",15,"bold"),bg="lightblue",fg="black").place(x=0,y=10,relwidth=1)
#====================================================Forget Password work=========================================================
                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    question.place(x=50, y=40)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = ("Select", "Your Birth Place", "Your Birth Date", "Your Nick Name", "Your Best Friend Name", "Your Kinky Secret")
                    self.cmb_quest.place(x=50, y=80)
                    self.cmb_quest.current(0)
                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    answer.place(x=50, y=120)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15,), bg="lightgray")
                    self.txt_answer.place(x=50, y=160, width=250, height=35)
                    password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                    password.place(x=50, y=210)
                    self.txt_new_password = Entry(self.root2, font=("times new roman", 15,), bg="lightgray")
                    self.txt_new_password.place(x=50, y=250, width=250, height=35)

                    btn_change = Button(self.root2, text="Change Password", font=("georgia", 10, "bold"), cursor="hand2", bg="yellow", activebackground="lightgreen", fg="black")command=self.forget_password)
                    btn_change.place(x=70, y=330, width=180, height=35)                    
                
                                    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
#======================================================================================================================================
    def register_window(self):
        self.root.destroy()
        import register

    def Login_data(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="" :
            messagebox.showerror("Error", "all feilds are required", parent=self.root)
            return

        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please agree to the terms and conditions", parent=self.root)
            return 
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="resultmanage")
                cur=con.cursor()                              #SQL queries help
                
                cur.execute("select * from college where email=%s and password=%s ", (self.txt_email.get(), self.txt_pass.get()))

                row=cur.fetchone()
    
                if row==None:
                    messagebox.showerror("Error", "Invalid EMAIL & PASSWORD"/n"Try Forget password", parent=self.root)
                    self.clear()
                    
                else:
                    messagebox.showinfo("Success", "Login Successful", parent=self.root)                    
                    self.root.destroy()                      
                    import result
                    new_root = Tk()
                    obj = result.ResultClass(new_root)
                    new_root.mainloop()
                    
                    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

            


# if __name__ == "__main__":
root = Tk()
obj = loginclass(root)
root.mainloop()