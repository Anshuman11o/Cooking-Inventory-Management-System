from tkinter import * #importing tkinter-GUI
from tkinter import messagebox
import Backend #importing Backend.py file to establish connection

#view command for the reports table, it is called when the view button in the reports screen is pressed
def view_command_report(): 
    Backend.insert_report()
    my_tuple = Backend.view_report()
    my_record = my_tuple[0]
    first_val = my_record[1]
    second_val = my_record[2]
    third_val = my_record[3]
    e15.delete("0",END)
    e15.insert(END,first_val)
    e16.delete("0",END)
    e16.insert(END,second_val)
    e17.delete("0",END)
    e17.insert(END,third_val) #displaying data in a textbox
    
#select function for the table menu, helps in identifying the tuple selected in the listbox according to their index
def get_selected_row_men(event):
    #assigning a global variable, which will be used within the other forntend fucntions for connection with backend
    global selected_tuple_men 
    index_men = list_men.curselection()[0]
    selected_tuple_men=list_men.get(index_men)
    e12.delete(0,END)
    e12.insert(END,selected_tuple_men[0])
    e13.delete(0,END)
    e13.insert(END,selected_tuple_men[1]) #selected tuple values are displayed in the specific entry box

def error():
    messagebox.showerror('Empty field Error', 'Error: One or more fields are empty!')

#view command for the menu table is called when the view all button is pressed
def view_command_men():
    list_men.delete(0,END)
    for row in Backend.view_men():
        list_men.insert(END,row) #shows all the records in the listbox

#add command for the menu table is called when the add entry button is pressed
#deletes the listbox records and entry values temporarily and adds the new record into the listbox, added by the user
def add_command_men():
    if (dnm_text.get()==""):
        error()
        if (pn_integer.get()==""):
            error()
    else:
        Backend.insert_men(dnm_text.get(),pn_integer.get())
        list_men.delete(0,END)
        list_men.insert(END,(dnm_text.get(),pn_integer.get())) 

#delete command for the menu table is called when the delete button is pressed, it deletes the selected record in the listbox
def delete_command_men():
    Backend.delete_men(selected_tuple_men[0]) #making use of the global variable

#update command for the menu table is called when the update button is pressed, it updates the new values inputted by the user in the listbox
def update_command_men():
    Backend.update_men(dnm_text.get(),pn_integer.get())
    view_command_men()

#similar select, view, add, delete, and update functions connected with the backend (database) for the orders table
def get_selected_row_ord(event):
    global selected_tuple_ord
    index_ord=list_ord.curselection()[0]
    selected_tuple_ord=list_ord.get(index_ord)
    e8.delete(0,END)
    e8.insert(END,selected_tuple_ord[1])
    e9.delete(0,END)
    e9.insert(END,selected_tuple_ord[2])
    e10.delete(0,END)
    e10.insert(END,selected_tuple_ord[3])
    e11.delete(0,END)
    e11.insert(END,selected_tuple_ord[4])

def view_command_ord():
    list_ord.delete(0,END)
    for row in Backend.view_ord():
        list_ord.insert(END,row)

def add_command_ord():
    if (cn_text.get()==""):
        error()
        if(dno_text.get()==""):
            error()
            if(qo_integer.get()==""):
                error()
                if(od_text.get()==""):
                    error()
    else:
        Backend.insert_ord(cn_text.get(),dno_text.get(),qo_integer.get(),od_text.get())
        list_ord.delete(0,END)
        list_ord.insert(END,(cn_text.get(),dno_text.get(),qo_integer.get(),od_text.get()))
    

def delete_command_ord():
    Backend.delete_ord(selected_tuple_ord[0])


def update_command_ord():
    Backend.update_ord(selected_tuple_ord[0],cn_text.get(),dno_text.get(),qo_integer.get(),od_text.get())
    view_command_ord()

#similar select, view, add, delete, and update functions connected with the backend (database) for the inventory table
def get_selected_row_inv(event):
    global selected_tuple_inv
    index=list_inv.curselection()[0]
    selected_tuple_inv=list_inv.get(index)
    e3.delete(0,END)
    e3.insert(END,selected_tuple_inv[0])
    e4.delete(0,END)
    e4.insert(END,selected_tuple_inv[1])
    e5.delete(0,END)
    e5.insert(END,selected_tuple_inv[2])
    e6.delete(0,END)
    e6.insert(END,selected_tuple_inv[3])
    
def view_command_inv():
    list_inv.delete(0,END)
    for row in Backend.view():
        list_inv.insert(END,row)

