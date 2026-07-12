# class Stdent:
#     def __init__(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name=name
    
# s=Stdent('shiva')
# print(f"name:{s.get_name()}"

#super()

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         print(f"{self.name} make sound")

# class Dog(Animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed=breed

#     def sound(self):
#         super().sound()
#         print(f"{self.name} barking")

# dog=Dog("deva","labratri")
# dog.sound()

from abc import ABC,abstractmethod
class Vechile(ABC):
    @abstractmethod
    def start_engin(self):
        pass
class Bick(Vechile):
    def __init__(self,name):
        self.name=name
    def start_engin(self):
        print(f"{self.name} is started ")
b=Bick("yamaha")
b.start_engin()