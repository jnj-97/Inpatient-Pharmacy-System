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
    The data of the table is taken from Sheet4 of the Document
    
    Patient_table which consists of the Patient Name, Id number, Ward and Precribed Medicines
    The format of the table is 'Patient_id' | 'Name' | 'Ward' | 'Prescribed Medicines'
    Each patient is initialised with no or None medication as this is only the initial database
    The data of the table is taken from Sheet3 of the Document
    
    Stock_table which consists of the medication available in the Pharmacy stock and the quantity of each Medication
    The format of the table is 'Medicine Name' | 'Units Remaining'
    The data of the table is taken from Sheet5 of the document
    
   The tables are initialed by using the module openpyxl which supports .xlsx documents
   A for loop is created where the for loop iterates through each row of each sheet and collects data from each cell
   The for loop exits when it reaches max_row + 1 row where max row returns the last row of the sheet with any data entered
   The data collected from the sheet is then placed in a dictionary where the keys are the database table column names and the value is the data from the sheet     
   It is then inserted into the table using the function table_name.insert_one(dict) from pymongo module
   This entire process is enclosed in a class for encapsulation purposes. The entire process in enclosed within the class's __init__ function. Hence the initialisation can be      done by calling an object of the class 
   
  Doctor.py
    This script is meant for use by doctors where they can view patient records and modify medications as well as discharge them
    It makes use of the modules from previous script as well as tkinter for a user friendly gui and datetime for record puprposes
    New Tables such as a Record Table, Added Table and Position table are introduced
    A tkinter window is created with 600x420 Geometry and Doctor Portal Title.
    A background image is created using PIL(Python Image Library)
    Various Labels, Input Boxes and OptionMenus(Dropdowm menus) are created and some are placed using place and grid
    The doctor enters thier id and Name in the respective input boxes
    The entries are checked in the database
    if exists:
      The input boxes,labels, and buttons created for Doctor id and name entries are destroyed
      the Patients present in the same ward as the doctor is fetched using find() function and stored in a list which are used as inputs for an Optionmenu
    else:
      "wrong input, try again" Label is placed
    After Logging in and getting the patients optionment there are two buttons View Old Records and Create New Records
    On clicking Create New Records Button:
      Labels Such as Remarks, Current Medication and Remove Medication are Created 
      A Textbox where doctors can add remarks is created. On clicking the add button a dictionary is created in the following format
      {'Doctor_id':doctor_id,'Patient_id':patient_id,'Date':datetime.datetime.now(),'Remark':Remark}
      This dictionary is added into the record table
      A label "Added" is placed with a constant x coordinate
      The labels y coordinate is added into the added table
      next time the ADD button is clicked the Added label will have the y coordinate from added table
      the added tables entry will be increased by 30
      This is so multiple "Added" Labels are placed one below the other
      this method is used multiple times and will be referred as the __ADDDED Label Method__
      The list of medication is fetched from the patient table and is placed one below the other using the ADDED Label Method
      The lsit of medication for a patient is stored in the patient table in the form medicine1.medicine2.medicine3...
      If Prescribed Medicines is None then a None label is placed
      The medicines are fetched using the split() function
      The List of mediciation from the stock table are fetched and stored in a list used as Input for an OptionMenu
      Below that an add button is placed where doctors can prescribe medicine
      If patient has no prescribed medicine then the medicine replaces None
      else Patient['Prescribed Medcicines']=Patient['Prescribed Medcicines'] +'.{}'.format(medicine)
      Everytime the add button is clicked 'ADDED' labels are placed using ADDED Label Method
      A OptionMenu consisting of all the Patients Medication is placed
      A Remove button is placed below the OptionMenu. Doctors can Remove medication using these elements
      When the Remove Button is clicked:
      if len(Patient['Prescribed Medicine'].split('.'))==1 #indicates patient has only one medicine prescribed
        Patient['Prescribed Medicine']=None
       else:
        x=''
        for medicines in Patient['Prescribed Medicine'].split('.'):
          if medicines==clicked medicine:
            pass
          else:
          x=x+medicines
        Patient['Prescribed Medicine']=x
      If Prescribed Medicines is None then a None label is placed
      A close button is placed at the bottom which destroyes the tk window using tk.destroy()
     If View Old Records Button is Clicked
      Labels Such as Date,Remarks and Medication are Created
      All the Records of the selected patient are fetched from the Record table and displayed one below the other using ADDED Label Method
      If there are no Records a NONE Label is placed 
      The medication of the patient is fetched from the patient table and displayed one below the other using split() and ADDED Label Method
      If there are no Medications a NONE Label is placed
      A Discharge button is placed at the bottom of the window. On clicking this button the patient's dictionary is deleted from the patient table using the delete_one(dict)           method
      A close button is placed at the bottom which destroyes the tk window using tk.destroy()
      
     Nurse.py
      This script is meant for use by nurses where they can view medications from their ward which they have to supply for the day
      A tkinter window is created with 600x420 Geometry and Nurse Portal Title.
      A background image is created using PIL(Python Image Library)
      Various Labels, Input Boxes and OptionMenus(Dropdowm menus) are created and some are placed using place and grid
      The nurse enters thier id and Name in the respective input boxes
      The entries are checked in the database
      if exists:
       The input boxes,labels, and buttons created for Nurse id and name entries are destroyed
        the Patients present in the same ward as the nurse is fetched using find() function
        for items in the list:
          Name is placed
          for prescribed medicines.split() in name:
            if None:
              pass
            else:
              Each medicine is placed one after the other using the ADDED Label Method but the x coordinate varies instead of y coordinate
    else:
      "wrong input, try again" Label is placed
    
   server.py
    It makes use of the modules from previous script as well as selenium for ordering medicines from the mock website
    id_table is introduced 
    The format of the table is 'Medicine Name' | 'id'
    The ids are the html id names of the buttons in the mock website. This allows us to click certain buttons according to conditions
    An infinite loop is introduced, hence this code runs infinitely
      Whithin this loop if the time is 8am or 2 pm or 8 pm
        The list of patients with prescribed medication is fetched
          for medicine in prescribed medication
            the quantity of medication in stock table is reduced by 1
           this simulates the consumption of medication by patients
        The list of medication in stock table where quantity is less than 10 is fetched 
          A chrome web driver object for selenium is introduced. This allows selenium web automation using chrome browser
          The web driver fetches the mock site, in this code the site was being hosted on localmachine using a simpleHTTP python server. The mock website is also available at 
          http://jagadeeswar300.github.io/medicines/
          We fetch the id of the low quantity medicines from id table and click the corresponding button. We then checkout the button
          We fetch the price of the buttons from medicine price table and add it to a total price 
          We store all the medicines we ordered in a list
          At the end of the for loop, we print the medicine name, its price and the total price
          
I hope this document helps as i have spent a lot of time typing it
          
          
    
