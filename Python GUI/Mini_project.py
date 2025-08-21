from tkinter import *
from PIL import Image,ImageTk
news_root=Tk()
news_root.title("PERSONAL_INTREST")
news=Label(text="MEET THE CREATOR OF THE PROGRAM~'SAKSHAM JAISWAL'",font="georgia 14",bg="BLACK",fg="yellow",relief="sunken")
news.pack(side="top",anchor="nw",fill="x")
#################################################################################################
news=Label(text="THIS IS AN FRAUD " \
"\nTHE SCHOOLS TELLS US IN OUR SCHOOL THE FUTRE IS BRIGHT " \
"\nBUT THE REALITY IS THE TEACHEES US IN THE PRUSSIAN SYSTEM WHICH IS NOT A VALUABLE FOR CREATIVE MIND"
,font="georgia 13",bg="red",fg="white",borderwidth=6,pady=3).pack(side="bottom",anchor="nw",fill="x")
#################################################################################################
image1 = Image.open("img/me.jpeg")  # Use your file name and extension
image1 = image1.resize((370, 600), Image.LANCZOS)  # Correct: resize the PIL image
photo1 = ImageTk.PhotoImage(image1)
image1_label = Label(news_root, image=photo1)
image1_label.photo = photo1
image1_label.pack(side="left",anchor="nw",fill="x")
#################################################################################################
news=Label(text="The reasons why the creator and everyone loves him because 'ZORO-DA' kakui" \
"\nHe uses three sword style  and all of them are CURSED BLADES made up in his home-town" \
"\nHis dream is to become world's STRONGEST SWORD-MASTER !!!"
,font="verdana 15",bg="darkgreen",fg="WHITE").pack(side="top",anchor="sw",fill="x")
###############################################################################################
image1 = Image.open("img/logo.jpg")  # Use your file name and extension
image1 = image1.resize((400, 600), Image.LANCZOS)  # Correct: resize the PIL image
photo1 = ImageTk.PhotoImage(image1)
image1_label = Label(news_root, image=photo1)
image1_label.photo = photo1
image1_label.pack(side="left",anchor="se",fill="x")
################################################################################################
news=Label(text="The favourite character of the creator |ZORO-JURO|" \
"\nAn pirate hunter which is very powerful and Handsome Rizzler" \
"\nAnd there are various Reasons why zoro is intresting\nBCOZ he full fills his promises" \
"\nthats not all for the achivements you can google it " \
,font="georgia 13",bg="black",fg="white",borderwidth=6).pack(side="top",anchor="se",fill="x")
################################################################################################
# """In png we use file 
# and
# In jpg/jpeg we don't USE file keyword"""

img = Image.open("img/zoro.png.png")
img = img.resize((625, 543), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
image = Label(news_root, image=photo)
image.photo = photo
image.pack(side="top", anchor="ne",fill="x")
###############################################################################################
news_root.geometry('543x343')
news_root.minsize(543,343)
news_root.maxsize(1920,1080)
news_root.mainloop()
####################################################################################################