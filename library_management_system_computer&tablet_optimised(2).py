# importing all the packages
from tkinter import *
import pymongo 
from datetime import date
import time
textcolor="red"
# connecting with data base
client = pymongo.MongoClient("mongodb://127.0.0.1:27017") # client to establish connection with the database
db = client.books4 #There is a database in my mongo db localhost named books4. db variable acesses the path to that database

books = db.bklist #There is a collection in my books4 database named bklist. It stores the documents(fields and values for all lists)

# all the functions for this program are done here


def timeupdate(): # this function is for the real time updation of time
	global day_label
	l=((time.asctime(time.localtime(time.time()))).rstrip()).split(" ")
	day=l[0]
	if day=="Mon":
		day="Monday"
	if day=="Tue":
		day="Tuesday"
	if day=="Wed":
		day="Wednesday"
	if day=="Thu":
		day="Thursday"
	if day=="Fri":
		day="Friday"
	if day=="Sat":
		day="Saturday"
	if day=="Sun":
		day="Sunday"
#print(l)

	month=l[1].lower()
	if month=="jan":
		month="January"
	if month=="feb":
		month="February"
	if month=="mar":
		month="March"
	if month=="jun":
			month="June"
	if month=="jul":
		month="July"
	if month=="aug":
		month="August"
	if month=="sep":
		month="September"
	if month=="oct":
		month="October"
	if month=="nov":
		month="November"
	if month=="dec":
		month="December"
	if month=="apr":
		month="April"
	if month=="may":
		month="May"
	date=l[2]
	year=l[len(l)-1]


	timing=(l[3])[0:5]
	hrs = int(timing[0:2])
	minute = int(timing[3: ])
	x=" am"
	
	if hrs>12:
		hrs=hrs-12
		x=" pm"
	timing=str(hrs)+":"+str(minute)+x
	z=("Its, "+timing+"\n"+day+"\n"+str(date)+" "+month+" "+str(year))
	day_label=Label(search_books,text=z,bg="lightyellow",fg=textcolor,font="Times 20 bold italic")
	day_label.pack(padx=10,pady=40)

#All the books available in the library will be displayed over here
def showall():
    show_all_root = Toplevel(info_books)
    show_all_root.title("All books")
    show_all_root.geometry("350x350")
    for book in books.find():
        obj = {}
        obj["bookname"] = book["bookname"]
        obj["author"] = book["author"]
        s = StringVar()
        s.set(obj["bookname"] + " by "+ obj["author"])
        lb = Label(show_all_root,textvariable=s)
        lb.pack()
        Button(show_all_root,test="exit",command="exit").pack()
    # show_all_root.mainloop()

""" books_availability_status=""
def search_book():
    #Declared the first string variable to be used in the search
    String = StringVar()
    inp = input("Enter the book name : ").title()
    # inp2 = input("Enter the author name : ").title()
    n = 0
    for book in books.find({"bookname":inp}):
        #Collecting the book details fro the database
        obj = {}
        obj["bookname"] = book["bookname"]
        obj["author"] = book["author"]
        obj["genre"] = book["genre"]
        obj["code"] = book["code"]
        obj["standard"] = book["standard"]
        obj["cost"] = book["cost"]
        obj["availability"] = book["availability"]
        n = n + 1
    if n > 0:
        #Logical execution in case of a book is found
        String.set("Book found!")
        string2 = StringVar()
        print("Book found. \n")
        if obj["availability"] == "available":
            #Logical execution in case of a book is available
            string2.set("Book is available for issuing.")
            print("The book is currently available : ")
            string2.set("Bookname : " + obj["bookname"] + "\nAuthor : " + obj["author"] + "\nGenre : " + obj["genre"] + "\nCode : " + obj["code"] + "\nStandard : " + obj["standard"] + "\nCost : " + obj["cost"] + "\n")
            print("Book name : ",obj["bookname"],"\nAuthor : ",obj["author"],"\nGenre : ",obj["genre"],"\nCode : ",obj["code"],"\nStandard : ",obj["standard"],"\nCost : ",obj["cost"],"\n")
        else:
            #If book is found but is not available
            string2.set("Book is not available for issuing.")
            print("The book is currently unavailable . ")
    else:
        #Logical execution in case of a book is not found
        String.set("Book not found! Please recheck the spelling of the book.")
        print("Book not found. Please check the spelling of the book.")
 """
def add_book():
	pass

def click():
	pass

def lost():
	pass

#def showall():
#	pass

def submit():
	pass

def availability():
	pass






# creating the root widget
root = Tk()
root.geometry("400x300")
root.minsize(400,300)
root.title("Library management software")

# defining and packing all the frames
mainframe = Frame(root,relief="raised") # this is the mainframe widget
mainframe.pack(fill="both") # packing of the mainframe


titlebar = Frame(mainframe,bg="lightblue",border=5,relief="raised") # this the titlebar
titlebar.pack(side="top",fill="x") # packing of the title bar

