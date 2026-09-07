import pymysql

connection=pymysql.connect(host="localhost",user="root",password="oneteam",database="collegedb")

cursor=connection.cursor()

department=input("enter the name : ")
cursor.execute(f"insert into department(dp_name)values('{department}')")
connection.commit()