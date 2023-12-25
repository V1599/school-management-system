from py_compile import main
import mysql.connector
con=mysql.connector.connect(host='localhost',username='root',password='vishu.159',database='school')


def AddSt(): 
    n=input("Student name: ")
    cl=input("Class: ")
    r=int(input("Roll no: "))
    a=input("Address: ")
    ph=input("Phone: ")
    data=(n,cl,r,a,ph)
    sql='insert into student values (%s,%s,%s,%s,%s)'
    with con.cursor() as cursor:
        cursor.execute(sql,data)
        con.commit()
    print("Data entered succesfully")
    print("")
def RemoveSt():
    cl=input("Class: ")
    r=int(input("Roll no: "))
    sql='delete from student where class=%s and rollno=%s'
    data=(cl,r)
    with con.cursor() as cursor:
            cursor.execute(sql, data)
            con.commit()
    print("Data Updated")
         
def DisplaySt():
    cl=input("Class: ")
    data=(cl,)
    sql='select * from student where class=%s'
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    
    for i in d: 
       Student_details={
           "Name": i[0],
            "Class": i[1],
            "Rollno": i[2],
            "Address": i[3],
            "Phone": i[4]
       }
       print(Student_details)
       print("")
       
    print("")
def AddT():
    # Take user input for each field
    tcode = int(input("TCode: "))
    n = input("Teacher name: ")
    s = int(input("Salary: "))
    a = input("Address: ")
    ph = input("Phone: ")

    try:
    # Prepare SQL query with placeholders
        sql = "INSERT INTO teacher VALUES (%s, %s, %s, %s, %s)"

    # Establish connection
        c=con.cursor()
        with con.cursor() as c:
            c.execute(sql, (tcode, n, s, a, ph))
            con.commit()

        print("Data entered successfully")
        print("")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
def RemoveT():

    n = input("Teacher: ")
    tcode = int(input("TCode: "))

    try:
        sql = "DELETE FROM teacher WHERE name = %s AND tcode = %s"
        data = (n, tcode)

        with con.cursor() as cursor:
            cursor.execute(sql, data)
            con.commit()

        print("Data Updated")

    except Exception as e:
        print(f"An error occurred: {e}")

     
def Updatesal():

    while True:
        n = input("Teacher: ")
        tcode = int(input("TCode: "))
        salary = int(input("Salary: "))
        data = (salary, n, tcode)

        try:
            sql = "UPDATE teacher SET salary = %s WHERE name = %s AND tcode = %s"
            with con.cursor() as c:
                c.execute(sql, data)
                con.commit()
            print("Data Updated")
            print("")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again")
            print("")
   
     
def DisplayT():
    sql='select * from teacher'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()

    for i in d:
        teacher_data = {
            "Tcode": i[0],
            "Name": i[1],
            "Salary": i[2],
            "Address": i[3],
            "Phone": i[4]
        }
        print(teacher_data)
        print("")

    print("")
    
    
    
def ClAttd():
    Cl=input("Class: ")
    clt=input("Class teacher: ")
    t=int(input("Class strenght: "))
    d=input("Date: ")
    ab=int(input("No of absentees: "))
    data=(Cl,clt,t,d,ab)
    sql='insert into clattendance values(%s,%s,%s,%s,%s)'
     
    with con.cursor() as cursor:
            cursor.execute(sql, data)
            con.commit()
    print("Data entered successfully")
    print("")
    
def Remove_ClAttd():

    cl = input("class: ")

    try:
        sql = "DELETE FROM clattendance WHERE class=%s"
        data = (cl)

        with con.cursor() as cursor:
            cursor.execute(sql, data)
            con.commit()

        print("Data Updated")

    except Exception as e:
        print(f"An error occurred: {e}")

    
def DisplayClAttd():
    sql='select * from clattendance'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    
    for i in d: 
        ClAttd_data = {
                "Class":i[0],
                "Class teacher":i[1],
                "Total St":i[2],
                "Date":i[3],
                "Absentees":i[4],
                }
    print(ClAttd_data)
    print("")
    
print("")
    
def TAttd():
    n=input("Name: ")
    d=input("Date: ")
    a=input("Attendance: ")
    data=(n,d,a)
    sql='insert into tattendance values(%s,%s,%s)'
    
    with con.cursor() as cursor:
            cursor.execute(sql, data)
            con.commit()
    print("Data entered successfully")
    print("")
    
