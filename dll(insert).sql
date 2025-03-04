USE ADBMS;

INSERT INTO Doctors (Doctor_ID, Doctor_SSN, Name, Phone)
VALUES 
(101, '1266071613', 'Francis', 7407535102),
(102, '8083069438', 'Vishal', 5775593029),
(103, '9017595693', 'Hua', 1694362521),
(104, '9190841246', 'John', 7630399848),
(105, '5083126610', 'Kate', 2420072433),
(106, '7881793415', 'Donald', 7478736086),
(107, '9364885804', 'Mathew', 3851072550),
(108, '4931814876', 'Joe', 2291855091),
(109, '6660443937', 'Elizabeth', 8795129630),
(110, '9877557927', 'Arya', 1443429264);

select *  from Doctors;

-- Inserting Patient Records
INSERT INTO Patients (Patient_SSN, Doctor_ID, Name, Gender, DOB, Address, Contact, Email, BLOOD_GROUP)
VALUES 
('123-45-6789', 101, 'Aadi', 'Male', '2003-01-01', 'Mumbai', '123-456-7890', 'aadi@example.com', 'B+'),
('987-65-4321', 102, 'Grace', 'Female', '2003-02-02', 'Mumbai', '987-654-3210', 'grace@example.com', 'AB+'),
('456-78-9012', 103, 'Jaya Sahani', 'Female', '2003-03-03', 'Mumbai', '222-333-4444', 'jaya@example.com', 'B+'),
('345-67-8901', 104, 'Chelton Deva', 'Male', '2003-04-04', 'Santacruz', '555-666-7777', 'chelton@example.com', 'AB+'),
('234-56-7890', 105, 'Ronan Fernandes', 'Male', '2003-05-05', 'Andheri', '888-999-0000', 'ronan@example.com', 'B+'),
('567-89-0123', 106, 'Mugdha Zope', 'Female', '2003-06-06', 'Mumbai', '111-222-3333', 'mugdha@example.com', 'O+'),
('678-90-1234', 107, 'Vineet Chaturvedi', 'Male', '2003-07-07', 'Kurla', '444-555-6666', 'vineet@example.com', 'B+'),
('789-01-2345', 108, 'Jahnvi Gupta', 'Female', '2003-08-08', 'Mumbai', '777-888-9999', 'jahnvi@example.com', 'A+'),
('890-12-3456', 109, 'Aryan Mohitee', 'Male', '2003-09-09', 'Borivali', '000-111-2222', 'aryan@example.com', 'B+'),
('901-23-4567', 110, 'Khevnaa Marfartia', 'Female', '1993-10-10', '654 Fir St', '333-444-5555', 'khevnaa@example.com', 'B+'),
('012-34-5678', 101, 'Dhruv Shetty', 'Male', '1995-11-11', '123 Pine St', '666-777-8888', 'dhruv@example.com', 'B+'),
('123-45-6780', 102, 'Jenny', 'Female', '1996-12-12', '789 Oak St', '999-000-1111', 'jenny@example.com', 'B+'),
('234-56-7891', 103, 'Harshil Sansi', 'Male', '1997-01-01', '321 Maple St', '222-333-4444', 'harshil@example.com', 'A+'),
('345-67-8902', 104, 'Laura Young', 'Female', '1998-02-02', '456 Birch St', '555-666-7777', 'laura@example.com', 'B+'),
('456-78-9013', 105, 'Vaibhav Tripathi', 'Male', '1999-03-03', '789 Cedar St', '888-999-0000', 'vaibhav@example.com', 'B+'),
('567-89-0124', 106, 'Nina Walker', 'Female', '2000-04-04', '321 Redwood St', '111-222-3333', 'nina@example.com', 'O+'),
('678-90-1235', 107, 'Shubh Shetty', 'Male', '2001-05-05', '654 Fir St', '444-555-6666', 'shubh@example.com', 'B+'),
('789-01-2346', 108, 'Paula Allen', 'Female', '2002-06-06', '123 Pine St', '777-888-9999', 'paula@example.com', 'A+'),
('890-12-3457', 109, 'Ishan Hedge', 'Male', '2003-07-07', '789 Oak St', '000-111-2222', 'ishan@example.com', 'B+'),
('901-23-4568', 110, 'Rachel Adams', 'Female', '2004-08-08', '321 Maple St', '333-444-5555', 'rachel@example.com', 'A+'),
('123-45-6782', 111, 'Aditya Sharma', 'Male', '2000-05-10', 'Thane, India', '101-202-3030', 'aditya@example.com', 'O-'),
('234-56-7892', 112, 'Simran Kapoor', 'Female', '1995-07-20', 'Dadar, India', '202-303-4040', 'simran@example.com', 'A+'),
('345-67-8903', 113, 'Rajesh Kumar', 'Male', '2001-09-15', 'Vile Parle, India', '303-404-5050', 'rajesh@example.com', 'B-'),
('456-78-9014', 114, 'Neha Patel', 'Female', '2002-02-10', 'Juhu, India', '404-505-6060', 'neha@example.com', 'AB-'),
('567-89-0125', 115, 'Vikram Yadav', 'Male', '1997-08-25', 'Andheri West, India', '505-606-7070', 'vikram@example.com', 'O+'),
('678-90-1236', 116, 'Pooja Mehta', 'Female', '2000-11-30', 'Goregaon, India', '606-707-8080', 'pooja@example.com', 'A-'),
('789-01-2347', 117, 'Mohit Soni', 'Male', '1999-06-17', 'Bandra, India', '707-808-9090', 'mohit@example.com', 'B+'),
('890-12-3458', 118, 'Rita Bhattacharya', 'Female', '2003-12-12', 'Kurla East, India', '808-909-0101', 'rita@example.com', 'AB+'),
('901-23-4569', 119, 'Ravi Reddy', 'Male', '1998-04-22', 'Malad, India', '909-010-1212', 'ravi@example.com', 'O+'),
('012-34-5679', 120, 'Priya Thakur', 'Female', '2001-03-18', 'Parel, India', '010-121-2323', 'priya@example.com', 'B+'),
('123-45-6783', 121, 'Ankur Gupta', 'Male', '2000-02-28', 'Versova, India', '101-111-1212', 'ankur@example.com', 'A+'),
('234-56-7893', 122, 'Sushmita Sen', 'Female', '2002-03-22', 'Kandivali, India', '111-121-1313', 'sushmita@example.com', 'AB+'),
('345-67-8904', 123, 'Sandeep Singh', 'Male', '2001-04-14', 'Borivali, India', '121-131-1414', 'sandeep@example.com', 'B+'),
('456-78-9015', 124, 'Nikita Mehta', 'Female', '2000-07-18', 'Mulund, India', '131-141-1515', 'nikita@example.com', 'O+'),
('567-89-0126', 125, 'Tarun Sharma', 'Male', '1999-06-30', 'Vasai, India', '141-151-1616', 'tarun@example.com', 'B-'),
('678-90-1237', 126, 'Aditi Verma', 'Female', '2003-01-02', 'Vile Parle East, India', '151-161-1717', 'aditi@example.com', 'AB+'),
('789-01-2348', 127, 'Nikhil Rao', 'Male', '1998-08-03', 'Ghatkopar, India', '161-171-1818', 'nikhil@example.com', 'A-'),
('890-12-3459', 128, 'Tanya Shah', 'Female', '2002-10-11', 'Andheri East, India', '171-181-1919', 'tanya@example.com', 'B+'),
('901-23-4570', 129, 'Abhinav Joshi', 'Male', '2001-12-05', 'Malad East, India', '181-191-2020', 'abhinav@example.com', 'O+'),
('012-34-5680', 130, 'Swati Desai', 'Female', '2000-03-14', 'Kandivali East, India', '191-202-2121', 'swati@example.com', 'A+'),
('123-45-6784', 131, 'Vineeta Rani', 'Female', '1999-05-25', 'Borivali East, India', '202-212-2222', 'vineeta@example.com', 'B-'),
('234-56-7894', 132, 'Manish Yadav', 'Male', '2001-07-09', 'Dombivli, India', '212-222-2323', 'manish@example.com', 'AB-'),
('345-67-8905', 133, 'Simran Yadav', 'Female', '2000-09-17', 'Andheri West, India', '222-232-2424', 'simran.yadav@example.com', 'O-'),
('456-78-9016', 134, 'Aditya Malhotra', 'Male', '2002-05-14', 'Bandra West, India', '232-242-2525', 'aditya.malhotra@example.com', 'A+'),
('567-89-0127', 135, 'Shruti Bansal', 'Female', '2001-11-22', 'Kandivali West, India', '242-252-2626', 'shruti.bansal@example.com', 'B+'),
('678-90-1238', 136, 'Vikas Agarwal', 'Male', '2002-01-10', 'Jogeshwari East, India', '252-262-2727', 'vikas.agarwal@example.com', 'O-'),
('789-01-2349', 137, 'Rekha Sharma', 'Female', '1998-04-28', 'Goregaon East, India', '262-272-2828', 'rekha.sharma@example.com', 'A-'),
('890-12-3460', 138, 'Rahul Singh', 'Male', '2000-06-15', 'Mira Road, India', '272-282-2929', 'rahul.singh@example.com', 'B+'),
('901-23-4571', 139, 'Geeta Mehra', 'Female', '2003-08-10', 'Vashi, India', '282-292-3030', 'geeta.mehra@example.com', 'AB+'),
('012-34-5681', 140, 'Ashish Kumar', 'Male', '2001-10-30', 'Thane West, India', '292-303-3131', 'ashish.kumar@example.com', 'B+'),
('123-45-6785', 141, 'Aishwarya Deshmukh', 'Female', '2002-03-12', 'Panvel, India', '303-313-3232', 'aishwarya.deshmukh@example.com', 'A+'),
('234-56-7895', 142, 'Manoj Verma', 'Male', '1999-12-24', 'Navi Mumbai, India', '313-323-3333', 'manoj.verma@example.com', 'B-'),
('345-67-8906', 143, 'Sonali Joshi', 'Female', '2000-08-29', 'Dahisar, India', '323-333-3434', 'sonali.joshi@example.com', 'AB+'),
('456-78-9017', 144, 'Pradeep Kumar', 'Male', '2002-01-03', 'Chembur, India', '333-343-3535', 'pradeep.kumar@example.com', 'O+'),
('567-89-0128', 145, 'Priyanka Kapoor', 'Female', '2001-04-21', 'Kalyan, India', '343-353-3636', 'priyanka.kapoor@example.com', 'A+'),
('678-90-1239', 146, 'Raghav Pandey', 'Male', '2000-05-18', 'Bhayander, India', '353-363-3737', 'raghav.pandey@example.com', 'O-'),
('789-01-2350', 147, 'Komal Rani', 'Female', '1999-11-04', 'Dadar West, India', '363-373-3838', 'komal.rani@example.com', 'B+'),
('890-12-3461', 148, 'Tarun Bansal', 'Male', '2001-06-19', 'Bhiwandi, India', '373-383-3939', 'tarun.bansal@example.com', 'AB+'),
('901-23-4572', 149, 'Nishant Singh', 'Male', '1998-02-13', 'Vile Parle, India', '383-393-4040', 'nishant.singh@example.com', 'A+'),
('012-34-5682', 150, 'Sanjana Yadav', 'Female', '2003-09-21', 'Versova West, India', '393-404-4141', 'sanjana.yadav@example.com', 'B+'),
('123-45-6786', 151, 'Ritesh Kumar', 'Male', '2000-03-06', 'Bandra East, India', '404-414-4242', 'ritesh.kumar@example.com', 'O+'),
('234-56-7896', 152, 'Priya Bhardwaj', 'Female', '2001-07-22', 'Juhu, India', '414-424-4343', 'priya.bhardwaj@example.com', 'A+'),
('345-67-8907', 153, 'Shubham Verma', 'Male', '2002-01-17', 'Vasai East, India', '424-434-4444', 'shubham.verma@example.com', 'B+'),
('456-78-9018', 154, 'Anjali Mishra', 'Female', '2000-11-25', 'Malad West, India', '434-444-4545', 'anjali.mishra@example.com', 'AB+'),
('567-89-0129', 155, 'Ravi Kapoor', 'Male', '1999-02-14', 'Goregaon West, India', '444-454-4646', 'ravi.kapoor@example.com', 'O+'),
('678-90-1240', 156, 'Swati Agarwal', 'Female', '2002-06-03', 'Thane East, India', '454-464-4747', 'swati.agarwal@example.com', 'A-'),
('789-01-2351', 157, 'Rajeev Jain', 'Male', '2001-12-20', 'Vikhroli, India', '464-474-4848', 'rajeeve.jain@example.com', 'B-'),
('890-12-3462', 158, 'Shilpa Kapoor', 'Female', '2003-05-12', 'Kandivali East, India', '474-484-4949', 'shilpa.kapoor@example.com', 'O-'),
('901-23-4573', 159, 'Ashish Desai', 'Male', '2001-08-01', 'Mira Road East, India', '484-494-5050', 'ashish.desai@example.com', 'AB+'),
('012-34-5683', 160, 'Nandita Mehra', 'Female', '1999-10-25', 'Borivali West, India', '494-505-5151', 'nandita.mehra@example.com', 'B+'),
('123-45-6787', 161, 'Alok Singh', 'Male', '2002-07-02', 'Ghatkopar West, India', '505-515-5252', 'alok.singh@example.com', 'A+'),
('234-56-7897', 162, 'Ananya Rao', 'Female', '2001-11-30', 'Andheri East, India', '515-525-5353', 'ananya.rao@example.com', 'AB+'),
('345-67-8908', 163, 'Vivek Sharma', 'Male', '2000-09-10', 'Mulund West, India', '525-535-5454', 'vivek.sharma@example.com', 'O+'),
('456-78-9019', 164, 'Divya Thakur', 'Female', '1999-06-16', 'Thane West, India', '535-545-5555', 'divya.thakur@example.com', 'B-'),
('567-89-0130', 165, 'Prakash Tiwari', 'Male', '2000-02-25', 'Mira Road West, India', '545-555-5656', 'prakash.tiwari@example.com', 'A-'),
('678-90-1241', 166, 'Kavita Joshi', 'Female', '2002-10-07', 'Bhandup West, India', '555-565-5757', 'kavita.joshi@example.com', 'AB+'),
('789-01-2352', 167, 'Sandeep Chawla', 'Male', '2001-01-14', 'Vasai West, India', '565-575-5858', 'sandeep.chawla@example.com', 'O+'),
('890-12-3463', 168, 'Madhuri Bhatia', 'Female', '1998-12-04', 'Kandivali West, India', '575-585-5959', 'madhuri.bhatia@example.com', 'A+'),
('901-23-4574', 169, 'Abhinav Malhotra', 'Male', '2000-11-17', 'Vikhroli West, India', '585-595-6060', 'abhinav.malhotra@example.com', 'B+'),
('012-34-5684', 170, 'Ritika Kapoor', 'Female', '2001-04-02', 'Jogeshwari West, India', '595-606-6161', 'ritika.kapoor@example.com', 'O+'),
('123-45-6788', 171, 'Rohit Yadav', 'Male', '2003-09-21', 'Navi Mumbai West, India', '606-616-6262', 'rohit.yadav@example.com', 'B+'),
('234-56-7898', 172, 'Shalini Iyer', 'Female', '1999-07-15', 'Andheri West, India', '616-626-6363', 'shalini.iyer@example.com', 'A+'),
('345-67-8909', 173, 'Ashutosh Sharma', 'Male', '2002-05-06', 'Borivali East, India', '626-636-6464', 'ashutosh.sharma@example.com', 'O+'),
('456-78-9020', 174, 'Tanvi Pandey', 'Female', '2001-03-18', 'Kandivali West, India', '636-646-6565', 'tanvi.pandey@example.com', 'AB+'),
('567-89-0131', 175, 'Nitin Bhardwaj', 'Male', '2000-01-29', 'Malad East, India', '646-656-6666', 'nitin.bhardwaj@example.com', 'B-'),
('678-90-1242', 176, 'Sonia Shah', 'Female', '2002-07-13', 'Goregaon East, India', '656-666-6767', 'sonia.shah@example.com', 'A+'),
('789-01-2353', 177, 'Himanshu Kapoor', 'Male', '1999-05-01', 'Thane East, India', '666-676-6868', 'himanshu.kapoor@example.com', 'O-'),
('890-12-3464', 178, 'Meenal Agarwal', 'Female', '2000-08-19', 'Malad West, India', '676-686-6969', 'meenal.agarwal@example.com', 'AB+'),
('901-23-4575', 179, 'Vikas Gupta', 'Male', '2001-04-25', 'Vasai East, India', '686-696-7070', 'vikas.gupta@example.com', 'B+'),
('012-34-5685', 180, 'Manisha Rathi', 'Female', '2002-03-16', 'Dadar East, India', '696-707-7171', 'manisha.rathi@example.com', 'A+'),
('123-45-6789', 181, 'Pranjal Pandey', 'Male', '2000-11-12', 'Bhayander West, India', '707-717-7272', 'pranjal.pandey@example.com', 'AB+'),
('234-56-7899', 182, 'Neha Rani', 'Female', '2001-09-03', 'Goregaon West, India', '717-727-7373', 'neha.rani@example.com', 'O+'),
('345-67-8910', 183, 'Naveen Yadav', 'Male', '1999-06-28', 'Vasai West, India', '727-737-7474', 'naveen.yadav@example.com', 'B+'),
('456-78-9021', 184, 'Sakshi Kapoor', 'Female', '2000-02-06', 'Malad East, India', '737-747-7575', 'sakshi.kapoor@example.com', 'A+'),
('567-89-0132', 185, 'Saurabh Deshmukh', 'Male', '2002-10-17', 'Ghatkopar West, India', '747-757-7676', 'saurabh.deshmukh@example.com', 'O+'),
('678-90-1243', 186, 'Neelam Verma', 'Female', '2001-12-07', 'Kandivali West, India', '757-767-7777', 'neelam.verma@example.com', 'AB+'),
('789-01-2354', 187, 'Tanuj Pandey', 'Male', '2000-04-19', 'Andheri East, India', '767-777-7878', 'tanuj.pandey@example.com', 'B+'),
('890-12-3465', 188, 'Shivani Joshi', 'Female', '2001-05-11', 'Bhandup East, India', '777-787-7979', 'shivani.joshi@example.com', 'A-'),
('901-23-4576', 189, 'Sandeep Raj', 'Male', '2000-08-09', 'Navi Mumbai East, India', '787-797-8080', 'sandeep.raj@example.com', 'O-'),
('012-34-5686', 190, 'Simran Mehta', 'Female', '2001-10-21', 'Vikhroli East, India', '797-808-8181', 'simran.mehta@example.com', 'AB+');