def add_command_inv():
    if (rm_text.get()==""):
        error()
        if(al_integer.get()==""):
            error()
            if(cpm_integer.get()==""):
                error()
                if(au_integer.get()==""):
                    error()
    else:
        Backend.insert(rm_text.get(),al_integer.get(),cpm_integer.get(),au_integer.get())
        list_inv.delete(0,END)
        list_inv.insert(END,(rm_text.get(),al_integer.get(),cpm_integer.get(),au_integer.get()))
    
def delete_command_inv():
    Backend.delete(selected_tuple_inv[0])
    
def update_command_inv():
    Backend.update(rm_text.get(),al_integer.get(),cpm_integer.get(),au_integer.get())
    view_command_inv()


#my menu GUI function
#This function contains all the graphical user interface for the menu screen in tkinter
def My_Menu():

    root6 = Toplevel(root)
    root6.title("My_Menu")
    root6.geometry("670x320")

    Label(root6, text="Dish Name").grid(row=0, column=0)
    global dnm_text     #assigning global text variables and entry boxes
    dnm_text=StringVar()
    global e12
    e12 = Entry(root6,textvariable=dnm_text)
    e12.grid(row=0, column=1)

    Label(root6, text="Price Name").grid(row=0,column=2)
    global pn_integer
    pn_integer=IntVar()
    global e13
    e13 = Entry(root6,textvariable=pn_integer)
    e13.grid(row=0,column=3)

    global list_men   #creating a global listbox for only the my menu screen
    list_men=Listbox(root6, height=17,width=75)
    list_men.grid(row=3, column=0, rowspan=6, columnspan=2)

    sb3=Scrollbar(root6)  #creating a scrollbar to naviagte through the lisbox
    sb3.grid(row=3, column=2, rowspan=6)

    list_men.configure(yscrollcommand=sb3.set)
    sb3.configure(command=list_men.yview)
#using the bind method to call the selection function and to allow tuples being selected in a listbox
    list_men.bind('<<ListboxSelect>>',get_selected_row_men)   
    #assigining commands to every button, which calls a function
    Button(root6, text="View all", width=10,command=view_command_men).grid(row=3, column=3)   
    Button(root6, text="Add entry", width=10,command=add_command_men).grid(row=4, column=3)
    Button(root6, text="Update", width=10,command=update_command_men).grid(row=5, column=3)
    Button(root6, text="Delete", width=10,command=delete_command_men).grid(row=6, column=3)
  
#orders GUI function
#This function contains all the graphical user interface for the orders screen in tkinter
def Orders():

    root4 = Toplevel(root)
    root4.title("Orders")
    root4.geometry("670x350")

    Label(root4, text="Customer Name").grid(row=0, column=0)
    global cn_text
    cn_text=StringVar()
    global e8
    e8 = Entry(root4,textvariable=cn_text)
    e8.grid(row=0, column=1)

    Label(root4, text="Dish Name").grid(row=0,column=2)
    global dno_text
    dno_text=StringVar()
    global e9
    e9 = Entry(root4,textvariable=dno_text)
    e9.grid(row=0,column=3)

    Label(root4, text="Quantity ordered").grid(row=1, column=0)
    global qo_integer
    qo_integer=IntVar()
    global e10
    e10 = Entry(root4,textvariable=qo_integer)
    e10.grid(row=1, column=1)

    Label(root4, text="Order date").grid(row=1,column=2)
    global od_text
    od_text=StringVar()
    global e11
    e11 = Entry(root4,textvariable=od_text)
    e11.grid(row=1, column=3)

    global list_ord
    list_ord=Listbox(root4, height=17,width=75)
    list_ord.grid(row=3, column=0, rowspan=6, columnspan=2)

    sb2=Scrollbar(root4)
    sb2.grid(row=3, column=2, rowspan=6)

    list_ord.configure(yscrollcommand=sb2.set)
    sb2.configure(command=list_ord.yview)

    list_ord.bind('<<ListboxSelect>>',get_selected_row_ord)
    
    Button(root4, text="View all", width=10,command=view_command_ord).grid(row=3, column=3)
    Button(root4, text="Add entry", width=10,command=add_command_ord).grid(row=4, column=3)
    Button(root4, text="Update", width=10,command=update_command_ord).grid(row=5, column=3)
    Button(root4, text="Delete", width=10,command=delete_command_ord).grid(row=6, column=3)

