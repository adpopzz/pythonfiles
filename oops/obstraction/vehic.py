from abc import ABC,abstractmethod
class bike(ABC):
    name=str
    model=str
    fuel_type=str
    def __init__(self,name,model,fuel_type):

        self.name=name
        self.model=model
        self.fuel_type=fuel_type
    @abstractmethod
    def start(self):
        pass

class hunter(bike):
    def __init__(self, name, model, fuel_type):
        super().__init__(name, model, fuel_type)
    def start(self):
        print(f"{self.name}starting model:- {self.model} fuel:- {self.fuel_type}")

hun=hunter("hunter dapper grey","2023 ","petrol")
hun.start()

class ather(bike):
    def __init__(self, name, model, fuel_type):
        super().__init__(name, model, fuel_type)
    def start(self):
        print(f"{self.model} starting model:- {2022} fuel:- {self.fuel_type}")