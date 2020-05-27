#importing all modules
from tkinter import *
from functools import partial
import tkinter.messagebox
import ib
ib.connect_database()

#Login form for admin
def admin_login():
    frame.grid_forget()
    global admin_frame
    admin_frame = Frame(tk, bg='Pink')
    admin_frame.grid(padx=500, pady=250)

    label = Label(admin_frame, text="Admin Login", font='bold')
    label.grid(row=0, pady=20)

    label1 = Label(admin_frame, text="Name:")
    label1.grid(row=1, pady=10)

    label2 = Label(admin_frame, text="Password:")
    label2.grid(row=3, pady=10)
    global entry1
    global entry2
    entry1 = Entry(admin_frame)
    entry1.grid(row=2, pady=10)

    entry2 = Entry(admin_frame,show='*')
    entry2.grid(row=4, pady=10)

    button = Button(admin_frame, text="Submit", command=page1)
    button.grid(row=5, pady=20)
    mainloop()

#all buttons of page1
def create_Family():
    def create_fam_in_database():
        def back_to_main_page1_from_create_fam():
            frame_create_fam.grid_forget()
            page1()
        family_no=entry3.get()
        name = entry4.get()
        age = entry15.get()
        address = entry16.get()
        family_member = entry17.get()
        mobile_number = entry26.get ()
        if  len(family_no) != 0 and len(name) != 0 and len(age) != 0 and len(address) != 0 and len(family_member) != 0 and len (mobile_number) != 0 :
            ib.create_Family(family_no,name,age,address,family_member,mobile_number)
            frame_create_fam.grid_forget()
            page1()
        else:
            label = Label(frame_create_fam, text="Please fill all entries")
            label.grid(pady=2)

            button = Button(frame_create_fam, text="Exit", command=back_to_main_page1_from_create_fam, bg='red')
            button.grid()
    page1_frame.grid_forget()

    global frame_create_fam
    frame_create_fam=Frame(tk,bg='pink')
    frame_create_fam.grid(padx=500,pady=200)

    label=Label(frame_create_fam,text='Family_no:',font='bold')
    label.grid(row=0,pady=4)
    global entry3
    entry3=Entry(frame_create_fam)
    entry3.grid(row=1,pady=4)

    label1=Label(frame_create_fam,text='Name:',font='bold')
    label1.grid(row=2,pady=4)
    global entry4
    entry4=Entry(frame_create_fam)
    entry4.grid(row=3,pady=4)
    label2=Label(frame_create_fam,text='Age',font='bold')
    label2.grid(row=4,pady=4)
    global entry15
    entry15=Entry(frame_create_fam)
    entry15.grid(row=5,pady=4)
    label3 = Label(frame_create_fam, text='Address',font='bold')
    label3.grid(row=6,pady=4)
    global entry16
    entry16 = Entry(frame_create_fam)
    entry16.grid(row=7,pady=4)
    label4 = Label(frame_create_fam, text='Family_members',font='bold')
    label4.grid(row=8,pady=4)
    global entry26
    entry26 = Entry(frame_create_fam)
    entry26.grid(row=9,pady=4)
    label6 = Label(frame_create_fam, text='Mobile_Number',font='bold')
    label6.grid(row=10,pady=4)
    global entry17
    entry17 = Entry(frame_create_fam)
    entry17.grid(row=11,pady=4)

    button=Button(frame_create_fam,text='Submit',command=create_fam_in_database,width=15,height=2)
    button.grid(row=12,pady=4)

    mainloop()

#all buttons of page1
def create_Agent():
    def create_ag_in_database():
        def back_to_main_page1_from_create_ag():
            frame_create_ag.grid_forget()
            page1()
        Name=entry7.get()
        Mobile_no = entry27.get ()
        Address = entry36.get ()
        Report = entry28.get ()
        if  len(Name) != 0 and len(Mobile_no) != 0 and len(Address) != 0 and len(Report) != 0 :
            ib.create_Agent(Name,Mobile_no,Address,Report)
            frame_create_ag.grid_forget()
            page1()
        else:
            label = Label(frame_create_ag, text="Please fill all entries")
            label.grid(pady=2)

            button = Button(frame_create_ag, text="Exit", command=back_to_main_page1_from_create_ag, bg='red')
            button.grid()
    page1_frame.grid_forget()

    global frame_create_ag
    frame_create_ag=Frame(tk,bg='pink')
    frame_create_ag.grid(padx=500,pady=200)

    
    label11=Label(frame_create_ag,text='Name:',font='bold')
    label11.grid(row=0,pady=4)
    global entry7
    entry7=Entry(frame_create_ag)
    entry7.grid(row=1,pady=4)

    label12=Label(frame_create_ag,text='Mobile_No',font='bold')
    label12.grid(row=2,pady=4)
    global entry27
    entry27=Entry(frame_create_ag)
    entry27.grid(row=3,pady=4)
    
    label13=Label(frame_create_ag,text='Address',font='bold')
    label13.grid(row=4,pady=4)
    global entry36
    entry36=Entry(frame_create_ag)
    entry36.grid(row=5,pady=4)
    
    label15 = Label(frame_create_ag, text='Report',font='bold')
    label15.grid(row=6,pady=4)
    global entry28
    entry28=Entry(frame_create_ag)
    entry28.grid(row=7,pady=4)
    
    button=Button(frame_create_ag,text='Submit',command=create_ag_in_database,width=15,height=2)
    button.grid(row=8,pady=4)

    mainloop()