#reports GUI function
#This function contains all the graphical user interface for the reports screen in tkinter
def Reports():

    root3 = Toplevel(root)
    root3.title("Reports")
    root3.geometry("300x250")

    Label(root3, text="Total cost").grid(row=0,column=0)
    global tc_integer
    tc_integer = IntVar()
    global e15
    e15 = Entry(root3,textvariable=tc_integer)
    e15.grid(row=0,column=1)
    Label(root3, text="Total Revenue").grid(row=1,column=0)
    global tr_integer
    tr_integer = IntVar()
    global e16
    e16 = Entry(root3,textvariable=tr_integer)
    e16.grid(row=1,column=1)
    Label(root3, text="Total Profit").grid(row=2,column=0)
    global tp_integer
    tp_integer = IntVar()
    global e17
    e17 = Entry(root3,textvariable=tp_integer)
    e17.grid(row=2,column=1)
    
    Button(root3, text="View", width=30, bg='#B565A7',command=view_command_report).place(x=10, y=150)

#inventory GUI function
#This function contains all the graphical user interface for the inventory screen in tkinter
def Inventory():

    root2 = Toplevel(root)
    root2.title("Inventory")
    root2.geometry("670x350")

    Label(root2, text="Raw material").grid(row=0, column=0)
    global rm_text
    rm_text=StringVar()
    global e3
    e3 = Entry(root2,textvariable=rm_text)
    e3.grid(row=0, column=1)

    Label(root2, text="Amount left").grid(row=0,column=2)
    global al_integer
    al_integer=IntVar()
    global e4
    e4 = Entry(root2,textvariable=al_integer)
    e4.grid(row=0,column=3)

    Label(root2, text="Cost per Material").grid(row=1, column=0)
    global cpm_integer
    cpm_integer=IntVar()
    global e5
    e5 = Entry(root2,textvariable=cpm_integer)
    e5.grid(row=1, column=1)

    Label(root2, text="Amount used").grid(row=1, column=2)
    global au_integer
    au_integer=IntVar()
    global e6
    e6 = Entry(root2,textvariable=au_integer)
    e6.grid(row=1,column=3)

    global list_inv
    list_inv=Listbox(root2, height=17,width=75)
    list_inv.grid(row=3, column=0, rowspan=6, columnspan=2)

    sb1=Scrollbar(root2)
    sb1.grid(row=3, column=2, rowspan=6)

    list_inv.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list_inv.yview)

    list_inv.bind('<<ListboxSelect>>',get_selected_row_inv)

    Button(root2, text="View all", width=10,command=view_command_inv).grid(row=3, column=3)
    Button(root2, text="Add entry", width=10,command=add_command_inv).grid(row=4, column=3)
    Button(root2, text="Update", width=10,command=update_command_inv).grid(row=5, column=3)
    Button(root2, text="Delete", width=10,command=delete_command_inv).grid(row=6, column=3)


#homepage GUI function
#This function contains all the graphical user interface for the homepage screen in tkinter
def Home_page():
    root1 = Toplevel(root) #creating a new window for home page
    root1.title("Home Page")
    root1.geometry("300x250") #assigning a name and size to the new window
    #multiple button options, all calling the different GUI functions created above
    Button(root1, text="Inventory", command=Inventory, height = 3, width = 13, bg='#55B4B0').place(x=10, y=10)
    Button(root1, text="Reports", command=Reports, height = 3, width = 13, bg='#DFCFBE').place(x=10, y=150)
    Button(root1, text="Orders", command=Orders, height = 3, width = 13, bg='#BC243C').place(x=150, y=10)
    Button(root1, text="My Menu", command=My_Menu, height = 3, width = 13, bg='#98B4D4').place(x=150, y=150)
                                                                                        
#login function contains the logic which checks if the inputted username password is correct or not and shows error messages if required
def login_user():
    uname = e1.get() #defining variables for username and password
    password = e2.get()

    if (uname == "admin" and password == "1234"):  #Logic for the login screen
        Home_page()
    
    else:
        messagebox.showerror('Invalid username or password','Entered Username or Password is incorrect, Please try again.')
    

root = Tk()  #creating a new window for login screen
root.title("Login")
root.geometry("350x200")
global e1  #assigning global variables which can be used in the login function
global e2
Label(root, text="Username").place(x=10,y=10) #creating labels
Label(root, text="Password").place(x=10,y=40)

e1 = Entry(root)  #creating entry inputs
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

#creating buttons, which have a command variable that calls a function upon being pressed
Button(root, text="Login", command=login_user, height = 3, width = 13, bg='#FF6F61').place(x=140, y=100)

root.mainloop() #ending the GUI tkinter window