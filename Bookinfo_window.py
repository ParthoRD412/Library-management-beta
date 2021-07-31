# this is the module to show the top layer about the content of the book

from tkinter import * # calling all the classes of the tkinter module

from PIL import Image, ImageTk # call the image and imagetk classes of Pillow module to open the image

# use these variables to store information. 

# pass the information as per the variables

var = "" # book info, this variable is to store the informatin about the book | this shows the name of the book in caps, author's name, book code and book genre.

bookimageid = "" # this is to store the id of the image of the book

playbuttonid = "" # this is to store the id of the play button's image

bookshortintro = "" # this variable is used to store a short information about what the book is

ebookavailablity = "" # this variable will have the value "disabled"  if ebook isn't available or else "active"

"""

def playinfo():

	# this function is used to read out the short introduction about the book	variable : bookshortintro

	

def pdfviewer():

	# this function is used to open the pdf viewer to show the pdf of the book whose content you have opened

"""

# this is the main content of the graphical program

root = Tk()

def book_info():

	top=Toplevel(root,bg="lightgreen") # this is the secondary window

	top.geometry("1000x800")

	top.title("Book Info")

	

	# This is the section where image of the book will be shown

	image=open(bookimageid) # opening an image

	photo=ImageTk.PhotoImage(image) # converting the image from jpg or jpeg to png

	photolabel=Label(top,image=photo) # this is storing the image as a label in the foot variable

	photolabel.grid(row=0, column=0) # griding the foot variable 

	

	

	Label(top, text=var).grid(row=0,column=1,padx=10) # here the information of the book will be shown

	

	

	# this is the image that will overlap the button

	playbutton=open(playbuttonid)

	photobutton=ImageTk.PhotoImage(playbutton)

	playlabel=Label(top,image=photobutton)

	playlabel.grid(row=0,column=2,padx=30)

	

	Button(top, text="play",command=playinfo).grid(row=0,column=2,padx=30) # this button is to play the information about the book

	

	

	

	Label(top,text=bookshortintro,font="Times 10 bold italic").grid(row=1,column=0,pady=20) # this is the label to show the short intro about the book which is being displayed

	

	

	

	Button(top,text="Open Ebook",bg="green",fg="white",font="Times 10 bold italic",state=ebookavailablity,border=10,relief="raised", command=pdfviewer).grid(row=2,column=0,padx=40) # this button is used to open the pdf reader if there is a pdf available for the book

	

	

	

	Button(top,text="Close",font="Times 10 bold",command=top.destroy(),border=10,relief="raised",bg="red",fg="white").grid(row=3,column=2,padx=10,pady=15) # this is the button to close the top layer

	

Button(root,text="Button",command=book_info).pack() # this  is the single liner button packing

Button(root,command="exit",text="exit").pack()

root.mainloop() # running the mainloop
