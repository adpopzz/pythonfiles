import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
    
)


cursor=db.cursor()
query="""insert into pets(age,geneder,breed,location,price)values(3,'female','breed3','palakkad',25000)
    
"""
cursor.execute(query)
db.commit() #SAVE CHANGES