#all buttons of page1
def create_Grocery():
    def create_gro_in_database():
        def back_to_main_page1_from_create_gro():
            frame_create_gro.grid_forget()
            page1()
        item=entry33.get()
        name = entry34.get()
        quantity = entry35.get()
        address = entry36.get()
        amount = entry37.get()
        if  len(item) != 0 and len(name) != 0 and len(quantity) != 0 and len(address) != 0 and len(amount) != 0 :
            ib.create_Grocery(item,name,quantity,address,amount)
            frame_create_gro.grid_forget()
            page1()
        else:
            label = Label(frame_create_gro, text="Please fill all entries")
            label.grid(pady=2)

            button = Button(frame_create_gro, text="Exit", command=back_to_main_page1_from_create_gro, bg='red')
            button.grid()
    page1_frame.grid_forget()

    global frame_create_gro
    frame_create_gro=Frame(tk,bg='pink')
    frame_create_gro.grid(padx=500,pady=200)

    label=Label(frame_create_gro,text='Item Number',font='bold')
    label.grid(row=0,pady=4)
    global entry33
    entry33=Entry(frame_create_gro)
    entry33.grid(row=1,pady=4)

    label31=Label(frame_create_gro,text='Name',font='bold')
    label31.grid(row=2,pady=4)
    global entry34
    entry34=Entry(frame_create_gro)
    entry34.grid(row=3,pady=4)
    
    label32=Label(frame_create_gro,text='Quantity',font='bold')
    label32.grid(row=4,pady=4)
    global entry35
    entry35=Entry(frame_create_gro)
    entry35.grid(row=5,pady=4)
    
    label33 = Label(frame_create_gro, text='Address',font='bold')
    label33.grid(row=6,pady=4)
    global entry36
    entry36 = Entry(frame_create_gro)
    entry36.grid(row=7,pady=4)
    
    label34 = Label(frame_create_gro, text='Amount',font='bold')
    label34.grid(row=8,pady=4)
    global entry37
    entry37 = Entry(frame_create_gro)
    entry37.grid(row=9,pady=4)

    button=Button(frame_create_gro,text='Submit',command=create_gro_in_database,width=15,height=2)
    button.grid(row=10,pady=4)

    mainloop()


def show_Agent():
    def back_to_main_page1():
        show_ag_frame.grid_forget()
        page1()
    page1_frame.grid_forget()

    global show_ag_frame
    show_ag_frame=Frame(tk)
    show_ag_frame.grid(padx=50,pady=50)

    label=Label(show_ag_frame,text='Name\t\t\tReport',font='bold')
    label.grid(row=0)

    details=ib.show_Agent()

    for i in details:
        label=Label(show_ag_frame,text="{}\t\t\t{}".format(i[0],i[1]))
        label.grid(pady=4)

    button=Button(show_ag_frame,text='Exit',command=back_to_main_page1,width=20,height=2,bg='red',font='bold')
    button.grid()

    mainloop()

def back_to_main():
    page1_frame.grid_forget()
    global frame
    frame = Frame(tk, bg='Pink')
    frame.grid(padx=500, pady=250)

    button = Button(frame, text="Admin", command=admin_login)
    button.grid(row=0, pady=20)

    button = Button(frame, text="Exit", command=tk.destroy)
    button.grid(row=1, pady=20)
    tk.mainloop()

    mainloop()


#main page for admin
def page1():
    def back_to_main2():
        admin_frame.grid_forget()
        global frame
        frame = Frame(tk, bg='Pink')
        frame.grid(padx=500, pady=250)

        button = Button(frame, text="Admin", command=admin_login)
        button.grid(row=0, pady=20)

        button = Button(frame, text="Exit", command=tk.destroy)
        button.grid(row=1, pady=20)
        tk.mainloop()

        mainloop()

    name=entry1.get()
    password=entry2.get()
    if len(name)!=0 and len(password)!=0:
        result=ib.check_admin(name,password)
        print(result)
        if result:
            admin_frame.grid_forget()

            global page1_frame
            page1_frame = Frame(tk, bg='Pink')
            page1_frame.grid(padx=500, pady=200)

            button10 = Button(page1_frame, text="Family", command=create_Family, width=20, height=2)
            button10.grid(row=0, pady=6)

            button13 = Button(page1_frame, text="Agent", command=create_Agent, width=20, height=2)
            button13.grid(row=1, pady=6)

            button8 = Button(page1_frame, text="Grocery", command=create_Grocery,width=20,height=2)
            button8.grid(row=2,pady=6)

            button19 = Button(page1_frame, text="Show All Agent", command=show_Agent, width=20, height=2)
            button19.grid(row=3, pady=6)

            button12 = Button(page1_frame, text="Back", command=back_to_main, width=20, height=2)
            button12.grid(row=5, pady=6)

            mainloop()
        else:
            label=Label(admin_frame,text="Invalid id and pasasword")
            label.grid(row=6,pady=10)
            button=Button(admin_frame,text='Exit',command=back_to_main2)
            button.grid(row=7)
            mainloop()
    else:
        label = Label(admin_frame, text="Please fill All Entries")
        label.grid(row=6, pady=10)
        button = Button(admin_frame, text='Exit', command=back_to_main2)
        button.grid(row=7)
        mainloop()


#creating window
global tk
tk=Tk()


tk.config(bg='Pink')
tk.title('Online Help Desk')
tk.minsize(1200,800)
tk.maxsize(1200,800)




global frame
frame=Frame(tk,bg='Pink')
frame.grid(padx=500,pady=250)


button=Button(frame,text="Admin",command=admin_login)
button.grid(row=0,pady=20)

button=Button(frame,text="Exit",command=tk.destroy)
button.grid(row=1,pady=20)
tk.mainloop()
