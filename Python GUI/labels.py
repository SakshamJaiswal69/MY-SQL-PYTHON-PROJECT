# In this program their is full of labels functions 
from tkinter import*
ayush_root=Tk()

ayush_root.title("In this program their is full of labels functions ")
ayush_root.geometry("560x444")
ayush_root.maxsize(780,1240)
ayush=Label(text="Saksham will become an Entreprenuer",fg="black",bg="yellow",font="comicsansms,bold, 19",padx=20,pady=5)
ayush1=Label(text="The topic is HUMAN MIND REGROWTH",fg="black",bg="yellow",font="comicsansms,bold, 19",padx=20,pady=5)
ayush.pack(anchor="se")  # anchor is used to set the position of the label in the window
ayush1.pack(side="bottom",anchor="nw")# anchor ="se,ne,sw,nw" #side="top,bottom,left,right"


ayush_root.mainloop()