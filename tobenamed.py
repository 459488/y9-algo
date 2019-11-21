from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import webbrowser

def createfile():
    fo = open("newfile.txt","w")
    fo.write(typesomething.get())
    fo.close()

something = Tk()
something.title("filecreator")
something.geometry("800x500")

save = False

if save==True:
    l1 = Label(something,text="Saved!").grid(row=0,column=0)
else:
    l1 = Label(something,text="Not Saved... :(").grid(row=0,column=0)

bad = Button(something,text="Discard").grid(row=0,column=1)
good = Button(something,text="Save",command=createfile).grid(row=0,column=2)
ready = Button(something,text="Publish").grid(row=0,column=3)

# canvas = Canvas(something, width = 300, height = 300)
# canvas.grid(row=1,column=0)
# img1 = ImageTk.PhotoImage(Image.open("/Users/hewitt.ho/Documents/bin.png"))
# canvas.create_image(20, 20, anchor=NW, image=img1)

typesomething = Entry(something)
typesomething.grid(row=1,column=1)

something.mainloop()