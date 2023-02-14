from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector as connector

window = tk.Tk()
window.geometry("1000x900")
window.title("STUDENT DATABASE FORM")
# ______________________________________________________make_connection__________________________________________
global con
con = connector.connect(host='localhost', port='3306', user='root', password='*******')
print("connection made")
# _____________________________________________________________create_database___________________________________

dbname_var = StringVar()

def savee():
    name = dbname_var.get()
    query = "CREATE DATABASE " + str(name)
    print(query)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    print(dbname_var, 'Database created')
    cur.execute('show databases')
    for x in cur:
        print(x)

createDatabase_label = Label(window, text=('Enter the Database name to create').upper(), font=('calibre', 8, 'bold'),
                             fg="#BC7407")
Database_entry = Entry(window, textvariable=dbname_var, font=('calibre', 10, 'normal'))
submit_btn = Button(window, text='submit', command=savee)

createDatabase_label.place(x=10, y=10)
Database_entry.place(x=10, y=40)
submit_btn.place(x=10, y=70)

# _______________________________________________use_data______________________________________________________

db_name1 = StringVar()

def dataa():
    name1 = db_name1.get()
    global query1
    query1 = 'use ' + str(name1)
    print(query1)
    cur = con.cursor()
    cur.execute(query1)
    con.commit()
    print("we are using", name1, "database")

usedatabase_label = Label(window, text=('Enter the Database name to use').upper(), font=('calibre', 8, 'bold'),
                          fg="#BC7407")
Database_entry = Entry(window, textvariable=db_name1, font=('calibre', 10, 'normal'))
submit_btn = Button(window, text='submit', command=dataa)

usedatabase_label.place(x=10, y=120)
Database_entry.place(x=10, y=150)
submit_btn.place(x=10, y=180)

# __________________________________________________create_table__________________________________________________

tablenamee_var = StringVar()
column1 = StringVar()
column5 = StringVar()
column3 = StringVar()
column4 = StringVar()

def ctable():
    tname = tablenamee_var.get()
    column_1 = column1.get()
    column_2 = column5.get()
    column_3 = column3.get()
    column_4 = column4.get()

    query = "CREATE TABLE IF NOT EXISTS " + str(tname) + "({} integer,{} varchar(50),{} varchar(50),{} integer)" \
        .format(column_1, column_2, column_3, column_4)

    print(query)
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query)
    con.commit()
    print(tname, "table is created")

createTable_label = Label(window, text=('Enter the table name to create').upper(), font=('calibre', 8, 'bold'),
                          fg="#BC7407")
createTable_entry = Entry(window, textvariable=tablenamee_var, font=('calibre', 10, 'normal'))
submit_btn = Button(window, text='submit', command=ctable)

createTable_label.place(x=250, y=10)
createTable_entry.place(x=250, y=40)

name_label = Label(window, text='Enter the column names', font=('calibre', 8, 'bold')).place(x=250, y=70)

column1_label = Label(window, text='column1', font=('calibre', 7)).place(x=250, y=100)
column1_entry = Entry(window, textvariable=column1, font=('calibre', 10, 'normal')).place(x=250, y=130)

column2_label = Label(window, text='column2', font=('calibre', 7, 'bold')).place(x=250, y=160)
column2_entry = Entry(window, textvariable=column5, font=('calibre', 10, 'normal')).place(x=250, y=190)

column3_label = Label(window, text='column3', font=('calibre', 7, 'bold')).place(x=250, y=220)
column3_entry = Entry(window, textvariable=column3, font=('calibre', 10, 'normal')).place(x=250, y=250)

column4_label = Label(window, text='column4', font=('calibre', 7, 'bold')).place(x=250, y=280)
column4_entry = Entry(window, textvariable=column4, font=('calibre', 10, 'normal')).place(x=250, y=310)

submit_btn.place(x=250, y=340)

# _____________________________________________________insert___________________________________________________

table_name = StringVar()
name_var = StringVar()
id_var = StringVar()
rollno_var = StringVar()
class_var = StringVar()

choice_var1 = StringVar()

def insertt():
    #tnamee = choice_var.get()

    tname = table_name.get()
    Id = id_var.get()
    name = name_var.get()
    class1 = class_var.get()
    rollno = rollno_var.get()
    # class1 = class_var.get()

    query = "INSERT INTO {}(ID,NAME,CLASS,ROLLNO) values({},'{}','{}',{})" \
        .format(tname, Id, name, class1, rollno)
    print(query)
    #query2 = "SELECT * from " + str(tnamee)
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query)
    #cur.execute(query2)
    con.commit()
    print("data inserted into table")
    #label1=Label(window,text)


createTable_label = Label(window, text=('Enter the table name to insert').upper(), font=('calibre', 8, 'bold'),
                          fg="#BC7407").place(x=490, y=10)
