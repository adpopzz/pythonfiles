from abc import ABC ,abstractmethod
class employee(ABC):
    name:str
    salary:str

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @abstractmethod
    def calculate_salray(self):
        pass

class manager(employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_salray(self):
        return self.salary+25000

class developer(employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_salray(self):
        return self.salary+10000
    
devp=developer(name="hari",salary=2500)
print(devp.calculate_salray())
