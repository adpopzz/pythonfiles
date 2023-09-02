import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
)

cusror=db.cursor()
# create a table buffalo
# id age weight breed image
query="""create table pets(id int auto_increment not null primary key,
        age int not null, 
        geneder varchar(200) not null,
        breed varchar(200) not null,
        location varchar(200) not null,
        price int not null  
         )"""

cusror.execute(query)