UPDATE Patients
SET Patient_ID = '201'
WHERE Patient_SSN = '123-45-6789';

UPDATE Patients
SET Patient_ID = '202'
WHERE Patient_SSN = '987-65-4321';

UPDATE Patients
SET Patient_ID = '203'
WHERE Patient_SSN = '456-78-9012';

UPDATE Patients
SET Patient_ID = '204'
WHERE Patient_SSN = '345-67-8901';

UPDATE Patients
SET Patient_ID = '205'
WHERE Patient_SSN = '234-56-7890';

UPDATE Patients
SET Patient_ID = '206'
WHERE Patient_SSN = '567-89-0123';

UPDATE Patients
SET Patient_ID = '207'
WHERE Patient_SSN = '678-90-1234';

UPDATE Patients
SET Patient_ID = '208'
WHERE Patient_SSN = '789-01-2345';

UPDATE Patients
SET Patient_ID = '209'
WHERE Patient_SSN = '890-12-3456';

UPDATE Patients
SET Patient_ID = '210'
WHERE Patient_SSN = '901-23-4567';

UPDATE Patients
SET Patient_ID = '211'
WHERE Patient_SSN = '012-34-5678';

UPDATE Patients
SET Patient_ID = '212'
WHERE Patient_SSN = '123-45-6780';

