import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Establish database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chelton7755",  # Replace with your actual password
    database="ADBMS",   # Ensure this matches your database name
    port=3306
)

cursor = conn.cursor()
print("DATABASE CONNECTION SUCCESSFUL")

class Record:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("HealthCare Management System")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")

        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.lblTitle = tk.Label(self.frame, text="RECORDS MENU", font=("Helvetica", 20, "bold"), bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        self.LoginFrame = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        buttons = [
            ("1. PATIENT RECORD", self.open_patient_window),
            ("2. PATIENT BILL RECORD", self.open_bill_window),
            ("3. DOCTOR RECORD", self.open_doctor_window),
            ("4. MEDICINE RECORD", self.open_medicine_window),
            ("5. TREATMENT RECORD", self.open_treatment_window),
            ("6. EXIT", self.Exit)
        ]

        for i, (text, command) in enumerate(buttons):
            button = tk.Button(self.LoginFrame, text=text, width=30, font=("Helvetica", 14, "bold"), bg="cadet blue", command=command)
            button.grid(row=i, column=0, pady=10)

    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()

    def open_patient_window(self):
        self.master.withdraw()
        PatientWindow(self.master)

    def open_doctor_window(self):
        self.master.withdraw()
        DoctorWindow(self.master)

    def open_bill_window(self):
        self.master.withdraw() 
        BillWindow(self.master)

    def open_medicine_window(self):
        self.master.withdraw()
        MedicineWindow(self.master)

    def open_treatment_window(self):
        self.master.withdraw()
        TreatmentWindow(self.master)

class BaseRecordWindow:
    def __init__(self, master):
        self.main_window = master
        self.master = tk.Toplevel(master)
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")

        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.lblTitle = tk.Label(self.frame, text=self.window_title, font=("Helvetica", 20, "bold"), bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.searchFrame = tk.Frame(self.frame, bg="cadet blue")
        self.searchFrame.grid(row=1, column=0, pady=20)

        self.lblSearch = tk.Label(self.searchFrame, text="Search By", font=("Helvetica", 14), bg="cadet blue", width=30, height=5)
        self.lblSearch.grid(row=0, column=0, padx=10)

        self.searchBy = tk.StringVar()
        self.cmbSearch = ttk.Combobox(self.searchFrame, textvariable=self.searchBy, state='readonly', font=("Helvetica", 14), width=30)
        self.cmbSearch['values'] = self.search_values
        self.cmbSearch.grid(row=0, column=1, padx=10)

        self.searchTerm = tk.StringVar()
        self.txtSearch = tk.Entry(self.searchFrame, textvariable=self.searchTerm, font=("Helvetica", 14), width=50)
        self.txtSearch.grid(row=0, column=2, padx=10)

        self.btnSearch = tk.Button(self.searchFrame, text="Search", font=("Helvetica", 14, "bold"), width=15, command=self.search_records)
        self.btnSearch.grid(row=1, column=1, padx=10)

        self.btnExit = tk.Button(self.searchFrame, text="Exit", font=("Helvetica", 14, "bold"), width=15, command=self.exit)
        self.btnExit.grid(row=1, column=2, pady=20)

        self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings')
        for col in self.columns:
            self.tree.heading(col, text=col.capitalize())
        self.tree.grid(row=2, column=0, padx=20, pady=20)

    def exit(self):
        self.master.focus_set()
        self.master.destroy()
        self.main_window.deiconify()

    def search_records(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def populate_tree(self, rows, columns):
        # Clear previous entries in the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Configure the Treeview columns and headings
        self.tree["columns"] = columns
        for col in columns:
            self.tree.heading(col, text=col.capitalize())  # Capitalize column headings

        # Insert data into the Treeview
        for row in rows:
            self.tree.insert("", "end", values=row)

class PatientWindow(BaseRecordWindow):
    window_title = "PATIENT RECORDS"
    search_values = ("Patient ID", "Patient Name")
    columns = ("patient_id","Patient_SSN", "Doctor_ID","Name", "GENDER","ADDRESS", "CONTACT", "EMAIL")

    def search_records(self):
        search_by = self.searchBy.get()
        search_term = self.searchTerm.get()

        if not search_by or not search_term:
            messagebox.showwarning("Input Error", "Please select a search criterion and enter a search term.")
            self.master.focus_set()
            return

        try:
            cursor.callproc('SearchPatients', (search_by, search_term))
            rows = []
            for result in cursor.stored_results():
                rows = result.fetchall()
            
            if rows:
                self.populate_tree(rows, self.columns)
            else:
                messagebox.showinfo("No Records", "No records found matching the search criteria.")
                self.master.focus_set()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            self.master.focus_set()

class DoctorWindow(BaseRecordWindow):
    window_title = "DOCTOR RECORDS"
    search_values = ("Doctor ID", "Doctor Name")
    columns = ("Doctor_id","Doctor_SSN", "Name", "Phone")

    def search_records(self):
        search_by = self.searchBy.get()
        search_term = self.searchTerm.get()

        if not search_by or not search_term:
            messagebox.showwarning("Input Error", "Please select a search criterion and enter a search term.")
            self.master.focus_set()
            return
        try:
            cursor.callproc('SearchDoctors', (search_by, search_term))
            rows = []
            for result in cursor.stored_results():
                rows = result.fetchall()
            if rows:
                self.populate_tree(rows, self.columns)
            else:
                messagebox.showinfo("No Records", "No records found matching the search criteria.")
                self.master.focus_set()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            self.master.focus_set()

class BillWindow(BaseRecordWindow):
    window_title = "PATIENT BILL RECORDS"
    search_values = ("Patient ID", "Patient Name")
    columns = ("bill_id","patient_id", "bill")

    def search_records(self):
        search_by = self.searchBy.get()
        search_term = self.searchTerm.get()

        if not search_by or not search_term:
            messagebox.showwarning("Input Error", "Please select a search criterion and enter a search term.")
            self.master.focus_set()
            return

        try:
            cursor.callproc('SearchBills', (search_by, search_term))
            rows = []
            for result in cursor.stored_results():
                rows = result.fetchall()
            
            if rows:
                self.populate_tree(rows, self.columns)
            else:
                messagebox.showinfo("No Records", "No records found matching the search criteria.")
                self.master.focus_set()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            self.master.focus_set()

class MedicineWindow(BaseRecordWindow):
    window_title = "MEDICINE RECORDS"
    search_values = ("Patient ID", "Medicine Name")
    columns = ("m_no", "patient_id", "medicine_name", "m_cost", "m_qty", "m_date")

    def search_records(self):
        search_by = self.searchBy.get()
        search_term = self.searchTerm.get()

        if not search_by or not search_term:
            messagebox.showwarning("Input Error", "Please select a search criterion and enter a search term.")
            self.master.focus_set()
            return

        try:
            cursor.callproc('SearchMedicines', (search_by, search_term))
            rows = []
            for result in cursor.stored_results():
                rows = result.fetchall()
            
            if rows:
                self.populate_tree(rows, self.columns)
            else:
                messagebox.showinfo("No Records", "No records found matching the search criteria.")
                self.master.focus_set()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            self.master.focus_set()

class TreatmentWindow(BaseRecordWindow):
    window_title = "TREATMENT RECORDS"
    search_values = ("Patient ID", "Patient Name", "Doctor ID")
    columns = ("t_no", "patient_id", "doc_id", "treatment", "treatment_code", "t_cost", "t_date")

    def search_records(self):
        search_by = self.searchBy.get()
        search_term = self.searchTerm.get()

        if not search_by or not search_term:
            messagebox.showwarning("Input Error", "Please select a search criterion and enter a search term.")
            self.master.focus_set()
            return

        try:
            cursor.callproc('SearchTreatments', (search_by, search_term))
            rows = []
            for result in cursor.stored_results():
                rows = result.fetchall()
            
            if rows:
                self.populate_tree(rows, self.columns)
            else:
                messagebox.showinfo("No Records", "No records found matching the search criteria.")
                self.master.focus_set()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            self.master.focus_set()

