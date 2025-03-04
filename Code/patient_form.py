from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector


def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Chelton7755",
            database="ADBMS",
            port=3306
        )
        if conn.is_connected():
            print("DATABASE CONNECTION SUCCESSFUL")
            return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to connect to database: {err}")
        return None

# PATIENT FORM    
class Patient:
    def __init__(self, master,main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # =============ATTRIBUTES===========
        self.pat_id = IntVar()
        self.pat_ssn = IntVar()
        self.doc_id = IntVar()
        self.pat_name = StringVar()
        self.pat_dob = StringVar()
        self.pat_address = StringVar()
        self.pat_gender = StringVar()
        self.pat_BG = StringVar()
        self.pat_email = StringVar()
        self.pat_contact = IntVar()
        self.pat_contactalt = IntVar()
        self.pat_CT = StringVar()
        self.pat_C = StringVar()


        # ===============TITLE==========
        self.lblTitle = Label(self.frame, text="PATIENT REGISTRATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        # ==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # ===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_id)
        self.lblpatid.grid(row=0, column=1)
        
        self.lblPatssn = Label(self.LoginFrame, text="PATIENT SSN", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblPatssn.grid(row=1, column=0)
        self.lblPatssn  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_ssn)
        self.lblPatssn.grid(row=1, column=1)

        self.lbldocid = Label(self.LoginFrame, text="Doctor ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldocid.grid(row=2, column=0)
        self.lbldocid  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.doc_id)
        self.lbldocid.grid(row=2, column=1)

        self.lblpatname = Label(self.LoginFrame, text="NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpatname.grid(row=3, column=0)
        self.lblpatname  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_name)
        self.lblpatname.grid(row=3, column=1)
        
        self.lblbdob = Label(self.LoginFrame, text="DOB (YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblbdob.grid(row=4, column=0)
        self.lblbdob  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_dob)
        self.lblbdob.grid(row=4, column=1)
        
        self.lblgender = Label(self.LoginFrame, text="GENDER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblgender.grid(row=0, column=2)
        self.lblgender  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_gender)
        self.lblgender.grid(row=0, column=3)
        
        self.lblBG = Label(self.LoginFrame, text="BLOOD GROUP", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblBG.grid(row=1, column=2)
        self.lblBG  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_BG)
        self.lblBG.grid(row=1, column=3)
        
        self.lbleid = Label(self.LoginFrame, text="ADDRESS", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbleid.grid(row=2, column=2)
        self.lbleid  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_address)
        self.lbleid.grid(row=2, column=3)

        self.lbldoc = Label(self.LoginFrame, text="CONTACT", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldoc.grid(row=3, column=2)
        self.lbldoc  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_contact)
        self.lbldoc.grid(row=3, column=3)

        self.lbladd = Label(self.LoginFrame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbladd.grid(row=4, column=2)
        self.lbladd  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_email)
        self.lbladd.grid(row=4, column=3)

        self.button2 = Button(self.LoginFrame2, text="SUBMIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.INSERT_PAT)
        self.button2.grid(row=3, column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.UPDATE)
        self.button3.grid(row=3, column=2)
        
        self.button4 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.D_DISPLAY)
        self.button4.grid(row=3, column=3)
        
        self.button5 = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.S_DISPLAY)
        self.button5.grid(row=3, column=4)
        
        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=3, column=5)


        
    def clear(self):
        self.lblpatid.delete(0, 'end')
        self.lblPatname.delete(0, 'end')
        self.lblsex.delete(0, 'end')
        self.lblDOB.delete(0, 'end')
        self.lblbgrp.delete(0, 'end')
        self.lblCon.delete(0, 'end')
        self.lblAlt.delete(0, 'end')
        self.lbleid.delete(0, 'end')
        self.lbldoc.delete(0, 'end')
        self.lbladd.delete(0, 'end')

        # Clear the corresponding fields in the database table
        #query = "DELETE FROM your_table_name"
        #cursor.execute(query)




        

    #INSERT DATA IN PATIENT FORM
    def INSERT_PAT(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Chelton7755",
                database="ADBMS"
            )
            
            p11 = self.pat_C.get()  # Assuming this is for Patient_City or similar
            p2 = self.pat_name.get()
            p3 = self.pat_gender.get()
            p4 = self.pat_BG.get()  # Blood group if needed
            p5 = self.pat_dob.get()  # Date of birth
            p6 = self.pat_contact.get()
            p8 = self.pat_address.get()
            p9 = self.pat_CT.get()  # Assuming this is patient city or similar
            p10 = self.pat_email.get()
            p12 = self.pat_id.get()  # This is Patient_ID, make sure this is not an auto-increment field
            p13 = self.pat_ssn.get()  # Keep SSN as string

            cursor = conn.cursor()

