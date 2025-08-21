from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import sqlite3

class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("COLLEGE RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.maxsize(1200,480)
        # self.root.minsize(1080,450)
        self.root.config(bg="light yellow")
        self.root.focus_force()
#===============title========================================================================
        title = Label(self.root, text="Student Results ", font=("goudy old style", 20, "bold"), bg="Yellow", fg="black")
        title.place(x=1, y=10, width=1200, height=35)
#===============================variable================================================
        self.var_search=StringVar()
        self.var_id=""
#=============================search================================================
        lbl_search = Label(self.root, text="Search By Roll No.", font=("georgia", 20, "bold"), bg="white")
        lbl_search.place(x=230, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("georgia", 20 ), bg="light yellow")
        txt_search.place(x=490, y=100, width=150)
#=============================Buttons===========================================
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="lightblue",activebackground="lightblue", fg='black', cursor="hand2",command=self.search)
        btn_search.place(x=650, y=100, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="gray",activebackground="lightgray", fg='black', cursor="hand2",command=self.clear)
        btn_clear.place(x=770, y=100, width=100, height=35)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="Red",activebackground="red", fg='white', cursor="hand2",command=self.delete)
        btn_delete.place(x=500, y=350, width=150, height=35)
#=============================LABELS=============================================
        lbl_roll = Label(self.root, text="Roll No.", font=("georgia", 12, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        lbl_roll.place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("georgia", 12, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        lbl_name.place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("georgia", 12, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        lbl_course.place(x=450, y=230, width=150, height=50)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=("georgia", 12, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        lbl_marks_ob.place(x=600, y=230, width=150, height=50)
        lbl_full_marks = Label(self.root, text="Total marks", font=("georgia", 12, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        lbl_full_marks.place(x=750, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="Percentage", font=("georgia",12, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        lbl_per.place(x=900, y=230, width=150, height=50)

        # ==================================================
        self.roll = Label(self.root, font=("georgia", 10, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root, font=("georgia", 10, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=("georgia", 10, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks_ob = Label(self.root, font=("georgia", 10, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        self.marks_ob.place(x=600, y=280, width=150, height=50)
        self.full_marks = Label(self.root, font=("georgia", 10, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        self.full_marks.place(x=750, y=280, width=150, height=50)
        self.per = Label(self.root, font=("georgia", 10, "bold"), bg="light yellow", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)
#==============================search=============================================
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                if self.var_search.get()=="":
                        messagebox.showerror("Error","Roll No. should be required",parent=self.root)
                else:
                        cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
                        row = cur.fetchone()
                        if row is not None:
                                self.var_id=row[0]
                                self.roll.config(text=row[1])
                                self.name.config(text=row[2])
                                self.course.config(text=row[3])
                                self.marks_ob.config(text=row[4])
                                self.full_marks.config(text=row[5])
                                self.per.config(text=row[6])
                        else:
                                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
                con.close()
#================================================================================
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")  
        self.var_search.set("")
#================================================================================
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search Student Result First", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE rid = ?", (self.var_id,))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid =?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result Deleted Succesfully",parent=self.root)
                        self.clear()        
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
#================================================================================

if __name__ == "__main__":
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()