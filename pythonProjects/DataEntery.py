from tkinter import *
from tkinter import ttk
from tkinter.ttk  import  Combobox
from tkinter import messagebox
import openpyxl ,xlrd
from openpyxl import workbook
import pathlib

root=Tk()
root.title("DataEntry")
root.geometry("700x400+300+200")
root.resizable(False,False)
root.configure(bg="#326273")

file=pathlib.Path('Backend_data.xlsx')
if file.exists():
    pass
else:
    file= workbook()
    sheet=file.active
    sheet['A1']="Full Name"
    sheet['B1'] = "PhoneNo"
    sheet['C1']="Age"
    sheet['D1']="Gender"
    sheet['E1'] = "Address"
    file.save('Backend_data.xlsx')
def submit():
    name=nameValue.get()
    contact=contactValue.get()
    age=ageValue.get()
    gender=gender_combobox.get()
    address=addressEntry.get(1.0 , END)

    print(name)
    print(contact)
    print(age)
    print(gender)
    print(address)

    pass
def clear():
    nameValue.set('')
    contactValue.set('')
    ageValue.set('')
    addressEntry.delete(1.0,END)



#icon
icon_image=PhotoImage(file="copy of logo.png")
root.iconphoto(False,icon_image)

#heading
Label(root,text="Please fill out this Entry form:",font="arial ",bg="#326273",fg="#fff").place(x=20,y=0)

#label
Label(root,text='Name',font=23,bg="#326273",fg="#fff").place(x=50,y=100)
Label(root,text='Contact No',font=23,bg="#326273",fg="#fff").place(x=50,y=150)
Label(root,text='Age',font=23,bg="#326273",fg="#fff").place(x=50,y=200)
Label(root,text='Gender',font=23,bg="#326273",fg="#fff").place(x=370,y=200)
Label(root,text='Address',font=23,bg="#326273",fg="#fff").place(x=50,y=250)

#Entry
nameValue=StringVar()
contactValue=StringVar()
ageValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=30,bd=2,font=15)
contactEntry=Entry(root,textvariable=contactValue,width=30,bd=2,font=15)
ageEntry=Entry(root,textvariable=ageValue,width=10,bd=2,font=15)

nameEntry.place(x=200,y=100)
contactEntry.place(x=200,y=150)
ageEntry.place(x=200,y=200)
#gender
gender_combobox=Combobox(root,value=['Male','Female'],font='arial',state='r',width=14)
gender_combobox.place(x=440,y=200)
gender_combobox.set('Male')

addressEntry =Text(root,width=50,height=4,bd=4)
addressEntry.place(x=200,y=250)


#Button
Button(root,text="Submit",bg="#326273",fg="white",width=15,height=2).place(x=200,y=350)
Button(root,text="Clear",bg="#326273",fg="white",width=15,height=2).place(x=340,y=350)
Button(root,text="Exit",bg="#326273",fg="white",width=15,height=2).place(x=480,y=350)

root.mainloop()