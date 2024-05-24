#basic class and object 
class Car:
    total_car = 0
    def __init__(self,brand , model ):
       self.__brand = brand #encapsulation
       self.__model = model
       Car.total_car += 1 

    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "petrol or diesel"
    @staticmethod
    def car_description():
        return "Cars are means of transport"
    @property
    def model(self):
        return self.__model

        
myCar = Car("Toyoto" , "corolla")
# print(myCar.brand)

my_new_car = Car("Tata" , "safari")
print(my_new_car.model)
# my_new_car.model = "sumo"
print(my_new_car.fullname())

#inheritance

class ElectricCar(Car):
    def __init__(self, __brand, __model ,batterySize):
        super().__init__(__brand , __model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("Tesla", "Model 5" , "85kwh")
print(my_tesla.model)
print(my_tesla.fullname())

#encapsulation
print(my_tesla.get_brand())

#polymorphism
print(my_new_car.fuel_type())
print(my_tesla.fuel_type())

#class variable
print(Car.total_car)

#static method
print(my_new_car.car_description()) #not accessiable
print(Car.car_description())

#Property decorator
print(my_new_car.model)

#isInstance
print(isinstance(my_tesla , Car))
print(isinstance(my_tesla , ElectricCar))

#multiple inheritance

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar2(Battery , Engine ,Car):
    pass

my_new_tesla = ElectricCar2("Tesla2" ,"model 5")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())