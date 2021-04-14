import PIL.Image
from PIL import ImageTk
import datetime
from tkinter import *
import pymongo
client=pymongo.MongoClient()
Medicine=client.Medical_Database
Doctor=client.Doctor_Database
Record=client.Record_Database
Nurse=client.Nurse_Database
Stock=client.Stock_Database
Patient=client.Patient_Database
Date_db=client.Date_Database
medicine_price_table=Medicine.Table
Doctor_table=Doctor.Table
Nurse_table=Nurse.Table
Patient_table=Patient.Table
Stock_table=Stock.Table
Record_table=Record.Table
Date_table=Date_db.Table
position=client.Position_Database
position_table=position.Table
added=client.Added_Database
added_table=added.Table
added_table.drop()
position_table.drop()
def discharge():
    selection=clicked.get().split(':')
    Patient_table.delete_one({'Patient_id':selection[0]})
    Record_table.delete_many({'Patient_id':selection[0]})
    window.destroy()
def oldrecord():
    selection=clicked.get().split(':')
    Label(window,text='Date',bg='white',fg='black',font=('calibre',14,'bold')).place(x=10,y=130)
    Label(window,text='Remarks',bg='white',fg='black',font=('calibre',14,'bold')).place(x=150,y=130)
    window.geometry('900x800')
    records=[]
    for document in Record_table.find({'Patient_id':selection[0]}):
        records.append(document)
    y_value=190
    if(len(records)==0):
        Label(window,text='None',bg='white',fg='black',font=('calibre',15,'normal')).place(x=10,y=160)
    else:
        for record in records:
            Label(window,text=record['Date'].strftime('%d/%m/%y %I:%M %p')).place(x=10,y=y_value)
            Label(window,text=record['Remark'],bg='white',fg='black').place(x=150,y=y_value)
            y_value=y_value+40
    Label(window,text='Medication',fg='black',bg='white',font=('calibre',14,'bold')).place(x=10,y=y_value)
    patient=Patient_table.find_one({'Patient_id':selection[0]})
    if patient['Prescribed Medicines']==None:
        Label(window,text='None',fg='black',bg='white',font=('calibre',14,'normal')).place(x=10,y=y_value+30)
    else:
        p_medicine=patient['Prescribed Medicines'].split('.')
        y_value=y_value+30
        for medicines in p_medicine:
            Label(window,text=medicines,bg='white',fg='black').place(x=10,y=y_value)
            y_value=y_value+30
    Button(window,text='Discharge',bg='green',fg='white',font=('calibre',14,'bold'),command=discharge).place(x=700,y=670)
    Button(window,text='Close',bg='red',fg='white',font=('calibre',14,'bold'),command=window.destroy).place(x=820,y=670)
def addrecord():
    Record_table.insert_one({'Doctor_id':d_id.get(),'Patient_id':clicked.get().split(':')[0],'Date':datetime.datetime.now(),'Remark':Remark.get('1.0','end-1c')})
    Label(window,text='ADDED',fg='black',bg='white').place(x=200,y=added_table.find_one()['position'])
    new_position=added_table.find_one()['position']+30
    added_table.drop()
    added_table.insert_one({'position':new_position}) 
def addmedicine():
    Label(window,text='ADDED',fg='black',bg='white').place(x=500,y=position_table.find_one()['position'])
    if Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})['Prescribed Medicines']==None:
        old_dict=Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})
        new_dict={'Patient_id':old_dict['Patient_id'],'Name':old_dict['Name'],'Ward':old_dict['Ward'],'Prescribed Medicines':medicine_name.get()}
        Patient_table.find_one_and_replace(old_dict,new_dict)
    else:
        old_dict=Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})
        new_dict={'Patient_id':old_dict['Patient_id'],'Name':old_dict['Name'],'Ward':old_dict['Ward'],'Prescribed Medicines':old_dict['Prescribed Medicines']+".{}".format(medicine_name.get())}
        Patient_table.find_one_and_replace(old_dict,new_dict)
    new_position=position_table.find_one()['position']+30
    position_table.drop()
    position_table.insert_one({'position':new_position})
def removemedicine():
    if len(Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})['Prescribed Medicines'].split('.'))==1:
        old_dict=Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})
        new_dict={'Patient_id':old_dict['Patient_id'],'Name':old_dict['Name'],'Ward':old_dict['Ward'],'Prescribed Medicines':None}
        Patient_table.find_one_and_replace(old_dict,new_dict)
    else:
        old_dict=Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})
        m_list=old_dict['Prescribed Medicines'].split('.')
        m_list.remove(remove_medicine.get())
        x=''
        for things in m_list:
            if things==m_list[0]:
                x+=things
            else:
                x+='.{}'.format(things)
        new_dict={'Patient_id':old_dict['Patient_id'],'Name':old_dict['Name'],'Ward':old_dict['Ward'],'Prescribed Medicines':x}
        Patient_table.find_one_and_replace(old_dict,new_dict)
    Label(window,text='Removed',fg='black',bg='white').place(x=50,y=added_table.find_one()['position']+100)
    yvalue=added_table.find_one()['position']
    added_table.drop()
    added_table.insert_one({'position':yvalue+30})
        