createTable_entry = Entry(window, textvariable=table_name, font=('calibre', 10, 'normal')).place(x=490, y=40)
insert_label = Label(window, text='Enter the data to insert', font=('calibre', 8), fg='#4A7A8C').place(x=490, y=60)
namee_label = Label(window, text='Student Id', font=('calibre', 7)).place(x=490, y=80)
name_entry = Entry(window, textvariable=id_var, font=('calibre', 7, 'normal')).place(x=490, y=100)
id_label = Label(window, text='Student name', font=('calibre', 7,)).place(x=490, y=120)
id_entry = Entry(window, textvariable=name_var, font=('calibre', 7, 'normal')).place(x=490, y=140)
rollno_label = Label(window, text='class', font=('calibre', 7,)).place(x=490, y=160)
rollno_entry = Entry(window, textvariable=class_var, font=('calibre', 7, 'normal')).place(x=490, y=180)
class_label = Label(window, text='rollno', font=('calibre', 7,)).place(x=490, y=200)
class_entry = Entry(window, textvariable=rollno_var, font=('calibre', 7, 'normal')).place(x=490, y=220)
submit_btn = Button(window, text='submit', command=insertt).place(x=490, y=240)

# _____________________________________________________select__________________________________________________
choice_var = StringVar()
def selectt():
    tnamee = choice_var.get()
    query = "SELECT * from " + str(tnamee)
    print(query)
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query)
    print("selected everything from ", tnamee)
    i = 40
    labelh=Label(window,text="STUDENT INFO",font=("calibre",10,"bold")).place(x=800,y=20)
    for rows in cur:
        print(rows)
        label1=Label(window, text=rows).place(x=800, y=i)
        i=i+20

selectTable_label = Label(window, text=('Enter TABLE name to select all data').upper(), font=('calibre', 8, 'bold'),
                          fg="#BC7407")
selectTable_entry = Entry(window, textvariable=choice_var, font=('calibre', 10, 'normal'))

submit_btnnn = Button(window, text='submit', command=selectt).place(x=490, y=360)

selectTable_label.place(x=490, y=300)
selectTable_entry.place(x=490, y=330)
# submit_btmmn.place(x=490, y=360)

# __________________________________________________UPDATE_DATA_____________________________________________
tablename = StringVar()
columnn1 = StringVar()
valuee1 = StringVar()
where_col = StringVar()
where_val = StringVar()


def update_data():
    ttname = tablename.get()
    columnn11 = columnn1.get()
    value11 = valuee1.get()
    wcol = where_col.get()
    wval = where_val.get()

    query = "UPDATE {} SET {}='{}' WHERE {}={} ".format(ttname, columnn11,value11, wcol, wval)
    print(query)
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query)
    print("Data updated succesfully")


updatetable_label = Label(window, text=('Enter TABLE name to update').upper(), font=('calibre', 8, 'bold'),
                          fg="#BC7407"). \
    place(x=10, y=220)
updatetablename_entry = Entry(window, textvariable=tablename, font=('calibre', 10, 'normal')).place(x=10, y=250)
updatetable1_label = Label(window, text='column name', font=('calibre', 7)). \
    place(x=10, y=280)
updatecolumn_entry = Entry(window, textvariable=columnn1, font=('calibre', 10, 'normal')).place(x=10, y=310)
updatetable2_label = Label(window, text='value name', font=('calibre', 7)). \
    place(x=10, y=340)
updatevalue_entry = Entry(window, textvariable=valuee1, font=('calibre', 10, 'normal')).place(x=10, y=370)
updatetable3_label = Label(window, text='Where column', font=('calibre', 7)). \
    place(x=10, y=400)
updateWcol_entry = Entry(window, textvariable=where_col, font=('calibre', 10, 'normal')).place(x=10, y=430)
updatetable4_label = Label(window, text='Where value', font=('calibre', 7)). \
    place(x=10, y=460)
updateWval_entry = Entry(window, textvariable=where_val, font=('calibre', 10, 'normal')).place(x=10, y=490)

submit_btnn = Button(window, text='submit', command=update_data).place(x=10, y=520)
# __________________________________________________Delete_data__________________________________________________
tablee_name = StringVar()
column11 = StringVar()
condition1 = StringVar()
wh_value = StringVar()

def delete_data():
    tname = tablee_name.get()
    column = column11.get()
    condition = condition1.get()
    value = wh_value.get()

    query = "DELETE FROM {} WHERE {}{}{} ".format(tname, column, condition, value)
    print(query)
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query)
    print("Data deleted succesfully")


deletedata_label = Label(window, text=('Enter TABLE name to delete data').upper(), font=('calibre', 8, 'bold'),
                         fg="#BC7407"). \
    place(x=490, y=400)
delete_dataname_entry = Entry(window, textvariable=tablee_name, font=('calibre', 10, 'normal')).place(x=490, y=430)
deletetable1_label = Label(window, text='column name', font=('calibre', 7)). \
    place(x=490, y=460)
deletecolumn_entry = Entry(window, textvariable=column11, font=('calibre', 10, 'normal')).place(x=490, y=490)
deletetable2_label = Label(window, text='Condion(< > =)', font=('calibre', 7)). \
    place(x=490, y=520)
deletevalue_entry = Entry(window, textvariable=condition1, font=('calibre', 10, 'normal')).place(x=490, y=550)
deletetable3_label = Label(window, text='Where value', font=('calibre', 7)). \
    place(x=490, y=580)
deleteWval_entry = Entry(window, textvariable=wh_value, font=('calibre', 10, 'normal')).place(x=490, y=610)

submit_btnmn = Button(window, text='submit', command=delete_data).place(x=490, y=640)
labell1=Label(window,text="Developed by sandeep",font=("calibre",7,"bold")).place(x=700,y=660)

window.mainloop()