UPDATE Patients
SET Patient_ID = '213'
WHERE Patient_SSN = '234-56-7891';

UPDATE Patients
SET Patient_ID = '214'
WHERE Patient_SSN = '345-67-8902';

select *  from Patients;

-- Insert values into the Bills table
INSERT INTO Bills (Patient_id, Bill)
VALUES 
(201, 500.00),
(202, 750.50),
(203, 300.75),
(204, 620.40),
(205, 250.00),
(206, 430.00),
(207, 390.00),
(208, 280.25),
(209, 100.00),
(210, 870.60);

select* From Bills;

INSERT INTO Medicines (patient_id, medicine_name, cost, quantity, date) VALUES
(201, 'Paracetamol', 50.00, 10, '2024-11-10'),
(202, 'Ibuprofen', 30.00, 5, '2024-11-10'),
(203, 'Amoxicillin', 150.00, 2, '2024-11-10'),
(204, 'Cough Syrup', 60.00, 3, '2024-11-11'),
(205, 'Vitamin C', 20.00, 15, '2024-11-12'),
(206, 'Insulin', 200.00, 1, '2024-11-13'),
(207, 'Pain Relief Ointment', 45.00, 4, '2024-11-14'),
(208, 'Antibiotic Cream', 75.00, 2, '2024-11-14'),
(209, 'Aspirin', 25.00, 10, '2024-11-15'),
(210, 'Antacid', 15.00, 7, '2024-11-16');

