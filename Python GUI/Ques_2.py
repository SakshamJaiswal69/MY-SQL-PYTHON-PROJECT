from tkinter import*
# in bottom of scren we have to write something 
screenroot=Tk()
screenroot.geometry("540x320")
screenroot.maxsize(916,560)
screenroot.minsize(540,460)
screen=Label(text="Get READY for The START-UP MAN !",font="bold 20",foreground="white",background="black",relief="raised",padx=8,pady=10)
screen.pack(side="bottom",fill="x")

screenroot.mainloop()