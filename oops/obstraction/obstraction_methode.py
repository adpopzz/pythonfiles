from abc import ABC,abstractmethod

class Ide(ABC):

    
    @abstractmethod
    def debug(self):
        pass


class pycharm(Ide):
    def debug(self):
        print("pycharm debug methode")

class eclipse(Ide):
    def debug(self):
        print(" eclipse debug ")

# pyc=pycharm()
# pyc.debug()

pyc=eclipse()
pyc.debug()

