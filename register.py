from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

class RegisterClass:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightblue")
    #=============image===========
        self.bg_img = Image.open("images/na.jpg")
        self.bg_img = self.bg_img.resize((1350, 720), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=250, y=10, relwidth=1, relheight=1)
    #=============Side image===========
        self.left_img = Image.open("images/re.png")
        self.left_img = self.left_img.resize((400, 500), Image.LANCZOS)
        self.left_img = ImageTk.PhotoImage(self.left_img)
        self.left = Label(self.root, image=self.left_img)
        self.left.place(x=80, y=100, width=400, height=500)
        # Variables
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()

        # Title 
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title = Label(frame1, text="Register Window", font=("Georgia", 18, "bold"), bg="lightgreen", fg="black")
        title.place(x=45,y=20)
        # title.pack(pady=25)
#=================row 1==========================
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=60)
        txt_fname=Entry(frame1,font=("times new roman",15,),bg="lightgray").place(x=50,y=90,width=250,height=35)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=60)
        txt_lname=Entry(frame1,font=("times new roman",15,),bg="lightgray").place(x=370,y=90,width=250,height=35)
#==========================contact details==========================
        f_contact=Label(frame1,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=130)
        txt_contact=Entry(frame1,font=("times new roman",15,),bg="lightgray").place(x=50,y=165,width=250,height=35)

        l_email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=130)
        txt_l_email=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=165,width=250,height=35)
#==============================row 3=====================
        f_question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=205)
        cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        cmb_quest['values']=("Select","Your Birth Place","Your Birth Date","Your Nick Name","Your Best Friend Name","Your Kinky Secret")
        cmb_quest.place(x=50,y=240)
        cmb_quest.current(0)
        l_answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=205)
        txt_l_answer=Entry(frame1,font=("times new roman",15,),bg="lightgray").place(x=370,y=240,width=250,height=35)
#=============================password===============================
        f_pass=Label(frame1,text="Password",font=("comicsans",15,"bold"),bg="white",fg="black").place(x=50,y=280)
        txt_pass=Entry(frame1,font=("times new roman",15,),bg="lightgray").place(x=50,y=320,width=250,height=35)

        l_con_pass=Label(frame1,text="Confirm Password",font=("comicsans",15,"bold"),bg="white",fg="black").place(x=370,y=280)
        txt_l_con_pass=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=320,width=250,height=35)

#========================checkBox==========================
        chk=Checkbutton(frame1,text="I Agree the terms and conditions",onvalue=1,offvalue=0,bg="lightblue",activebackground="lightyellow",font=("georgia",12,"bold")).place(x=50,y=380)

        regi=Button(frame1,text="Register Now",font=("georgia",15,"bold"),cursor="hand2",bg="green",activebackground="lightgreen",fg="white",command=self.register)
        regi.place(x=60,y=430,width=270,height=35)

        sign=Button(frame1,text="Sign In",font=("georgia",15,"bold"),cursor="hand2",bg="green",activebackground="lightgreen",fg="white")
        sign.place(x=400,y=430,width=120,height=35)





        
    def register(self):
        fname = self.var_fname.get()
        lname = self.var_lname.get()
        contact = self.var_contact.get()
        email = self.var_email.get()
        question = self.var_question.get()
        answer = self.var_answer.get()
        password = self.var_password.get()
        cpassword = self.var_confirm_password.get()
        agree = self.var_chk.get()

        if fname == "" or lname == "" or contact == "" or email == "" or question == "Select" or answer == "" or password == "" or cpassword == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        return
        if password != cpassword:
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        return
        if agree == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions", parent=self.root)
        return

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fname TEXT,
                lname TEXT,
                contact TEXT,
                email TEXT UNIQUE,
                question TEXT,
                answer TEXT,
                password TEXT
                )
            """)
            cur.execute("SELECT * FROM users WHERE email=?", (email,))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Email already registered", parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO users (fname, lname, contact, email, question, answer, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (fname, lname, contact, email, question, answer, password)
                )
                con.commit()
                messagebox.showinfo("Success", "User registered successfully", parent=self.root)
            # Optionally clear fields here
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = RegisterClass(root)
    root.mainloop()