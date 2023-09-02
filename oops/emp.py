class Employee:
    id:int
    name:str
    desig:str
    salary:str

    def set_emp(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def get_emp(self):
        print(self.name,self.id,self.desig,self.salary)

emp1=Employee()

emp1.set_emp(1000,"hari","hr",35000)
emp1.get_emp()