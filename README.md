# Inpatient-Pharmacy-System
project which maintains a database of Patients, Doctors, Medication and automatically orders medicine from a mock website when medicine stock is low as Patients Consume Them

This project consists of 4 python Scripts
  dbinit.py
  This python script initialises the database using the data from the document Medicines.xlsx
  The Database Consists of 5 major tables
    
    medicine_price_table which consists of the price and packaging of the medicines in the mock website 
    The format of the table is 'Medicine Name'|'Package units'|'Price' where Package units is the number of Tablets you get in one package of the medicine at the price of 'Price'
    The data of the table is taken from Sheet1 of the Document
  
    Doctor_table which consists of the Doctor Name, Id number and Ward duty 
    The Format of the table is 'Doctor_id' | 'Name' | 'Ward'
    The data of the table is taken from Sheet2 of the Document
    
    Nurse_table which consists of the Nurse Name, Id number and Ward duty
    The format of the table is 'Nurse_id' | 'Name' | 'Ward'
    The data of the table is taken from Sheet3 of the Document
    
    Patient_table which consists of the Patient Name, Id number, Ward and Precribed Medicines
    The format of the table is 'Patient_id' | 'Name' | 'Ward' | 'Prescribed Medicines'
    Each patient is initialised with no or None medication as this is only the initial database
    
  