def newrecord():
    window.geometry('700x900')
    Label(window,text='Enter Remarks',fg='black',bg='white',font=('calibre',14,'bold')).place(x=10,y=130)
    Remark.place(x=10,y=160)
    Button(window,text='ADD',bg='green',fg='white',font=('calibre',14,'bold'),command=addrecord).place(x=370,y=270)
    Label(window,text='Current Medication',fg='black',bg='white',font=('calibre',14,'bold')).place(x=450,y=130)
    patient_dict=Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})
    medication_position=160
    if patient_dict['Prescribed Medicines']==None:
        None_label=Label(window,text='None',fg='black',bg='white').place(x=450,y=medication_position)
        medication_position=medication_position+30
    else:
        for things in patient_dict['Prescribed Medicines'].split('.'):
            Label(window,text=things,fg='black',bg='white').place(x=450,y=medication_position)
            medication_position=medication_position+30
    medicine_list=[]
    for document in Stock_table.find():
        medicine_list.append(document['Medicine Name'])
    medicine_name.set(medicine_list[0])
    OptionMenu(window,medicine_name,*medicine_list).place(x=450,y=medication_position)
    position_table.drop()
    position_table.insert_one({'position':medication_position+100})
    added_table.insert_one({'position':300})
    Button(window,text='ADD',bg='green',fg='white',font=('calibre',14,'bold'),command=addmedicine).place(x=550,y=medication_position+70)
    #print(Remark.get('1.0','end-1c'))   
    Label(window,text="Remove Medication",bg='white',fg='black',font=('calibre',14,'bold')).place(x=10,y=added_table.find_one()['position']+30)
    rmedicine_list=[]
    if Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})['Prescribed Medicines']==None:
        Label(window,text='Patient is not Under Medication',fg='black',bg='white').place(x=10,y=added_table.find_one()['position']+60)
        yvalue=added_table.find_one()['position']+90
        added_table.drop()
        added_table.insert_one({'position':yvalue})
    else:
        for patient in Patient_table.find_one({'Patient_id':clicked.get().split(':')[0]})['Prescribed Medicines'].split('.'):
            rmedicine_list.append(patient)
        remove_medicine.set(rmedicine_list[0])
        OptionMenu(window, remove_medicine, *rmedicine_list).place(x=10,y=added_table.find_one()['position']+60)
        Button(window,text='REMOVE',fg='white',bg='red',font=('calibre',14,'bold'),command=removemedicine).place(x=50,y=added_table.find_one()['position']+100)
        yvalue=added_table.find_one()['position']
        added_table.drop()
        added_table.insert_one({'position':yvalue+150})
    Button(window,text='Close',bg='red',fg='white',font=('calibre',14,'bold'),command=window.destroy).place(x=620,y=690)
def output():
    if bool(Doctor_table.find_one({'Doctor_id':d_id.get(),'Name':name.get()})):
        n.destroy()
        login.grid_forget()
        nbox.destroy()
        i.destroy()
        idbox.destroy()
        b.destroy()
        wrong.place_forget()
        doctor_dict=Doctor_table.find_one({'Doctor_id':d_id.get(),'Name':name.get()})
        Label(window,text='Select Patient',bg='white',fg='black',font='15').place(x=10,y=30)
        wardpatients=[]
        for document in Patient_table.find({'Ward':doctor_dict['Ward']}):
            wardpatients.append('{}:{}'.format(document['Patient_id'],document['Name']))
        clicked.set(wardpatients[0])
        OptionMenu(window,clicked,*wardpatients).place(x=10,y=60)
        Button(window,text='View Old Records',bg='white',fg='black',command=oldrecord).place(x=10,y=100)
        Button(window,text='Create New Record',bg='white',fg='black',command=newrecord).place(x=130,y=100)
    else:
        wrong.place(x=200,y=400)
window=Tk()
window.geometry('600x420')
window.title("Doctor Portal")
im1 = PIL.Image.open("doctor_bg.jpg")
im=im1.resize((1000,620))
ph = ImageTk.PhotoImage(im)
background_label =Label(window, image=ph).place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text='Doctor Portal',font='Helvetica 18 bold',bg='white').grid(row=0,column=0)
window.columnconfigure(0, weight=1)
login=Label(window,text="Login",font='Helvetica 50 bold',bg='white',fg='red')
login.grid(row=1,column=0)
name=StringVar()
d_id=StringVar()
clicked=StringVar()
medicine_name=StringVar()
remove_medicine=StringVar()
n=Label(window,font="14",text="Name",bg='white',fg='black')
nbox=Entry(window,textvariable = name, font=('calibre',10,'normal'),width=30)
i=Label(window,font="14",text="ID Number",bg='white',fg='black')
idbox=Entry(window,textvariable = d_id, font=('calibre',10,'normal'),width=30)
b=Button(window,text='Submit',bg='black',command=output,fg='white')
Remark=Text(window,bg='white',fg='black',width=50,height=6)
n.place(x=200,y=130)
nbox.place(x=200,y=170)
i.place(x=200,y=200)
idbox.place(x=200,y=230)
b.place(x=370,y=260)
wrong=Label(window,text="Invalid Credentials, Please Try Again",bg='white',fg='black')
window.mainloop()