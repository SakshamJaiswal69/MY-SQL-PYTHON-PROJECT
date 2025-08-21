from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("COLLEGE RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.maxsize(1200,480)
        self.root.minsize(1080,450)
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()
#===============title==========================
        title = Label(self.root, text="Manage Student Detail", font=("goudy old style", 20, "bold"), bg="#0BE264", fg="black")
        title.place(x=1, y=10, width=1200, height=35)
#==========================Variables===============
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_search = StringVar()
#=====================Widgets================
#======================column_1======================
        lbl_roll=Label(self.root, text="Roll no", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=60)
        lbl_name=Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=100)
        lbl_Email=Label(self.root, text="Emails", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=140)
        lbl_Gender=Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=180)
        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=150, y=220, width=150)
        lbl_Address=Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=220)

        lbl_City=Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=310, y=220)
        self.txt_City = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=380, y=220, width=100)
        
        lbl_pin=Label(self.root, text="Pin", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=510, y=220)
        self.txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=570, y=220, width=100)

        lbl_State=Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=260)
#==================Entry_fields================
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_roll.place(x=150, y=60, width=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="light yellow")
        txt_name.place(x=150, y=100, width=200)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_email.place(x=150, y=140, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values= ("Select","Male","Female","Other"),font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)
        
#====================column_2===============================
        lbl_dob=Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=360, y=60)
        lbl_contact=Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=360, y=100)
        lbl_admission=Label(self.root, text="Admission", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=360, y=140)
        lbl_course=Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=360, y=180)
#==================Entry_fields================
        self.course_list=[]
#funtion_call to update the list
        self.Fetch_Course()
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_dob.place(x=470, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="light yellow")
        txt_contact.place(x=470, y=100, width=200)
        self.txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_admission.place(x=470, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values= self.course_list,font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=470, y=180, width=200)
        self.txt_course.set("Select")
#====================Text_Fields=====================================       
        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_address.place(x=150, y=250, width=540, height=100)
#==========================Buttons===============================
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3",activebackground="#2196f3", fg="black", cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#22f5eb",activebackground="#22f5eb", fg="black", cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336",activebackground="#f44336", fg="black", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b",activebackground="#607d8b", fg="black", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)
#========================Search_panel===========================
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root, text="Roll no", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_roll=Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="yellow",activebackground="yellow", fg='black', cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)
#=========================Content_Frame====================
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=450, height=350)
#=======================scroll_bar=========================
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "Name", "email", "gender", "dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
#=================heading/columns============================
        self.CourseTable.heading("roll", text="Roll no")
        self.CourseTable.heading("Name", text="Name")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="PIN")
        self.CourseTable.heading("address", text="Address")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("roll", width=50)
        self.CourseTable.column("Name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("admission", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("address", width=100)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#==========================CLEAR========================================
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.var_search.set("")
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
#======================DELETE==========================================
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Select Student First", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select student from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM student WHERE roll = ?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student Deleted Successfully", parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
#=========================GET_DATA================================================
    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        if row:
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
            self.txt_address.insert(END, row[11])
#========================ADD===========================================
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "ROLL NO. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Roll No. is already present, try different", parent=self.root)
                else:
                    cur.execute(
                            "INSERT INTO STUDENT(roll,Name,email,gender,dob,contact,admission,course,state,city,pin,address) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
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
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
#===========================UPDATE=========================================
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No. is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select Student from List", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE student SET Name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? WHERE roll=?",
                    (
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
                        self.txt_address.get("1.0", END).strip(),
                        self.var_roll.get()
                    )
                )
                con.commit()
                messagebox.showinfo("Success", "Student Updated successfully", parent=self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
#======================SHOW==============================================
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  

#=====================Fetch_Course============================
    def Fetch_Course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT course FROM course")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                   self.course_list.append(row[0])      
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
    
#==================SEARCH=====================================
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE roll=?", (self.var_search.get(),))
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            if rows:
                for row in rows:
                    self.CourseTable.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()