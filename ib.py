import sqlite3


def connect_database():
    global conn
    global cur

    
    conn = sqlite3.connect("dbdb.db")
    
    cur = conn.cursor()

    
    cur.execute("create table if not exists Family (family_no int primary key, name text, age int, address text,family_member int,mobile_number int)")
    cur.execute("create table if not exists Grocery(item int primary key,name text, quantity text,adress text,amount int)")
    cur.execute("create table if not exists Agent (Name text,Mobile_no int,Address text,Report text)")
    cur.execute("create table if not exists admin (name text,pwd text)")
    cur.execute("insert into admin values('hack','123')")
    conn.commit()

#check admin dtails in database
def check_admin(name,password):

    cur.execute("select * from admin")
    data=cur.fetchall()

    if data[0][0]==name and data[0][1]==password:
        return True
    return

def create_Family(family_no,name,age,address,family_memeber,mobile_number):
    cur.execute("insert into Family values(?,?,?,?,?,?)",(family_no,name,age,address,family_memeber,mobile_number))
    conn.commit()

def create_Agent(Name,Mobile_no,Address,Report):
    cur.execute("insert into Agent values(?,?,?,?)",(Name,Mobile_no,Address,Report))
    conn.commit()

def create_Grocery(item,name,quantity,address,amount):
    cur.execute("insert into Grocery values(?,?,?,?,?)",(item,name,quantity,address,amount))
    conn.commit()

#show employees detail from staff table
def show_Agent():
    cur.execute("select Name,Report from Agent")
    detail=cur.fetchall()
    return detail




