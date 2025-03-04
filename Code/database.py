import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chelton7755",  # Replace with your actual password
    database="ADBMS",   # Ensure this matches your database name
    port=3306
)

print("DATABASE CONNECTION SUCCESSFUL")

c = conn.cursor()

# Drop existing tables if they exist
c.execute("DROP TABLE IF EXISTS APPOINTMENT")
c.execute("DROP TABLE IF EXISTS TREATMENT")
c.execute("DROP TABLE IF EXISTS PATIENT")
c.execute("DROP TABLE IF EXISTS DOCTOR")

# Create tables
c.execute("""
    CREATE TABLE PATIENTS (
        PATIENT_ID INT PRIMARY KEY AUTO_INCREMENT,
        NAME VARCHAR(20) NOT NULL,
        GENDER VARCHAR(10) NOT NULL,
        BLOOD_GROUP VARCHAR(5) NOT NULL,
        DOB DATE NOT NULL,
        ADDRESS VARCHAR(100) NOT NULL,
        CONSULT_TEAM VARCHAR(50) NOT NULL,
        EMAIL VARCHAR(50) NOT NULL,
        `CONDITION` VARCHAR(30) NOT NULL
    )
""")
print("PATIENT TABLE CREATED SUCCESSFULLY")

c.execute("""
CREATE TABLE Doctor(
    Doctor_ID INT NOT NULL AUTO_INCREMENT,
    Doctor_SSN VARCHAR(11) NOT NULL,
    Name VARCHAR(30) NOT NULL,
    Phone_Number VARCHAR(10) NOT NULL,
    PRIMARY KEY(Doctor_ID),
    CHECK (CHAR_LENGTH(Phone_Number) = 10),
    CHECK (Doctor_SSN REGEXP '^\d{9}$') -- Optional: Validates SSN format (replace with actual pattern as needed)
);
""")

c.execute("""
CREATE TABLE IF NOT EXISTS WORKS (
    DEPT_ID INT,
    EMP_ID INT,
    ROLE VARCHAR(20),
    SHIFT_DETAILS VARCHAR(30),
    FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT (DEPT_ID) ON DELETE SET NULL,
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE (EMP_ID) ON DELETE CASCADE
)
""")
print("WORKS TABLE CREATED SUCCESSFULLY")


c.execute("""
    CREATE TABLE TREATMENT (
    T_NO INT AUTO_INCREMENT PRIMARY KEY,
    PATIENT_ID INT,
    DOC_ID INT,
    TREATMENT VARCHAR(100) NOT NULL,
    TREATMENT_CODE VARCHAR(30) NOT NULL,
    T_COST INT NOT NULL,
    T_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (DOC_ID) REFERENCES EMPLOYEE (EMP_ID) ON DELETE SET NULL,
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
)
""")
print("TREATMENT TABLE CREATED SUCCESSFULLY")

c.execute("""
CREATE TABLE IF NOT EXISTS CONSULT (
    PATIENT_ID INT,
    EMP_ID INT,
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE,
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE (EMP_ID) ON DELETE CASCADE,
    PRIMARY KEY(PATIENT_ID,EMP_ID)
)
""")
print("CONSULT TABLE CREATED SUCCESSFULLY")

c.execute("""
    CREATE TABLE MEDICINE (
        M_NO INT AUTO_INCREMENT PRIMARY KEY,
        PATIENT_ID INT,
        MEDICINE_NAME VARCHAR(100) NOT NULL,
        M_COST INT NOT NULL,
        M_QTY INT NOT NULL,
        M_DATE DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
    )
""")
print("MEDICINE TABLE CREATED SUCCESSFULLY")

c.execute("""
    CREATE TABLE ROOM (
    PATIENT_ID INT NOT NULL,
    ROOM_NO VARCHAR(20) PRIMARY KEY,
    ROOM_TYPE VARCHAR(10) NOT NULL,
    RATE INT NOT NULL,
    DATE_ADMITTED DATE,
    DATE_DISCHARGED DATE,
    PAY_STATUS ENUM('YES', 'NO'),
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
)
""")
print("ROOM TABLE CREATED SUCCESSFULLY")

c.execute("""
    CREATE TABLE BILL (
        PATIENT_ID INT NOT NULL,
        BILL INT,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT (PATIENT_ID) ON DELETE CASCADE
    )
""")


# Trigger to check room allocation before insert
c.execute("""
    CREATE TRIGGER check_room_allocation_before_insert
BEFORE INSERT ON ROOM
FOR EACH ROW
BEGIN
    DECLARE room_count INT;
    DECLARE patient_count INT;

    -- Check if the room is already allocated to another patient
    SELECT COUNT(*) INTO room_count FROM ROOM WHERE ROOM_NO = NEW.ROOM_NO;
    IF room_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: The room is already allocated to another patient.';
    END IF;

    -- Check if the patient is already allocated a room
    SELECT COUNT(*) INTO patient_count FROM ROOM WHERE PATIENT_ID = NEW.PATIENT_ID;
    IF patient_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: The patient is already allocated a room.';
    END IF;
END;
    """)

    # Trigger to check room allocation before update
c.execute("""
    CREATE TRIGGER check_room_allocation_before_update
BEFORE UPDATE ON ROOM
FOR EACH ROW
BEGIN
    DECLARE room_count INT;

    -- Only check if ROOM_NO is being updated
    IF NEW.ROOM_NO != OLD.ROOM_NO THEN
        -- Check if the new room number is already allocated to another patient
        SELECT COUNT(*) INTO room_count FROM ROOM WHERE ROOM_NO = NEW.ROOM_NO AND PATIENT_ID != NEW.PATIENT_ID;
        IF room_count > 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: The room is already allocated to another patient.';
        END IF;
    END IF;
END
    """)
 
