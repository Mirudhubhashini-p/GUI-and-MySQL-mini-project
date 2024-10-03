from tkinter import*
from tkinter import messagebox
import mysql.connector
#creating function for createbtn

def createData():
    id=enterId.get()
    name=enterName.get()
    dept=enterDept.get()

    if(id==""or name=="" or dept==""):
        messagebox.showwarning("Cannot insert","All the fields are required!")
    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="Systemmysql1809",database="employee")
        myCur=myDB.cursor()
        myCur.execute("insert into empdetails values('"+id+"','"+name+"','"+dept+"')")
        myDB.commit()


        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()

        messagebox.showinfo("Create Status","Data Created Successfully!")
        myDB.close()
    
def updateData():
    id=enterId.get()
    name=enterName.get()
    dept=enterDept.get()

    if(id==""or name=="" or dept==""):
        messagebox.showwarning("Cannot Update","All the fields are required!")
    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="Systemmysql1809",database="employee")
        myCur=myDB.cursor()
        myCur.execute("update empdetails set empName='"+name+"',empDept='"+dept+"' where empId='"+id+"'")
        myDB.commit()


        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()

        messagebox.showinfo("Updated Status","Data Updated Successfully!")
        myDB.close()

def readData():
    if(enterId.get()==""):
        messagebox.showwarning("Cannot Read","Please provide EmployeeId to read the data")
    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="Systemmysql1809",database="employee")
        myCur=myDB.cursor()
        myCur.execute("select * from empdetails where empId='"+enterId.get()+"'")
        
        rows=myCur.fetchall()

        for row in rows:
            enterName.insert(0,row[1])
            enterDept.insert(0,row[2])
        


def deleteData():
    if(enterId.get()==""):
        messagebox.showwarning("Cannot Read","Please provide EmployeeId to delete the data")
    else:
        myDB=mysql.connector.connect(host="localhost",user="root",password="Systemmysql1809",database="employee")
        myCur=myDB.cursor()
        myCur.execute("delete from empdetails where empId='"+enterId.get()+"'")
        myDB.commit()
        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()

        messagebox.showinfo("Delete Status","Data Deleted Successfully!")
        myDB.close()
def show():
    myDB=mysql.connector.connect(host="localhost",user="root",password="Systemmysql1809",database="employee")
    myCur=myDB.cursor()
    myCur.execute("select * from empdetails")
    rows=myCur.fetchall()
    showData.delete(0,showData.size())
    for row in rows:
        addData=str(row[0])+' ' +row[1]+' '+row[2]
        showData.insert(showData.size()+1,addData)
    myDB.close()


window=Tk()
window.geometry("600x600")
window.title("Employee CRUD App")
# Creating Labels

empId=Label(window,text="Employee ID",font=("Serif",12),fg="Black")
empId.place(x=20,y=30)
empName=Label(window,text="Employee Name",font=("Serif",12),fg="Black")
empName.place(x=20,y=60)
empDept=Label(window,text="Employee Depart",font=("Serif",12),fg="Black")
empDept.place(x=20,y=90)

# Creating inputs

enterId=Entry(window)
enterId.place(x=170,y=30)
enterName=Entry(window)
enterName.place(x=170,y=60)
enterDept=Entry(window)
enterDept.place(x=170,y=90)
# Creating Buttons

createBtn=Button(window,text="Create",bg="White",fg="Black",command=createData)
createBtn.place(x=20,y=160)

UpdateBtn=Button(window,text="Update",bg="White",fg="Black",command=updateData)
UpdateBtn.place(x=80,y=160)

readBtn=Button(window,text="Read",bg="White",fg="Black",command=readData)
readBtn.place(x=150,y=160)

deleteBtn=Button(window,text="Delete",bg="White",fg="Black",command=deleteData)
deleteBtn.place(x=210,y=160)


#Listbox creating

showData=Listbox(window)
showData.place(x=330,y=30)
show()
window.mainloop()
