CREATE DATABASE IF NOT EXISTS ADBMS;
USE ADBMS;


-- Table for patients
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_ssn VARCHAR(20) NOT NULL,
    doctor_id INT NOT NULL,
    name VARCHAR(100),
    gender VARCHAR(10),
    address VARCHAR(255),
    contact VARCHAR(15),
    email VARCHAR(100),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);
ALTER TABLE Patients ADD COLUMN Blood_Group VARCHAR(4);
ALTER TABLE Patients ADD COLUMN DOB VARCHAR(10);
-- Table for doctors
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_ssn VARCHAR(20) NOT NULL,
    name VARCHAR(100),
    phone VARCHAR(15)
);

-- Table for bills
CREATE TABLE IF NOT EXISTS Bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    bill DECIMAL(10, 2),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Table for medicines
CREATE TABLE IF NOT EXISTS Medicines (
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    medicine_name VARCHAR(100),
    cost DECIMAL(10, 2),
    quantity INT,
    date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Table for treatments
CREATE TABLE IF NOT EXISTS Treatments (
    treatment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    treatment VARCHAR(255),
    treatment_code VARCHAR(50),
    treatment_cost DECIMAL(10, 2),
    treatment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

----- CREATING PAYCHECK TABLE -----
CREATE TABLE Paycheck(
    Cheque_Number INT NOT NULL,
    Doctor_ID INT NOT NULL,
    Salary FLOAT NOT NULL,
    Bonus FLOAT NOT NULL,
    Pay_Date DATE NOT NULL,
    PRIMARY KEY(Cheque_Number),
    FOREIGN KEY(Doctor_ID) REFERENCES Doctors(Doctor_ID),
    CHECK (Salary >= 0 AND Bonus >= 0)
);

----- CREATING DIAGNOSIS TABLE -----
CREATE TABLE Diagnosis(
    Diagnosis_ID INT NOT NULL AUTO_INCREMENT,
    Diagnosis_Category VARCHAR(50) NOT NULL,
    Base_Price FLOAT NOT NULL CHECK (Base_Price >= 0),
    PRIMARY KEY(Diagnosis_ID)
);

----- CREATING CPT TABLE -----
CREATE TABLE CPT(
    CPT_ID INT NOT NULL AUTO_INCREMENT,
    CPT_Category VARCHAR(50),
    CPT_Price FLOAT NOT NULL CHECK (CPT_Price >= 0),
    PRIMARY KEY(CPT_ID)
);

CREATE TABLE Prescription(
    Prescription_ID INT NOT NULL AUTO_INCREMENT,
    Patient_ID INT NOT NULL,
    Prescription_Date DATE NOT NULL,
    PRIMARY KEY(Prescription_ID),
    FOREIGN KEY(Patient_ID) REFERENCES Patients(Patient_ID)
);

----- CREATING INVOICE TABLE -----
CREATE TABLE Invoice(
    Invoice_Number INT NOT NULL AUTO_INCREMENT,
    Patient_ID INT NOT NULL,
    CPT_ID INT NOT NULL,
    Diagnosis_ID INT NOT NULL,
    Amount FLOAT NOT NULL CHECK (Amount >= 0),
    Invoice_Date DATE NOT NULL,
    Prescription_ID INT NOT NULL,
    PRIMARY KEY(Invoice_Number),
    FOREIGN KEY(Patient_ID) REFERENCES Patients(Patient_ID),
    FOREIGN KEY(CPT_ID) REFERENCES CPT(CPT_ID),
    FOREIGN KEY(Diagnosis_ID) REFERENCES Diagnosis(Diagnosis_ID),
    FOREIGN KEY(Prescription_ID) REFERENCES Prescription(Prescription_ID)
);

CREATE TABLE Payment(
    Transaction_Number BIGINT NOT NULL AUTO_INCREMENT,
    Invoice_Number INT NOT NULL,
    Payment_Status VARCHAR(15) CHECK (Payment_Status IN ('FAILED', 'PENDING', 'SUCCESS')),
    Payment_Method VARCHAR(15) CHECK (Payment_Method IN ('Online Banking', 'Card', 'Cash')),
    Payment_Date DATE NOT NULL,
    PRIMARY KEY(Transaction_Number),
    FOREIGN KEY(Invoice_Number) REFERENCES Invoice(Invoice_Number)
);

CREATE TABLE Insurance(
    Company_ID INT NOT NULL AUTO_INCREMENT,
    Company_Name VARCHAR(50) NOT NULL,
    Phone_Number VARCHAR(10),
    PRIMARY KEY(Company_ID),
    CHECK (CHAR_LENGTH(Phone_Number) = 10)
);



-- Stored procedure for searching patients
DELIMITER $$

CREATE PROCEDURE SearchPatients(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        SELECT * FROM Patients WHERE patient_id = search_term;
    ELSEIF search_by = 'Patient Name' THEN
        SELECT * FROM Patients WHERE name LIKE CONCAT('%', search_term, '%');
    END IF;
END $$

DELIMITER ;

-- Stored procedure for searching doctors
DELIMITER $$

CREATE PROCEDURE SearchDoctors(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Doctor ID' THEN
        SELECT * FROM Doctors WHERE doctor_id = search_term;
    ELSEIF search_by = 'Doctor Name' THEN
        SELECT * FROM Doctors WHERE name LIKE CONCAT('%', search_term, '%');
    END IF;
END $$

DELIMITER ;

-- Stored procedure for searching bills
DELIMITER $$

CREATE PROCEDURE SearchBills(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        -- Convert search_term to an integer if looking up by patient_id
        SELECT * FROM Bills WHERE patient_id = CAST(search_term AS UNSIGNED);
        
    ELSEIF search_by = 'Patient Name' THEN
        -- Perform a join to search by Patient Name
        SELECT Bills.* 
        FROM Bills 
        INNER JOIN Patients ON Bills.patient_id = Patients.patient_id
        WHERE Patients.name LIKE CONCAT('%', search_term, '%');
    END IF;
END $$

DELIMITER ;


-- Stored procedure for searching medicines
DELIMITER $$

CREATE PROCEDURE SearchMedicines(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        SELECT * FROM Medicines WHERE patient_id = search_term;
    ELSEIF search_by = 'Medicine Name' THEN
        SELECT * FROM Medicines WHERE medicine_name LIKE CONCAT('%', search_term, '%');
    END IF;
END $$

DELIMITER ;

-- Stored procedure for searching treatments
DELIMITER $$

CREATE PROCEDURE SearchTreatments(IN search_by VARCHAR(50), IN search_term VARCHAR(100))
BEGIN
    IF search_by = 'Patient ID' THEN
        SELECT * FROM Treatments WHERE patient_id = search_term;
    ELSEIF search_by = 'Patient Name' THEN
        SELECT Treatments.* 
        FROM Treatments
        INNER JOIN Patients ON Treatments.patient_id = Patients.patient_id
        WHERE Patients.name LIKE CONCAT('%', search_term, '%');
    ELSEIF search_by = 'Doctor ID' THEN
        SELECT * FROM Treatments WHERE doctor_id = search_term;
    END IF;
END $$

DELIMITER ;
