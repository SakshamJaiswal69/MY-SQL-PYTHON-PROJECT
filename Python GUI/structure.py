from tkinter import * 
# this is to make an  simple window 
helloroot=Tk() 
hello =Label(text="saksham is an coder",font="Georgia 20",fg="white",bg="black").pack() # in label attribute ther will be only name 
helloroot.minsize(1024,768)
helloroot.geometry("1280x800")
helloroot.maxsize(1280,720)
helloroot.title("This is not the power of your creation !")
# print(font.families())  # this is to print the font families in the console
helloroot.mainloop()