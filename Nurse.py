
import PIL.Image
from PIL import ImageTk
from tkinter import *
import pymongo
client=pymongo.MongoClient()
Nurse=client.Nurse_Database
Patient=client.Patient_Database
Nurse_table=Nurse.Table
Patient_table=Patient.Table
def output():
    print('Hi')
    if bool(Nurse_table.find_one({'Nurse_id':d_id.get(),'Name':name.get()})):
        n.destroy()
        login.grid_forget()
        nbox.destroy()
        i.destroy()
        idbox.destroy()
        b.destroy()
        wrong.place_forget()
        nurse_dict=Nurse_table.find_one({'Nurse_id':d_id.get(),'Name':name.get()})
        Label(window,text='Patient Medication for Today',bg='white',fg='black',font='15').place(x=10,y=30)
        y_value=60
        for document in Patient_table.find({'Ward':nurse_dict['Ward']}):
            if document['Prescribed Medicines']==None:
                pass
            else:
                Label(window,text='{} -'.format(document['Name']),fg='black',bg='white').place(x=10,y=y_value)
                x_value=100
                for things in document['Prescribed Medicines'].split('.'):
                    Label(window,text=things,fg='black',bg='white').place(x=x_value,y=y_value)
                    x_value=x_value+100
                y_value=y_value+30
    else:
        wrong.place(x=200,y=400)
window=Tk()
window.geometry('600x420')
window.title("Nurse Portal")
im1 = PIL.Image.open("nurse_bg.jpg")
im=im1.resize((1000,620))
ph = ImageTk.PhotoImage(im)
background_label =Label(window, image=ph).place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text='Nurse Portal',font='Helvetica 18 bold',bg='white').grid(row=0,column=0)
window.columnconfigure(0, weight=1)
login=Label(window,text="Login",font='Helvetica 50 bold',bg='white',fg='red')
login.grid(row=1,column=0)
name=StringVar()
d_id=StringVar()
clicked=StringVar()
medicine_name=StringVar()
n=Label(window,font="14",text="Name",bg='white',fg='black')
nbox=Entry(window,textvariable = name, font=('calibre',10,'normal'),width=30)
i=Label(window,font="14",text="ID Number",bg='white',fg='black')
idbox=Entry(window,textvariable = d_id, font=('calibre',10,'normal'),width=30)
b=Button(window,text='Submit',bg='black',command=output,fg='white')
n.place(x=200,y=130)
nbox.place(x=200,y=170)
i.place(x=200,y=200)
idbox.place(x=200,y=230)
b.place(x=370,y=260)
wrong=Label(window,text="Invalid Credentials, Please Try Again",bg='white',fg='black')
window.mainloop()