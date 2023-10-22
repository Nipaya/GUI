import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from dbhelper import *

class Userlogin():
    def __init__(self):
        self.root = Tk()
        self.root.title("Nipaya, Dione Louis")
        self.root.geometry("590x500")
        self.root.resizable(False,False)

        self.frame = Frame(self.root, bd = 20)
        self.frame.grid()

        #LABEL

        self.lbl_idno = Label(self.frame, text = "IDNO :", font = "Verdana, 20", bd = 20)
        self.lbl_idno.grid(row = 0, column = 0)

        self.lbl_Firstname = Label(self.frame, text = "LASTNAME :", font = "Verdana, 20", bd = 20)
        self.lbl_Firstname.grid(row = 1, column = 0)

        self.lbl_Lastname = Label(self.frame, text = "FIRSTNAME :", font = "Verdana, 20", bd = 20)
        self.lbl_Lastname.grid(row = 2, column = 0)

        #COMBOBOX->COURSE
        self.lbl_Course = Label(self.frame, text = "COURSE :", font = "Verdana, 20", bd = 20)
        self.lbl_Course.grid(row = 3, column = 0)

        c = tk.StringVar()
        self.Course = ttk.Combobox(self.frame, width = 19, textvariable = c, font = "Verdana, 14")
        self.Course['values'] = ('BSIT', 'BSCS', 'BSCPE')
        self.Course.grid(row = 3, column = 1)
        self.Course.current()

        #COMBOBOX->LEVEL
        self.lbl_Level = Label(self.frame, text = "LEVEL", font = "Verdana, 20", bd = 20)
        self.lbl_Level.grid(row = 4, column = 0)
        l = tk.StringVar()
        self.Level = ttk.Combobox(self.frame, width = 19, textvariable = l, font = "Verdana, 14")
        self.Level['values'] = ('1', '2', '3', '4') 
        self.Level.grid(row = 4, column = 1)
        self.Level.current()
        
        #

        #ENTRY
        self.txt_idno = Entry(self.frame, text = "idno", font = "Verdana,20")
        self.txt_idno.grid(row=0,column=1)
        
        self.txt_Lastname = Entry(self.frame, text = "Lastname", font = "Verdana,20")
        self.txt_Lastname.grid(row=1,column=1)

        self.txt_Firstname = Entry(self.frame, text = "Firstname", font = "Verdana,20")
        self.txt_Firstname.grid(row=2,column=1)

        #BUTTONS
        self.button_find = Button(self.frame, text="Find", font="Verdana,20", foreground='white', bg="Black", command=self.find_idno)
        self.button_find.grid(row=0,column=3,columnspan=2, padx=10,  pady=20)

        #
        self.Button = Frame(self.frame, bd=20)
        self.Button.grid(row=15,column=0, columnspan=20)

        self.button_new = Button(self.Button, text="New", font="Verdana,20", foreground='white', bg="Black", command=self.New)
        self.button_new.grid(row=6,column=0, padx=15)

        self.button_save = Button(self.Button, text="Save", font="Verdana,20", foreground='white', bg="Black", command=self.savestudent)
        self.button_save.grid(row=6,column=2, padx=15)

        self.button_delete = Button(self.Button, text="Delete", font="Verdana,20", foreground='white', bg="Black", command=self.delete)
        self.button_delete.grid(row=6,column=4, padx=15)

        self.button_update = Button(self.Button, text="Update", font="Verdana,20", foreground='white', bg="Black", command=self.update)
        self.button_update.grid(row=6,column=6, padx=15)

        self.root.eval("tk::PlaceWindow . center")
        self.root.mainloop()

    def clearfield(self):
        self.txt_idno.delete(0, 'end')
        self.txt_Lastname.delete(0, 'end')
        self.txt_Firstname.delete(0, 'end')
        self.Course.delete(0,'end')
        self.Level.delete(0,'end')

    def find_idno(self):
        idno = self.txt_idno.get()
        if not idno:
            messagebox.showerror("ERROR","PLEASE INPUT BEFORE PRESSING FIND!!!")
            return

        data = getrecord('student', idno=idno)
        if not data:
            messagebox.showinfo("Student", f"Student: {idno} Available")
            messagebox.showinfo("Student", "please proceed....")

            return
        messagebox.showinfo("Student", "Student Found!")

    def savestudent(self):
        try:
            idno:str = self.txt_idno.get()
            lastname:str=self.txt_Lastname.get()
            firstname:str=self.txt_Firstname.get()
            course:str = self.Course.get()
            level:str = self.Level.get()

            okey:bool = addrecord('student', idno=idno, lastname=lastname, firstname=firstname,course=course,level=level)
            if okey:
                messagebox.showinfo("login status","LOGIN ACCEPTED")
                self.clearfield()
            else:
                messagebox.showerror("login status", "Login Fail!")
                self.clearfield()
        except:
            messagebox.showerror("Error","Student ID already exist.")
            self.clearfield()

    def delete(self):
        student_id = self.txt_idno.get()

        if student_id:
            confirmation = messagebox.askyesno("Confirmation", "Do You Really Really Want To Delete This Student?")
            if confirmation:
                deleterecord('student', idno=student_id)
                messagebox.showinfo("UPDATE:", "Student Deleted")
            else:
                messagebox.showerror("UPDATE", "Deletion Canceled.")        
        else:
            messagebox.showerror("ERROR","Deletion Canceled.")

    def update(self):
        try:
            confirm = messagebox.askyesno("Confirmation","Would you like to update this student?")
            idno:str = self.txt_idno.get()
            lastname:str=self.txt_Lastname.get()
            firstname:str=self.txt_Firstname.get()
            course:str = self.Course.get()
            level:str = self.Level.get()

            okey:bool = updaterecord('student', idno=idno, lastname=lastname, firstname=firstname,course=course,level=level)
            if okey:    
                if confirm:
                    messagebox.showinfo("Student","STUDENT UPDATED")
                    self.clearfield()
                else:
                    messagebox.showerror("ERROR","UPDATING THIS STUDENT FAILED")
            else:
                messagebox.showerror("ERROR","UPDATING THIS STUDENT FAILED")
        except:
            messagebox.showerror("Error","Student ID already exist.")

    def New(self):
        Userlogin()
    


def main()->None:
    Userlogin()
if __name__ == "__main__":
    main()