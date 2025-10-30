from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql

class RegisterClass:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")
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
        # Variables
        # self.var_fname = StringVar()
        # self.var_lname = StringVar()
        # self.var_contact = StringVar()
        # self.var_email = StringVar()
        # self.var_question = StringVar(value="Select")
        # self.var_answer = StringVar()
        # self.var_password = StringVar()
        # self.var_confirm_password = StringVar()
        # self.var_chk = IntVar()

        # Title 
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Register Window", font=("Georgia", 18, "bold"), bg="lightgreen", fg="black")
        title.place(x=45, y=20)

        #=================row 1==========================
        
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        f_name.place(x=50, y=60)
        self.txt_fname = Entry(frame1, font=("times new roman", 15,), bg="lightgray")
        self.txt_fname.place(x=50, y=90, width=250, height=35)
    
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=60)
        self.txt_l_name = Entry(frame1, font=("times new roman", 15,), bg="lightgray")
        self.txt_l_name.place(x=370, y=90, width=250, height=35)

        #==========================contact details==========================
        contact = Label(frame1, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=130)
        self.txt_contact = Entry(frame1, font=("times new roman", 15,), bg="lightgray")
        self.txt_contact.place(x=50, y=165, width=250, height=35)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=130)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=165, width=250, height=35)

        #==============================row 3=====================
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        question.place(x=50, y=205)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your Birth Place", "Your Birth Date", "Your Nick Name", "Your Best Friend Name", "Your Kinky Secret")
        self.cmb_quest.place(x=50, y=240)
        self.cmb_quest.current(0)
        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        answer.place(x=370, y=205)
        self.txt_answer = Entry(frame1, font=("times new roman", 15,), bg="lightgray")
        self.txt_answer.place(x=370, y=240, width=250, height=35)

        #=============================password===============================
        password= Label(frame1, text="Password", font=("comicsans", 15, "bold"), bg="white", fg="black")
        password.place(x=50, y=280)
        self.txt_pass = Entry(frame1, font=("times new roman", 15,), bg="lightgray", show='*')
        self.txt_pass.place(x=50, y=320, width=250, height=35)

        con_pass = Label(frame1, text="Confirm Password", font=("comicsans", 15, "bold"), bg="white", fg="black")
        con_pass.place(x=370, y=280)
        self.txt_con_pass = Entry(frame1, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_con_pass.place(x=370, y=320, width=250, height=35)

        #========================checkBox==========================
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree the Terms & Conditions", variable=self.var_chk,onvalue=1, offvalue=0, bg="lightblue", activebackground="lightyellow", font=("georgia", 12, "bold"))
        chk.place(x=50, y=380)

        btn_reg = Button(frame1, text="Register Now", font=("georgia", 15, "bold"), cursor="hand2", bg="green", activebackground="lightgreen", fg="white", command=self.register_data)
        btn_reg.place(x=60, y=430, width=270, height=35)

        btn_sign = Button(frame1, text="Sign In", font=("georgia", 15, "bold"), cursor="hand2", bg="green", activebackground="lightgreen", fg="white",command=self.login_window)
        btn_sign.place(x=400, y=430, width=120, height=35)

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

    def login_window(self):
        self.root.destroy()
        import login


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_pass.get()=="" or self.txt_con_pass.get()=="" or self.txt_answer.get()=="" or self.txt_contact.get()=="":
            messagebox.showerror("Error", "all feilds are required", parent=self.root)
            return
        elif self.txt_pass.get()!=self.txt_con_pass.get():
            messagebox.showerror("Error", "passwords do not match", parent=self.root)
            return 
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please agree to the terms and conditions", parent=self.root)
            return 
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="resultmanage")
                cur=con.cursor()
                cur.execute("select * from college where email=%s", self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already exists, please try with another email", parent=self.root)
                else:
                    cur.execute("insert into college (f_name,l_name,contact,email,question,answer,password) values(%s, %s, %s, %s, %s, %s, %s)",
                        (self.txt_fname.get(),
                        self.txt_l_name.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmb_quest.get(),
                        self.txt_answer.get(),
                        self.txt_pass.get()
                        )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

            


# if __name__ == "__main__":
root = Tk()
obj = RegisterClass(root)
root.mainloop()