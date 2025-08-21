from tkinter import*
from PIL import Image, ImageTk
root=Tk()

root.geometry("455x344")

# photo= PhotoImage("no.png")
# image1=Label(root, image=photo)  # used image cannot used again
# image1.photo=photo
# image1.pack()
image = Image.open(" logo.jpg ")  # Use your file name and extension
image = image.resize((1024, 720))  # Resize the image if needed
photo = ImageTk.PhotoImage(image)
image=Label(root,image=photo)
image.photo=photo
image.pack()

root.mainloop()