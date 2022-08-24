from tkinter import *
from tkinter import messagebox as msg
from pymongo import MongoClient
import time

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.books5
books = db.bklist

root = Tk()
root.title("Library management system")
root.geometry("380x650")
root.config(bg="#C0FF2E")


# Defining- all the functions here

#this function is for the real updation of time
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
	day_label=Label(root,text=z,bg="lightyellow",fg="red",font="Times 20 bold italic")
	day_label.pack(padx=10,pady=40)


#All the books available in the library will be displayed over here
def showall():
    show_all_root = Toplevel(root,bg="#F7F257")
    show_all_root.title("All books")
    show_all_root.geometry("300x600");n=0
    for book in books.find():
        obj = {}
        obj["bookname"] = book["bookname"]
        obj["author"] = book["author"]
        s = StringVar()
        s.set(obj["bookname"] + " by "+ obj["author"])
        lb = Label(show_all_root,textvariable=s,font="Times 15 bold italic",bg="#F7F257",fg="black")
        lb.pack(padx=10,pady=10,anchor="nw")
    
    #scrollbar=Scrollbar(show_all_root)
    #scrollbar.pack(anchor="e",fill="y")
    # scrollbar.config(command=yview)


#All books that can be borrowed will be displayed over here
def showav():
    show_all_root = Toplevel(root,bg="#FFB45E")
    show_all_root.title("The available books are shown here")
    show_all_root.geometry("300x600")
    for book in books.find({"availability":"available"}):
        obj = {}
        obj["bookname"] = book["bookname"]
        obj["author"] = book["author"]
        s = StringVar()
        s.set(obj["bookname"] + " by "+ obj["author"])
        lb = Label(show_all_root,textvariable=s,font="Times 15 bold italic",bg="#FFB45E")
        lb.pack(padx=10,pady=10,anchor="nw")

bookname = StringVar()
book_author = StringVar()
book_price = StringVar()


#Adding a new book to the database
def book_add():
	top=Toplevel(root,bg="#87E9FF");top.title("Buy stocks")
	top.geometry("400x300")
	Label(top,text="Enter the name of the book :",bg="#87E9FF",font="Times 15 bold italic").pack(padx=5,pady=5)
	name_entry = Entry(top,textvar=bookname,font="Times 15 bold italic",border=5,relief="sunken")
	name_entry.pack()
	Label(top,text="Enter the name of the author:",bg="#87E9FF",font="Times 15 bold italic").pack(padx=5,pady=5)
	author_entry = Entry(top,textvar=book_author,font="Times 15 bold italic",border=5,relief="sunken")
	author_entry.pack()
	Label(top,text="Enter the price of the book :",bg="#87E9FF",font="Times 15 bold italic").pack(padx=5,pady=5)
	price_entry = Entry(top,textvar=book_price,font="Times 15 bold italic",border=5,relief="sunken")
	price_entry.pack()
    # this button is to destroy the top level window


	def bookadd_to_database():
            doc = {}
            a  = name_entry.get()
            b = author_entry.get()
            c = price_entry.get()
            doc['bookname'] = a
            doc['author'] = b
            doc['cost'] = c
            doc['availability'] = 'available'
            books.insert_one(doc)
            #Clear the entry widgets after pressing submit button
            name_entry.delete(0, END)
            author_entry.delete(0, END)
            price_entry.delete(0, END)
            msg.showinfo("Sucess","Book Added to Database")
	Button(top,text="Submit",command=bookadd_to_database,bg="red",fg="white",font="Times 15 bold italic",border=5,relief="raised").pack(padx=5,pady=20)

