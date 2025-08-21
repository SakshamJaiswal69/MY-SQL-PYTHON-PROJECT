from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("COLLEGE RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.maxsize(1200,480)
        self.root.minsize(1080,450)
        self.root.config(bg="#FFFFFF")
        self.root.focus_force()
#===============title==========================
        title = Label(self.root, text="Manage Course Detail", font=("goudy old style", 20, "bold"), bg="#0BE264", fg="black")
        title.place(x=1, y=10, width=1200, height=35)
#==========================Variables===============
        self.var_Course = StringVar()
        self.var_Duration = StringVar()
        self.var_Charges = StringVar()
        self.var_search = StringVar()
#=====================Widgets================
        lbl_course=Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=60)
        lbl_duration=Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=100)
        lbl_charges=Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=140)
        lbl_description=Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="light yellow").place(x=10, y=180)
#==================Entry_fields================
        self.txt_Course = Entry(self.root, textvariable=self.var_Course, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_Course.place(x=150, y=60, width=200)
        self.txt_Duration = Entry(self.root, textvariable=self.var_Duration, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_Duration.place(x=150, y=100, width=200)
        self.txt_Charges = Entry(self.root, textvariable=self.var_Charges, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_Charges.place(x=150, y=140, width=200)
        self.txt_Description = Text(self.root, font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_Description.place(x=150, y=180, width=550, height=100)
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
        lbl_search=Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search=Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="yellow",activebackground="yellow", fg='black', cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)
#=========================Content_Frame====================
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=450, height=350)
#=======================scroll_bar=========================
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "course", "Duration", "charges", "description"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
#=================heading/columns============================
        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("course", text="Name")
        self.CourseTable.heading("Duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("Duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=100)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#==========================CLEAR========================================
    def clear(self):
        self.show()
        self.var_Course.set("")
        self.var_Duration.set("")
        self.var_search.set("")
        self.var_Charges.set("")
        self.txt_Description.delete("1.0",END)
        self.txt_Course.config(state=NORMAL)
#======================DELETE==========================================
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_Course.get() == "":
                messagebox.showerror("Error", "Select Course First", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE course = ?", (self.var_Course.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please select course from the list first", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where course =?",(self.var_Course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course Deleted Succesfully",parent=self.root)
                        self.show()
        
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
#=========================GET_DATA================================================
    def get_data(self,ev):
        self.txt_Course.config(state="readonly")
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        # print(row)
        self.var_Course.set(row[1])
        self.var_Duration.set(row[2])
        self.var_Charges.set(row[3])
        # self.var_Course.set(row[4])
        self.txt_Description.delete("1.0",END)
        self.txt_Description.insert(END,row[4])
#========================ADD===========================================
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_Course.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE course = ?", (self.var_Course.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This course is already present, try different", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO course (course,Duration,charges,description) VALUES (?,?,?,?)",
                        (
                            self.var_Course.get(),
                            self.var_Duration.get(),
                            self.var_Charges.get(),
                            self.txt_Description.get("1.0", END).strip()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
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
            if self.var_Course.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE course = ?", (self.var_Course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select Course from List", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE course SET Duration=?,charges=?,description=? WHERE course=? ",
                        (
                            self.var_Duration.get(),
                            self.var_Charges.get(),
                            self.txt_Description.get("1.0", END),
                            self.var_Course.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Course Updated successfully", parent=self.root)
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
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  
#=================CLEAR==========================================
    def clear(self):
        self.var_Course.set("")
        self.var_Duration.set("")
        self.var_Charges.set("")
        self.var_search.set("")
        self.txt_Description.delete("1.0", END)
#==================SEARCH=====================================
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Course name required for search", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE course LIKE ?", ('%' + self.var_search.get() + '%',))
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()