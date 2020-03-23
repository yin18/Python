from D1W5 import *
class snake(Reptile):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.name=name
        self.age=age
    def seek_heat(self):
        return("Let me see some sunshine")
    def sleep(self):
        return("Please let me sleep")

sidney = snake("HOO",2)
print(sidney.seek_heat())
print(sidney.eat())