search_books=Frame(mainframe,bg="lightyellow",border=5,relief="raised") # this frame is to pack the searchbox 
search_books.pack(side="left",fill="both") # packing the search_books frame

sorting_buttons=Frame(mainframe,bg="lightgreen",border=5,relief="raised") # this frame is for all the buttons regarding te showing of the books
sorting_buttons.pack(side="right",fill="y") # packing the sorting_buttons frame

info_books=Frame(mainframe,bg="black",border=5,relief="raised") # this frame is for showing the books
info_books.pack(anchor="s",fill="both") # packing the info_books frame

"""scrollbar=Scrollbar(info_books)
scrollbar.pack(side="right",fill="y")
# scrollbar.config(command=yview)"""


# content of the titlebar frame
Label(titlebar, text = " Library management",bg="lightblue",fg=textcolor,font="Times 20 bold italic").pack(side="left") # single liner packing of the Title of the program

Button(titlebar,text="Exit",bg=textcolor,fg="white",font="comicsansms 15 bold italic",border=5,relief="sunken",command="exit").pack(side="right") # single liner packing of the exit button



# content of the search_books frame
books = StringVar() # declaring the books variable to store the name of the books given by the user

Label(search_books, text = "Welcome to \nVirtual Library of \nLions Vidya Mandir",bg="lightyellow",fg=textcolor,font="Times 20 bold italic ").pack(padx=20,pady=10) # single liner packing of the Title of the program

Label(search_books, text = "Search",bg="lightyellow",fg=textcolor,font="Times 19 bold italic underline").pack(anchor="nw",padx=20,pady=20) # single liner packing of the Title of the program

searchbox = Entry(search_books,textvar=books, border=10, relief="sunken", bg="white",fg="blue",width=20,font="Times 15 bold italic") # this the searchbox 
searchbox.pack(padx=20,pady=10) # packing the search box

Button(search_books,text="Submit",bg=textcolor,fg="white",font="comicsansms 15 bold italic",border=10,relief="sunken",command=submit).pack(padx=10,pady=10) # single liner packing of the exit button

timeupdate()

# content of the sorting_buttons frame
Label(sorting_buttons, text = "Show",bg="lightgreen",fg=textcolor,font="Times 19 bold italic underline").grid(row=0,column=0,pady=20)
# .pack(padx=20,pady=20,anchor="nw")

b1=Button(sorting_buttons,text="  All the books  ",bg="yellow",fg="blue",borderwidth=10,font="comicsansms 15 bold italic",command=showall)
b1.grid(row=1,column=0,pady=10)
#b1.pack(pady=10,anchor="w")
# b1.bind("<Button->")

b2=Button(sorting_buttons,text="Available books",bg="yellow",fg="blue",borderwidth=10,font="comicsansms 15 bold italic" )
b2.grid(row=2,column=0,pady=10,padx=30)
# b2.pack(pady=10,anchor="w")
b2.bind("<Button->",availability)

b3=Button(sorting_buttons,text=" Return a book ",bg="yellow",fg="blue",borderwidth=10,font="comicsansms 15 bold italic" )
b3.grid(row=3,column=0,pady=10)
#b3.pack(pady=10,anchor="w")
b3.bind("<Button->",click)

b4=Button(sorting_buttons,text="   Buy stocks    ",bg="yellow",fg="blue",borderwidth=10,font="comicsansms 15 bold italic" )
b4.grid(row=4,column=0,pady=10)
#b4.pack(pady=10,anchor="w")
b4.bind("<Button->",click)

"""b5=Button(sorting_buttons,text="    Book Lost    ",bg="yellow",fg="blue",borderwidth=10,font="comicsansms 15 bold italic" )
b5.grid(row=5,column=0,pady=10)
#b5.pack(pady=10,anchor="w")
b5.bind("<Button->",lost)"""

# content of the info_books frame
Label(info_books,text="Books",bg="black",fg="white",font="Times 19 underline bold italic").pack(anchor="nw",padx=20,pady=20)

display_books=Frame(info_books,bg="black",relief="raised",border=10)
display_books.pack(fill="x",side="top")
Label(info_books,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",bg="black",fg="black").pack()
info_books_statusbar=Frame(info_books,bg="black",relief="raised",border=10)
info_books_statusbar.pack(side="bottom",fill="x")

testing_var=Label(display_books,text="All the books will be shown here",bg="black",fg="white",font="Times 19 underline bold italic").pack(fill="both",side="top")

statusbar_title=Label(info_books_statusbar,text="Page 1",bg="black",fg="white",font="Times 19 underline bold italic").pack()

status_back=Button(info_books_statusbar,text="  <<  ",bg="red",fg="white",font="comicsansms 10 bold",border=10,relief="raised")
status_back.pack(side="left",padx=20)



# status_forward=Button(info_books_statusbar,text="  >>  ",bg="red",fg="white",font="comicsansms 10 bold",border=10,relief="raised",command=book_details)
# status_forward.pack(side="right",padx=20)

root.mainloop() # running the mainloop() for tkinter program execution