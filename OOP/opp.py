# ------------ class
class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_descritpion():
        return "Car is means of transportation"
    
    @property
    def model(self):
        return self.__model
    
# new_car = Car("Toyota","Corolla")
# print(new_car.brand)
# print(new_car.model)
# print(new_car.fullname())

# new_car1 = Car("Tata","Safari")
# print(new_car1.brand)
# print(new_car1.model)
    
# -------- Start Inheritance

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"

teslaCar = ElectricCar("Tesla","Model S","85kwh")

# print(isinstance(teslaCar, Car))
# print(isinstance(teslaCar, ElectricCar))


#print(teslaCar.__brand)
#print(teslaCar.fuel_type())
#safari = Car("Tata","Safari")
#safari.model = "Mustaung"
#print(safari.model)

# print(safari.fuel_type())
# print(Car.total_car)
#print(teslaCar.brand)
#print(teslaCar.get_brand())

# StaticMethod
#print(Car.general_descritpion())
# -------- End Inheritance

#  Miltiple Inheritance
class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class NewElectriceCar(Battery,Engine,Car):
    pass

new_tesla_car = NewElectriceCar("Tesla","Model S")
print(new_tesla_car.battery_info())
print(new_tesla_car.engine_info())