#Returnig a book that had been borrowed
returnbook=StringVar()
def book_return():
	top=Toplevel(root,bg="#9861FF");top.title("Return book")
	#  top.geometry("400x300")
	Label(top,text="Enter the name of the book you want to return:",font="Times 15 bold italic",bg="#9861FF",fg="white").pack()
	name_entry = Entry(top,textvar=returnbook,font="Times 15 bold italic",border=5,relief="sunken")
	name_entry.pack(padx=10,pady=10)
	def return_book():
            name=(returnbook.get()).strip()
            counter = 0
            obj = {}
            for temp_book in books.find({"bookname": name}):
                obj["bookname"] = temp_book["bookname"]
                counter = counter + 1
            if counter == 0:
                msg.showinfo("Error", "Book not found")
            else:
                books.update_one({"bookname":obj["bookname"]},{"$set":{"availability":"available"}},upsert=False)
                msg.showinfo("Success", "Book returned")
                #Clears the entry widgets
                name_entry.delete(0, END)
	Button(top,text="Submit",command=return_book,font="Times 15 bold italic",bg="red",fg="white",border=5,relief="raised").pack(padx=10,pady=10)

#Borrowing an available book
issuebook=StringVar()
def book_issue():
	top=Toplevel(root,bg="#7DFAA7");top.title("Issue books")
	#  top.geometry("400x300")
	Label(top,text="  Enter the name of the book you want to issue:  ",font="Times 15 bold italic",bg="#7DFAA7",fg="black").pack(padx=10,pady=5)
	name_entry = Entry(top,textvar=issuebook,font="Times 15 bold italic",border=5,relief="sunken")
	name_entry.pack(pady=10)
	def issue_book():
            name=(issuebook.get()).strip()
            counter = 0
            obj = {}
            for temp_book in books.find({"bookname": name}):
                obj["bookname"] = temp_book["bookname"]
                counter = counter + 1
            if counter == 0:
                msg.showinfo("Error", "Book not found")
            else:
                books.update_one({"bookname":obj["bookname"]},{"$set":{"availability":"unavailable"}},upsert=False)
                msg.showinfo("Success", "Book issued")

	Button(top,text="Submit",command=issue_book,font="Times 15 bold italic",bg="red",fg="white",border=5,relief="raised").pack(padx=10,pady=10)

main_label = Label(root,text="LIONS VIDYA MANDIR",font="Times 20 bold italic underline",bg="#C0FF2E")
# main_lablel.grid(row=0,column=0,columnspan=5)
main_label.pack()

main_label = Label(root,text="Library Management System",font="Times 20 bold italic ",bg="#C0FF2E")
# main_lablel.grid(row=0,column=0,columnspan=5)
main_label.pack()



showall_button = Button(root,text="       Show all books       ",command=showall,font="Times 15 bold italic",border=10,relief="raised",bg="#26B0FF",fg="white")
showall_button.pack(padx=10,pady=10)
# showall_button. grid(row=1,column=1)
showav_button = Button(root,text="      Available books       ",command=showav,font="Times 15 bold italic",border=10,relief="raised",bg="#A1CDFF")
showav_button.pack(padx=10,pady=10)
# showav_button.grid(row=2,column=1)
issue_button = Button(root,text="        Isuue a book         ",command=book_issue,font="Times 15 bold italic",border=10,relief="raised",bg="#26B0FF",fg="white")
issue_button.pack(padx=10,pady=10)
# issue_button.grid(row=3,column=1)
return_button = Button(root,text="       Return a book        ",command=book_return,font="Times 15 bold italic",border=10,relief="raised",bg="#A1CDFF")
return_button.pack(padx=10,pady=10)
# return_buton.grid(row=4,column=1)
buy_stocks_btn = Button(root,text="         Buy Stocks           ",command=book_add,font="Times 15 bold italic",border=10,relief="raised",bg="#26B0FF",fg="white")
# buy_stocks_btn.grid(row=5,column=1)
buy_stocks_btn.pack(padx=10,pady=10)
# this button is to close the root window
close_button = Button(root,text="           Close          ",command=root.destroy,font="Times 15 bold italic",border=10,relief="raised",bg="#A1CDFF").pack(padx=10,pady=10)

main_label = Label(root,text="Designed & Coded by \nPartha Sarathi Dey & Rohan Dey",font="Times 10 bold italic",bg="#C0FF2E")
# main_lablel.grid(row=0,column=0,columnspan=5)
main_label.pack(pady=10,anchor="se")
root.mainloop()