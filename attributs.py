class Cars:
    def __init__(self,brand,module):
        self.brand=brand
        self.module=module
    def cars_info(self):
        print(f"car brand name ={self.brand},car model name is {self.module}")
bmw=Cars("BMW","M4 CS compitaion ")
bmw.cars_info()
toyota=Cars("forchunar","4*4 drive")
toyota.cars_info()
