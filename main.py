import sqlite3

db = sqlite3.connect("ContactInformation")

cr = db.cursor()

cr.execute("""CREATE TABLE IF NOT EXISTS Contact_Information(id INTEGER PRIMARY KEY,Name TEXT,Surname TEXT,
Address TEXT,Phone INTEGER,Email TEXT,Age,Salary)""")


def add_Contact():
    id = input("please enter id:")
    name = input("Please Enter Name:")
    surname = input("Please Enter Surname:")
    adress = input("Please Enter Address:")
    phone = input("Please Enter Phone:")
    email = input("Please Enter e-mail:")
    age = input("Please Enter Age:")
    salary = input("Please Enter Salary")
    cr.execute("""INSERT INTO Contact_Information VALUES (?,?,?,?,?,?,?,?)""",
               [id, name, surname, adress, phone, email, age, salary])
    db.commit()


def delete_Contact():
    id = input("Please enter id to delete it")
    cr.execute("""DELETE FROM Contact_Information Where id=?""", [id])
    db.commit()


def update_Contact():
    id = input("Please enter id to update")
    update = input("What do you want to change? (name,surname,email,adress,phone,salary,age)")
    new = input("Please enter new {} ".format(update))
    cr.execute("UPDATE Contact_Information SET {} =? WHERE id=?".format(update), [new, id])
    db.commit()


def show():
    print("All Database\n")
    sort = input("1.ASC\n"
                 "2.DESC\n")
    if sort == "1":
        cr.execute("SELECT * FROM Contact_Information ORDER BY id ASC")
    elif sort == "2":
        cr.execute("SELECT * FROM Contact_Information ORDER BY id DESC")
    veriler = cr.fetchall()
    for i in veriler:
        print(i)


def find():
    search = input("What do you want search ?")
    find_per = input("Please enter {} to find persons".format(search))
    cr.execute("""SELECT * FROM Contact_Information WHERE {}=?""".format(search), [find_per])
    veriler2 = cr.fetchall()
    print("Person list has {}={} ".format(search, find_per))
    for i in veriler2:
        print(i)


def list():
    gir = input("Enter parameter to list for: (name,surname,email,phone,address,salary,age)")
    cr.execute("SELECT {} FROM Contact_Information".format(gir))
    veriler = cr.fetchall()

    for i in veriler:
        print(i)


def add_Column():
    cursor = db.execute("select * from Contact_Information")
    colNames = cursor.description
    dizi = []
    for i in colNames:
        dizi.append(i[0])

    column_name = input("Please enter information name:")

    cr.execute("SELECT * FROM Contact_Information")
    row_count = cr.fetchall()

    if column_name in dizi:
        print("{} Column is already exist".format(column_name))
    else:
        cr.execute("ALTER TABLE Contact_Information ADD {} integer".format(column_name))
        for i in range(1, len(row_count) + 1):
            age = input("Please enter {} Person {}:".format(i, column_name))

            cr.execute("UPDATE Contact_Information SET {}=(?) WHERE id={}".format(column_name, i), [age])
        db.commit()


def drop_column():
    cr.execute("""CREATE TABLE IF NOT EXISTS Contact_Information1  (id INTEGER PRIMARY KEY,Name TEXT,Surname TEXT,
Address TEXT,Phone INTEGER,Email TEXT,Age INTEGER )""")
    cr.execute("""INSERT INTO Contact_Information1 SELECT id,Name,Surname,Address,Phone,Email,Age FROM 
    Contact_Information """)
    cr.execute("""DROP TABLE Contact_Information""")
    cr.execute("""ALTER TABLE Contact_Information1 RENAME TO Contact_Information""")

    db.commit()


def delete_database():
    cr.execute("DROP TABLE Contact_Information")


def getColumn():
    a = cr.execute("SELECT sql FROM sqlite_master WHERE tbl_name='table_name' AND type='table' ")


while True:
    print("-" * 100)
    print("1.Add \n"
          "2.Delete\n"
          "3.Update\n"
          "4.Find\n"
          "5.Show All Database\n"
          "6.List\n"
          "7.Add New Information\n"
          "8.Delete Column\n"
          "9.Delete All Information\n"
          "10.Quit\n"
          )
    print("-" * 100)
    enter = input(">>> (Enter number from menu)")

    if enter == "1":
        add_Contact()
    elif enter == "2":
        delete_Contact()
    elif enter == "3":
        update_Contact()
    elif enter == "4":
        find()
    elif enter == "5":
        show()
    elif enter == "6":
        list()
    elif enter == "7":
        add_Column()
    elif enter == "8":
        drop_column()
    elif enter == "9":
        delete_database()
    elif enter == '10':
        break
