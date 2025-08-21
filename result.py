from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import sqlite3

class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("COLLEGE RESULT MANAGEMENT SYSTEM")
        self.root.geometry("1200x480+80+170")
        self.root.maxsize(1200,480)
        # self.root.minsize(1080,450)
        self.root.config(bg="light yellow")
        self.root.focus_force()
#===============title==========================
        title = Label(self.root, text="Student Results Detail", font=("goudy old style", 20, "bold"), bg="Yellow", fg="black")
        title.place(x=1, y=10, width=1200, height=35)
        #=================variables=====================
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_course=StringVar()
        self.var_marks_ob=StringVar()
        self.var_full_marks=StringVar()
        self.var_per=StringVar()
        self.roll_list=[]
        self.Fetch_roll() 
        
#=============================Widgets====================
        lbl_select=Label(self.root, text="Select student", font=("goudy old style", 20, "bold"), bg="light yellow").place(x=50, y=100)
        lbl_name=Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="light yellow").place(x=50, y=160)
        lbl_course=Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="light yellow").place(x=50, y=220)
        lbl_marks_ob=Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="light yellow").place(x=50, y=280)
        lbl_full_marks=Label(self.root, text="Full marks", font=("goudy old style", 20, "bold"), bg="light yellow").place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll,values= self.roll_list,font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        

        txt_search_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightyellow",state='readonly').place(x=280, y=160, width=350)
        txt_search_course=Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), bg="lightyellow",state='readonly').place(x=280, y=220, width=350)
        txt_search_marks_ob=Entry(self.root, textvariable=self.var_marks_ob, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=280, width=350)
        txt_search_full_marks=Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=340, width=350)

#==========================buttons============================
        btn_search=Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="lightblue",activebackground="lightblue", fg='black', cursor="hand2",command=self.search).place(x=510, y=100, width=120, height=28)
        btn_add=Button(self.root, text="Submit", font=("times new roman", 15), bg="lightgreen",activebackground="lightgreen" , cursor="hand2",command=self.add).place(x=300, y=420, width=120, height=35)
        btn_clear=Button(self.root, text="Clear", font=("times new roman", 15), bg="lightgray",activebackground="lightgray" , cursor="hand2",command=self.clear).place(x=430, y=420, width=120, height=35)

#=========================image===================================
        self.bg_img=Image.open("images/result.png") 
        self.bg_img=self.bg_img.resize((520,340),Image.LANCZOS) 
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)

#=======================Fetch course=================================
    def Fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                   self.roll_list.append(row[0])      
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
    
#=======================search student details===========================
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name,course FROM student WHERE roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
#========================Add================================================
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "Select":
                messagebox.showerror("Error", "Please\nFetch student record", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll = ? and course =?", (self.var_roll.get(),self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This result is already present, try different", parent=self.root)
                else:
                    per=(int(self.var_marks_ob.get())/int(self.var_full_marks.get()))*100
                    cur.execute(
                        "INSERT INTO result (roll,name,course,marks_ob,full_marks,per) VALUES (?,?,?,?,?,?)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks_ob.get(),
                            self.var_full_marks.get(),
                            str(per)
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}", parent=self.root)
        finally:
            con.close()
#===================================Clear=======================================
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks_ob.set("")
        self.var_full_marks.set("")
        self.var_per.set("")
        self.Fetch_roll()  # Refresh the roll list



#================================================================================
if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()