# Check if patient already exists
            cursor.execute('SELECT * FROM PATIENT WHERE NAME = %s AND EMAIL = %s', (p2, p10))
            p = cursor.fetchall()

# If patient exists, show an error message
            if len(p) != 0:
                tkinter.messagebox.showerror("HealthCare Management System", "Patient already exists")
            else:
    # Insert patient details (without Patient_ID if it's auto-incremented)
                cursor.execute('INSERT INTO PATIENT (Patient_SSN, Doctor_ID, Name, Gender, DOB, Address, Contact, Email) '
                   'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                   (p13, p11, p2, p3, p5, p8, p6, p10))
                conn.commit()  # Ensure the changes are saved to the database
                tkinter.messagebox.showinfo("HealthCare Management System", "Patient registered successfully")
         
            self.clear()
            conn.commit()
        except mysql.connector.Error as err:
            tkinter.messagebox.showerror("Database Error", f"Error: {err}")
        

    
        

    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()

    def D_DISPLAY(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = DMenu(self.newWindow,self.master)

    def S_DISPLAY(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = SMenu(self.newWindow,self.master)
    
    def UPDATE(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = U_PAT(self.newWindow,self.master)

class U_PAT:
    def __init__(self, master,main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("HealthCare Management System")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # =============ATTRIBUTES===========
        self.pat_id = StringVar()
        self.pat_ssn = StringVar()
        self.doc_id = StringVar()
        self.pat_name = StringVar()
        self.pat_dob = StringVar()
        self.pat_address = StringVar()
        self.pat_gender = StringVar()
        self.pat_BG = StringVar()
        self.pat_email = StringVar()
        self.pat_contact = IntVar()
        self.pat_contactalt = IntVar()
        self.pat_CT = StringVar()
        self.pat_C = StringVar()


        # ===============TITLE==========
        self.lblTitle = Label(self.frame, text="PATIENT REGISTRATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        # ==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # ===========LABELS=============   
        self.lblpatid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_id)
        self.lblpatid.grid(row=0, column=1)
        
        self.lblPatname = Label(self.LoginFrame, text="PATIENT SSN", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblPatname.grid(row=1, column=0)
        self.lblPatname  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_ssn)
        self.lblPatname.grid(row=1, column=1)

        self.lblsex = Label(self.LoginFrame, text="Doctor ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblsex.grid(row=2, column=0)
        self.lblsex  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.doc_id)
        self.lblsex.grid(row=2, column=1)

        self.lblDOB = Label(self.LoginFrame, text="NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblDOB.grid(row=3, column=0)
        self.lblDOB  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_name)
        self.lblDOB.grid(row=3, column=1)
        
        self.lblbgrp = Label(self.LoginFrame, text="DOB (YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblbgrp.grid(row=4, column=0)
        self.lblbgrp  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_dob)
        self.lblbgrp.grid(row=4, column=1)
        
        self.lblCon = Label(self.LoginFrame, text="GENDER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblCon.grid(row=0, column=2)
        self.lblCon  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_gender)
        self.lblCon.grid(row=0, column=3)
        
        self.lblAlt = Label(self.LoginFrame, text="BLOOD GROUP", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblAlt.grid(row=1, column=2)
        self.lblAlt  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_BG)
        self.lblAlt.grid(row=1, column=3)
        
        self.lbleid = Label(self.LoginFrame, text="ADDRESS", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbleid.grid(row=2, column=2)
        self.lbleid  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_address)
        self.lbleid.grid(row=2, column=3)

        self.lbldoc = Label(self.LoginFrame, text="CONTACT", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldoc.grid(row=3, column=2)
        self.lbldoc  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_contact)
        self.lbldoc.grid(row=3, column=3)

        self.lbladd = Label(self.LoginFrame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbladd.grid(row=4, column=2)
        self.lbladd  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_email)
        self.lbladd.grid(row=4, column=3)

        self.button3 = Button(self.LoginFrame2, text="UPDATE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.UPDATE_PAT)
        self.button3.grid(row=3, column=2)
                
        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=3, column=5)

    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()
        self.main_window.focus_set()

    def clear(self):
        self.lblpatid.delete(0, 'end')
        self.lblpatid1.delete(0, 'end')
        self.lblPatname.delete(0, 'end')
        self.lblsex.delete(0, 'end')
        self.lblDOB.delete(0, 'end')
        self.lblbgrp.delete(0, 'end')
        self.lblCon.delete(0, 'end')
        self.lblAlt.delete(0, 'end')
        self.lbleid.delete(0, 'end')
        self.lbldoc.delete(0, 'end')
        self.lbladd.delete(0, 'end')

        # Clear the corresponding fields in the database table
        #query = "DELETE FROM your_table_name"
        #cursor.execute(query)
       



    def UPDATE_PAT(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Chelton7755",
                database="ADBMS"
            )
            
            cursor = conn.cursor()
            
            u2 = self.pat_id.get()
            u3 = self.pat_ssn.get()
            u4 = self.doc_id.get()
            u5 = self.pat_name.get()
            u6 = self.pat_gender.get()
            u7 = self.pat_dob.get()
            u8 = self.pat_BG.get()
            u9 = self.pat_email.get()
            u10 = self.pat_address.get()
            u11 = self.pat_C.get()
            u1 = self.pat_id.get()
            
            # Update patient details
            query = "UPDATE PATIENT SET PATIENT ID=%s, PATIENT SSN=%s, DOCTOR ID=%s, NAME=%s, GENDER=%s, DOB=%s, BLOOD_GROUP=%s, ADDRESS=%s, EMAIL=%s WHERE PATIENT_ID=%s"
            values = (u2, u3, u4, u5, u6, u7, u8, u10, u9, u2)
            cursor.execute(query, values)

            # Update contact numbers
            query = "UPDATE CONTACT_NO SET CONTACTNO=%s, ALT_CONTACT=%s WHERE PATIENT_ID=%s"
            values = (u6, u7, u2)
            cursor.execute(query, values)

            conn.commit()
            tkinter.messagebox.showinfo("HealthCare DATABASE SYSTEM", "Details updated into database successfully")
            self.clear()
            
        except mysql.connector.Error as err:
            tkinter.messagebox.showerror("Database Error", f"Error: {err}")

class DMenu:
    def __init__(self, master,main_window):
        global inp_d, entry1, DeleteB
        self.master = master
        self.main_window = main_window
        self.master.title("HealthCare Management System")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.del_pid = IntVar()
        self.lblTitle = Label(self.frame, text="DELETE WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        #===========LABELS=============
        self.lblpatid = Label(self.LoginFrame, text="ENTER PATIENT ID TO DELETE", font="Helvetica 14 bold",
                              bg="cadet blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.del_pid)
        self.lblpatid.grid(row=0, column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.DELETE_PAT)
        self.DeleteB.grid(row=3, column=1)
        self.DeleteB = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.Exit)
        self.DeleteB.grid(row=3, column=2)

    def DELETE_PAT(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Chelton7755",
                database="ADBMS"
            )
        global inp_d, del_pid
        cursor = conn.cursor()
        inp_d = self.del_pid.get()
        cursor.execute("SELECT * FROM PATIENT WHERE PATIENT_ID = %s", (inp_d,))
        p = cursor.fetchall()
        if len(p) == 0:
            tkinter.messagebox.showerror("HealthCare Management System", "PATIENT RECORD NOT FOUND")
            self.master.focus_set()
        else:
            cursor.execute("DELETE FROM PATIENT WHERE PATIENT_ID = %s", (inp_d,))
            conn.commit()
            tkinter.messagebox.showinfo("HealthCare Management System", "DETAILS DELETED FROM DATABASE")
            self.master.focus_set()

    def Exit(self):
        self.main_window.deiconify()
        self.main_window.focus_set()
        self.master.destroy()



import tkinter as tk
from tkinter import messagebox
from tkinter import *
import mysql.connector

class SMenu:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("HealthCare Management SystemM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.s_pid = IntVar()
        self.lblTitle = Label(self.frame, text="SEARCH WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)
        # ==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # ===========LABELS=============
        self.lblpatid = Label(self.LoginFrame, text="ENTER PATIENT ID TO SEARCH", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.entry_patid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.s_pid)
        self.entry_patid.grid(row=0, column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.SEARCH_PAT)
        self.SearchB.grid(row=0, column=1) 
        self.ClearB = Button(self.LoginFrame2, text="CLEAR", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.clear)
        self.ClearB.grid(row=0, column=2) 
        self.ExitB = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.ExitB.grid(row=0, column=3)  

    def SEARCH_PAT(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Chelton7755",
                database="ADBMS"
            )
        c1 = conn.cursor()
        inp_s = self.s_pid.get()
        c1.execute('SELECT * FROM PATIENT NATURAL JOIN CONTACT_NO WHERE PATIENT_ID = %s', (inp_s,))
        p = c1.fetchall()
        if len(p) == 0:
            messagebox.showerror("HealthCare Management System", "PATIENT RECORD NOT FOUND")
        else:
            for i in p:
                self.lblpatid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.lblpatid.grid(row=0, column=0)
        self.lblpatid  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_id)
        self.lblpatid.grid(row=0, column=1)
        
        self.lblPatname = Label(self.LoginFrame, text="PATIENT SSN", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblPatname.grid(row=1, column=0)
        self.lblPatname  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_ssn)
        self.lblPatname.grid(row=1, column=1)

        self.lblsex = Label(self.LoginFrame, text="Doctor ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblsex.grid(row=2, column=0)
        self.lblsex  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.doc_id)
        self.lblsex.grid(row=2, column=1)

        self.lblDOB = Label(self.LoginFrame, text="NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblDOB.grid(row=3, column=0)
        self.lblDOB  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_name)
        self.lblDOB.grid(row=3, column=1)
        
        self.lblbgrp = Label(self.LoginFrame, text="DOB (YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblbgrp.grid(row=4, column=0)
        self.lblbgrp  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_dob)
        self.lblbgrp.grid(row=4, column=1)
        
        self.lblCon = Label(self.LoginFrame, text="GENDER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblCon.grid(row=0, column=2)
        self.lblCon  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_gender)
        self.lblCon.grid(row=0, column=3)
        
        self.lblAlt = Label(self.LoginFrame, text="BLOOD GROUP", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblAlt.grid(row=1, column=2)
        self.lblAlt  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_BG)
        self.lblAlt.grid(row=1, column=3)
        
        self.lbleid = Label(self.LoginFrame, text="ADDRESS", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbleid.grid(row=2, column=2)
        self.lbleid  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_address)
        self.lbleid.grid(row=2, column=3)

        self.lbldoc = Label(self.LoginFrame, text="CONTACT", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldoc.grid(row=3, column=2)
        self.lbldoc  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_contact)
        self.lbldoc.grid(row=3, column=3)

        self.lbladd = Label(self.LoginFrame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbladd.grid(row=4, column=2)
        self.lbladd  = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_email)
        self.lbladd.grid(row=4, column=3)
        
    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()
        self.main_window.focus_set()

    def clear(self):
        # Clear the patient ID entry
        self.entry_patid.delete(0, 'end')
        
        # Clear the labels that display the search results, if they exist
        if hasattr(self, 'dis1'):
            self.dis1.config(text="")
        if hasattr(self, 'dis2'):
            self.dis2.config(text="")
        if hasattr(self, 'dis3'):
            self.dis3.config(text="")
        if hasattr(self, 'dis4'):
            self.dis4.config(text="")
        if hasattr(self, 'dis5'):
            self.dis5.config(text="")
        if hasattr(self, 'dis6'):
            self.dis6.config(text="")
        if hasattr(self, 'dis7'):
            self.dis7.config(text="")
        if hasattr(self, 'dis8'):
            self.dis8.config(text="")
        if hasattr(self, 'dis9'):
            self.dis9.config(text="")
        if hasattr(self, 'dis10'):
            self.dis10.config(text="")