# Create triggers for validation
c.execute("""
    CREATE TRIGGER check_patient_email
    BEFORE INSERT ON PATIENT
    FOR EACH ROW
    BEGIN
        IF NEW.EMAIL NOT LIKE '%_@__%.__%' THEN
            SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'Invalid email format for patient';
        END IF;
    END
""")

c.execute("""
    CREATE TRIGGER validate_employee_email
    BEFORE INSERT ON EMPLOYEE
    FOR EACH ROW
    BEGIN
        IF NEW.EMAIL NOT LIKE '%_@__%.__%' THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Invalid email format for employee';
        END IF;
    END
""")

c.execute("""
    CREATE TRIGGER prevent_delete_admin
    BEFORE DELETE ON EMPLOYEE
    FOR EACH ROW
    BEGIN
        IF OLD.EMP_ID = 1 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete the admin employee.';
        END IF;
    END;
""")

c.execute("""
    CREATE TRIGGER validate_employee_age
    BEFORE INSERT ON EMPLOYEE
    FOR EACH ROW
    BEGIN
        IF NEW.AGE < 18 OR NEW.AGE > 65 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Employee age must be between 18 and 65.';
        END IF;
    END;
""")

c.execute("""
     CREATE TRIGGER validate_patient_phone
        BEFORE INSERT ON CONTACT_NO
        FOR EACH ROW
        BEGIN
            IF CHAR_LENGTH(NEW.CONTACTNO) != 10 OR (CHAR_LENGTH(NEW.ALT_CONTACT)!=10 AND NEW.ALT_CONTACT !=0)THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Phone number must be 10 digits';
            END IF;
        END;
""")


# Create procedures
c.execute("""
    CREATE PROCEDURE SearchPatients(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        SELECT * FROM patient WHERE patient_id LIKE CONCAT('%', search_term, '%');
    ELSEIF search_by = 'Patient Name' THEN
        SELECT * FROM patient WHERE name LIKE CONCAT('%', search_term, '%');
    END IF;
END;
""")
print("PROCEDURE CREATED SUCCESSFULLY")

c.execute("""
    CREATE PROCEDURE SearchDoctors(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
        IF search_by = 'Doctor_ID' THEN
        SELECT * FROM Doctor WHERE Doctor_ID = search_term;
    ELSEIF search_by = 'Doctor_Name' THEN
        SELECT * FROM Doctor WHERE Name LIKE CONCAT('%', search_term, '%');
    ELSE
        SELECT 'Invalid search criteria: ' , search_by;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid search criteria';
    END IF;
END;
""")
print("PROCEDURE CREATED SUCCESSFULLY")

c.execute("""
    CREATE PROCEDURE SearchBills(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        SELECT b.patient_id, b.bill
        FROM bill b
        JOIN patient p ON b.patient_id = p.patient_id
        WHERE p.patient_id LIKE CONCAT('%', search_term, '%');
    ELSEIF search_by = 'Patient Name' THEN
        SELECT b.patient_id, b.bill
        FROM bill b
        JOIN patient p ON b.patient_id = p.patient_id
        WHERE p.name LIKE CONCAT('%', search_term, '%');
    END IF;
END
""")
print("PROCEDURE CREATED SUCCESSFULLY")

c.execute("""
    CREATE PROCEDURE SearchMedicines(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        SELECT m.m_no, m.patient_id, m.medicine_name, m.m_cost, m.m_qty, m.m_date
        FROM medicine m
        JOIN patient p ON m.patient_id = p.patient_id
        WHERE p.patient_id LIKE CONCAT('%', search_term, '%');
    ELSEIF search_by = 'Patient Name' THEN
        SELECT m.m_no, m.patient_id, m.medicine_name, m.m_cost, m.m_qty, m.m_date
        FROM medicine m
        JOIN patient p ON m.patient_id = p.patient_id
        WHERE p.name LIKE CONCAT('%', search_term, '%');
    END IF;
END 
""")
print("PROCEDURE CREATED SUCCESSFULLY")

c.execute("""
    CREATE PROCEDURE SearchTreatments(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        SELECT t.t_no, t.patient_id, t.doc_id, t.treatment, t.treatment_code, t.t_cost, t.t_date
        FROM treatment t
        JOIN patient p ON t.patient_id = p.patient_id
        WHERE p.patient_id LIKE CONCAT('%', search_term, '%');
    ELSEIF search_by = 'Patient Name' THEN
        SELECT t.t_no, t.patient_id, t.doc_id, t.treatment, t.treatment_code, t.t_cost, t.t_date
        FROM treatment t
        JOIN patient p ON t.patient_id = p.patient_id
        WHERE p.name LIKE CONCAT('%', search_term, '%');
    ELSEIF search_by = 'Doctor ID' THEN
        SELECT t.t_no, t.patient_id, t.doc_id, t.treatment, t.treatment_code, t.t_cost, t.t_date
        FROM treatment t
        JOIN employee e ON t.doc_id = e.emp_id
        WHERE e.emp_id LIKE CONCAT('%', search_term, '%');
    END IF;
END
""")
print("PROCEDURE CREATED SUCCESSFULLY")


# Commit changes and close the connection
conn.commit()
conn.close()
print("DATABASE SETUP COMPLETED SUCCESSFULLY")