def DisplayTAttd():
    sql='select * from tattendance'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    
    for i in d: 
      t_Attd = {
      "Name":i[0],
      "Date":i[1],
      "Attendance":i[2]}
      print(t_Attd)
    print("")
    
print("")
    
def add_fees():
    cl = int(input("class: "))
    q = int(input("Quarterly: "))
    b = int(input("BusFee: "))
    sc = int(input("ScFee: "))
    tc = int(input("TechFee: "))
    t = int(input("Total: "))
    
    data = (cl ,q , b, sc , tc, t)

    sql='INSERT INTO feestructure VALUES (%s, %s, %s, %s, %s, %s)'
    
    with con.cursor() as c:
            c.execute(sql,data)
            con.commit()

    print("Data entered successfully")
    print("")
    
def Updatefees():
    try:
        cl = (input("class: "))
        q= int(input("Quaterly: "))
        b = int(input("BusFee: "))
        sc = int(input("ScFee: "))
        tc = int(input("TechFee: "))
        t = int(input("Total: "))
        
        data = (cl,q, b, sc, tc, t)
        
        sql = '''
            UPDATE feestructure
            SET Quaterly=%s, BusFee=%s, ScFee=%s, TechFee=%s, Total=%s
            WHERE Class=%s
        '''
        
        with con.cursor() as c:
            c.execute(sql, data)
            con.commit()
        
        print("Data Updated")
        print("")
        
    except ValueError:
        print("Please enter numeric values for Quaterly, Bus Fee, Sc Fee, Tech Fee, and Total.")
        print("")
    
def DisplayFees():
    sql = 'select * from feestructure'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()

    for i in d:
        D_Fees = {
            "class": i[0],
            "Quaterly": i[1],
            "BusFee": i[2],
            "ScFee": i[3],
            "TechFee": i[4],
            "Total": i[5]
            } 
        print(D_Fees)
    print("")
    
    
if __name__=="__main__":
    ch='y'
    while ch in ['y','Y']:
        print("              St. Anselm's Senior Secondary School             ")
        print("1.Student")
        print("2.Teacher")
        print("3.ClAttendance")
        print("4.TAttendance")
        print("5.FeeStructure")
        table=int(input("Enter table no: "))
        print("")
        
        if table==1:
            op='y'
            while op in ['y','Y']:
                print("1.Add Student")
                print("2.Remove Student")
                print("3.Display Student details")
                task=int(input("Enter task no:"))
                if task==1:
                    AddSt()
                elif task==2:
                    RemoveSt()
                elif task==3:
                    DisplaySt()
                else:
                    print("Enter Valid Choice!!")
                op=input("Continue in this table(y/n):")
                
                
        elif table==2:
            op='y'
            while op in ['y','Y']:
                print("1.Add teacher")
                print("2.Remove teacher")
                print("3.Update Salary")
                print("4.Display teacher details")
                task=int(input("Enter task no:"))
                if task==1:
                    AddT()
                elif task==2:
                    RemoveT()
                elif task==3:
                    Updatesal()
                elif task==4:
                    DisplayT()
                else:
                    print("Enter Valid Choice!!")
                op=input("Continue in this table(y/n):")
        
        elif table==3:
            op='y'
            while op in ['y','Y']:
                print("1.Class Attendance")
                print("2.Remove Class Attendance")
                print("3.Display Class Attendance")
                task=int(input("Enter task no:"))
                if task==1:
                    ClAttd()
                elif task==2:
                    Remove_ClAttd()
                elif task==3:
                    DisplayClAttd()
                else:
                     print("Enter Valid Choice!!")
                op=input("Continue in this table(y/n):")
            
        elif table==4:
            op='y'
            while op in ['y','Y']:
                print("1.Teacher Attendance")
                print("2.Display TAttd details")
                task=int(input("Enter task no:"))
                if task==1:
                    TAttd()
                elif task==2:
                    DisplayTAttd()
                else:
                     print("Enter Valid Choice!!")
                op=input("Continue in this table(y/n):") 
                
        elif table==5:
            op='y'
            while op in ['y','Y']:
                print("1.Addfees")
                print("2.Update Fees")
                print("3.Display Fees details")
                task=int(input("Enter task no:"))
                if task==1:
                    add_fees()
                elif task==2:
                   Updatefees()
                elif task==3:
                    DisplayFees()
                else:
                     print("Enter Valid Choice!!")
                op=input("Continue in this table(y/n):")
        else:
            print("Enter Valid Choice!!!")
        ch=input("Do you want continue(y/n): ")
        pass
    
    if __name__=="__main__":
        main()
    
   
   