from get_connection import db_connect
class PetsView:

    def connect(self):
        db=db_connect(password="Password@123",database="animal")
        return db
    
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        quert="select * from pets"
        cursor.execute(quert)
        qs=cursor.fetchall()
        return qs
pv=PetsView()
print(pv.get())