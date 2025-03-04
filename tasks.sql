Use ADBMS;
-- task1 Optimize real-time query performance for patient records and medical histories.
-- Adding indexing to patient table--
CREATE INDEX IDX_Patient_SSN ON Patients(Patient_SSN);
CREATE INDEX IDX_Patient_Name ON Patients(Name);

show index from patients;

CREATE INDEX IDX_Patient_SSN ON Patients(Patient_SSN);
CREATE INDEX IDX_Patient_DoctorID ON Patients(Doctor_ID);

-- adding indexing to invoice table--
CREATE INDEX IDX_Invoice_PatientID ON Invoice(Patient_ID);
CREATE INDEX IDX_Invoice_DiagnosisID ON Invoice(Diagnosis_ID);
CREATE INDEX IDX_Invoice_Date ON Invoice(Invoice_Date);
CREATE INDEX IDX_Invoice_CPTID ON Invoice(CPT_ID);

SHOW INDEX FROM Invoice;

-- Index Doctor_ID for queries related to doctor paychecks. --
CREATE INDEX IDX_Paycheck_DoctorID ON Paycheck(Doctor_ID);

ALTER TABLE Invoice
PARTITION BY RANGE (YEAR(Invoice_Date)) (
    PARTITION p0 VALUES LESS THAN (2024),
    PARTITION p1 VALUES LESS THAN (2025),
    PARTITION p2 VALUES LESS THAN (2026),
    PARTITION p3 VALUES LESS THAN (MAXVALUE)
);




EXPLAIN SELECT * FROM Patients WHERE Name = 'John Doe';

-- Query to Retrieve Patient Information and Medical Histories: --
SELECT p.Patient_ID, p.Name, d.Diagnosis_Category, c.CPT_Category
FROM Patients p
JOIN Invoice i ON p.Patient_ID = i.Patient_ID
JOIN Diagnosis d ON i.Diagnosis_ID = d.Diagnosis_ID
JOIN CPT c ON i.CPT_ID = c.CPT_ID
WHERE p.Patient_SSN = '987-65-4321';

EXPLAIN SELECT p.Patient_ID, p.Name, d.Diagnosis_Category
FROM Patients p
JOIN Invoice i ON p.Patient_ID = i.Patient_ID
JOIN Diagnosis d ON i.Diagnosis_ID = d.Diagnosis_ID
WHERE p.Patient_SSN = '123-45-6789';


SHOW PROCESSLIST;
SHOW STATUS LIKE 'Handler%';

OPTIMIZE TABLE Patients;
OPTIMIZE TABLE Invoice;



-- task 2 Implement stringent access controls and encryption to protect patient confidentiality.

CREATE ROLE IF NOT EXISTS Doctor_Role;
CREATE ROLE IF NOT EXISTS Admin_Role;
CREATE ROLE IF NOT EXISTS Billing_Role;

-- Grant appropriate privileges to roles

-- Doctors can only read patient data, not modify it
GRANT SELECT ON Adbms.Patients TO Doctor_Role;

-- Admins can read, write, and manage all data
GRANT ALL PRIVILEGES ON Adbms.* TO Admin_Role;

-- Billing role can manage invoices and payments, but not patient data
GRANT SELECT, INSERT, UPDATE ON Adbms.Invoice TO Billing_Role;
GRANT SELECT, INSERT, UPDATE ON Adbms.Payment TO Billing_Role;

DROP USER 'admin_user'@'localhost';
CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'adminpassword456';

-- Create specific users and assign them roles
CREATE USER 'doctors_user'@'localhost' IDENTIFIED BY 'password123';
GRANT Doctor_Role TO 'doctors_user'@'localhost';

CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'adminpassword456';
GRANT Admin_Role TO 'admin_user'@'localhost';

CREATE USER 'billing_user'@'localhost' IDENTIFIED BY 'billingpassword789';
GRANT Billing_Role TO 'billing_user'@'localhost';

-- Ensure that users can't escalate their privileges
SET DEFAULT ROLE Doctor_Role TO 'doctors_user'@'localhost';
SET DEFAULT ROLE Admin_Role TO 'admin_user'@'localhost';
SET DEFAULT ROLE Billing_Role TO 'billing_user'@'localhost';


ALTER SYSTEM SET ssl = 'on';


-- task 3  Integrate advanced database models (mobile, distributed, and spatial) for efficient data retrieval and management.
 ---
-- Create a table to track changes for synchronization
CREATE TABLE Sync_Log (
    Sync_ID INT NOT NULL AUTO_INCREMENT,
    Table_Name VARCHAR(50),
    Record_ID INT,
    Sync_Status ENUM('Pending', 'Synced') DEFAULT 'Pending',
    Sync_Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Sync_ID)
);

-- Example sync entry after inserting a new patient (this entry would be used by the sync service)
INSERT INTO Sync_Log (Table_Name, Record_ID, Sync_Status) 
VALUES ('Patient', 101, 'Pending');

-- Update sync status after successful sync
UPDATE Sync_Log SET Sync_Status = 'Completed' WHERE Sync_ID = 1;

-- Use a synchronization service or API to update mobile databases with central changes and vice versa.
-- Data on mobile devices can be stored using SQLite for offline capabilities.

-- Use replication to copy data between servers
CHANGE MASTER TO MASTER_HOST='master_db_host', MASTER_USER='replication_user', MASTER_PASSWORD='password', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=107;

-- Start replication
START SLAVE;

-- Sharding (partitioning data for distributed storage)
CREATE TABLE Patient_Partitioned (
    Patient_ID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(30),
    Gender VARCHAR(10),
    Doctor_ID INT NOT NULL,
    PRIMARY KEY(Patient_ID)
) PARTITION BY RANGE (Patient_ID) (
    PARTITION p0 VALUES LESS THAN (1000),
    PARTITION p1 VALUES LESS THAN (2000),
    PARTITION p2 VALUES LESS THAN (3000),
    PARTITION p3 VALUES LESS THAN MAXVALUE
);

-- Adding spatial features to the Insurance Company table to track locations
ALTER TABLE Insurance ADD COLUMN Company_Location POINT;

-- Creating a spatial index to optimize geospatial queries
CREATE SPATIAL INDEX idx_location ON Insurance(Company_Location);

-- Insert data with geographical coordinates (latitude, longitude)
INSERT INTO Insurance (Company_Name, Phone_Number, Company_Location)
VALUES ('ABC Insurance', 1234567890, ST_GeomFromText('POINT(40.7128 -74.0060)'));

-- Query to find insurance companies within a certain distance
SELECT Company_Name, ST_Distance(Company_Location, ST_GeomFromText('POINT(40.730610 -73.935242)')) AS distance
FROM Insurance
WHERE ST_DWithin(Company_Location, ST_GeomFromText('POINT(40.730610 -73.935242)'), 10000);  -- 10 km radius

-- task 4 Design indexing strategies for quick access to medical records and treatment histories.
-- Displaying indexes for optimization checks
SHOW INDEX FROM Patients;
SHOW INDEX FROM Invoice;
SHOW PROCESSLIST;
SHOW STATUS LIKE 'Handler%';