select*from Medicines;

INSERT INTO Treatments (patient_id, doctor_id, treatment, treatment_code, treatment_cost, treatment_date) VALUES
(201, 101, 'Physiotherapy', 'PT-001', 500.00, '2024-10-10'),
(202, 102, 'Chemotherapy', 'CT-002', 2500.00, '2024-10-11'),
(203, 103, 'Radiation Therapy', 'RT-003', 3000.00, '2024-10-12'),
(204, 104, 'Cardiac Surgery', 'CS-004', 15000.00, '2024-10-13'),
(205, 105, 'Dialysis', 'DL-005', 800.00, '2024-10-14'),
(206, 106, 'Kidney Transplant', 'KT-006', 50000.00, '2024-10-15'),
(207, 107, 'Orthopedic Surgery', 'OS-007', 12000.00, '2024-10-16'),
(208, 108, 'General Checkup', 'GC-008', 300.00, '2024-10-17'),
(209, 109, 'Physical Therapy', 'PT-009', 600.00, '2024-10-18'),
(210, 110, 'Neurological Exam', 'NE-010', 1000.00, '2024-10-19');

select*from Treatments;

INSERT INTO Insurance (Company_ID, Company_Name, Phone_Number)
VALUES 
(100, 'AARP', 2024343525),
(101, 'Aetna', 8008723862),
(102, 'Amerigroup', 8006004441),
(103, 'CareSource', 8004880134),
(104, 'Humana', 8004574708),
(105, 'Cigna', 8009971654),
(106, 'Health Net', 8006756110),
(107, 'Anthem', 8003311476),
(108, 'Centene Corporation', 3147254477),
(109, 'Kemper Corporation', 8668609348),
(110, 'EmblemHealth', 8662740060);