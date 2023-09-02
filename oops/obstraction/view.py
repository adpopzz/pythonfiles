from abc import ABC, abstractmethod
class createview(ABC):
    model=str
    template_name:str
    form_name=str

    def __init__(self,model,template_name,form_name):
        self.model=model
        self.template_name=template_name
        self.form_name=form_name
    @abstractmethod
    def create(self):
        pass

class employeecreate(createview):
    def __init__(self, model, template_name, form_name):
        super().__init__(model, template_name, form_name)

    def create(self):
        print("functionality for creating employee")

emp=employeecreate("empoyee","employee.html","empform")
emp.create()