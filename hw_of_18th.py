class Bank:
    def __init__(self,balance):
        self.__balance=balance
    
    def set_balance(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    
b=Bank(99889)
print(b.get_balance())

class Calc:
    def mul(self,a,b,c=0):
        return a*b*c
m=Calc()
print(m.mul(3,4,5))
print(m.mul(4,5,6))


class Shape:
    def draw(self):
        print("drawid the shape ")
class Circle(Shape):
    def draw(self):
        print("draw a circle ")
c=Circle()
c.draw()

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self,house,rate_per_hour):
        self.house=house
        self.rate_per_hour=rate_per_hour

    def calculate_salary(self):
        return self.house * self.rate_per_hour
    
c=Manager(50,677)
print(c.calculate_salary())

