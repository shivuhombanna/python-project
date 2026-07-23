# class Employee:
#     def __init__(self,name,designation,salary=30000):
#         self.name=name
#         self.designation=designation
#         self.salary=salary
#     def emp_info(self):
#         print(f"the name is {self.name},\n designation is {self.designation} \n salary is    {self.salary}")

# shivu=Employee("shivaraj","HR","1.5L")
# geetha=Employee("geetha","maneger") 

# shivu.emp_info()
# geetha.emp_info()


#encapsulaion and abstraction 

# class Database:
#     def __init__(self):
#         self.__database={} #private
#     def writr(self,key,value):
#         self.__database[key,value]=value #nange key kotre valu na thorisu 
#     def read(self,key):
#         if key in self.__database:
#             print(self.__database[key])
#         else:
#             print("not availebel et")
# db=Database()
# db.writr("shivu","hobanna")
# db.read("hobanna")


# hw bro idu 
class Bankaccount:
    def __init__(self,accno,balence):
        self.__accno=accno
        self.__balence=balence
    
    def checkbal(self):
        print(f"the totl balence is {self.__balence}  ")
        
    def deposit(self,amount):
        if amount>0:
            self.__balence+=amount
            print(f"{amount},success fully add!")
        else:
            print("inavlid ")
    def withdra(self,amount):
        if amount<=0:
            print("you have no moany in your account")
        elif amount > self.__balence:
            print("in safishiant balance ")
        else:
            self.__balence-=amount
            print(f"{amount} success fully with Drawa !!")


s=Bankaccount("1009",100)

s.deposit(9000)
s.checkbal()

s.withdra(100)
s.checkbal()

        
