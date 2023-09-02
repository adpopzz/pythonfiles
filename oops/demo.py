class student:

    rolno:int
    name:str
    course:str
    def add_student(self,rol,name,course):
        self.rolno=rol
        self.name=name
        self.coursw=course
    
    def get_student(self):
        print(self.rolno,self.name,self.course)

stu1=student(123,"hari","b.com")


stu1.add_student(123,"hari","b.com")
stu1.get_student()