class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=4000


    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you are a cheater!")

    def  increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battary():
    def __init__(self,battary_size=80):
        self.battary_size=battary_size


    def describe_battary(self):
        print("This car has a "+str(self.battary_size)+"kwh battary.")


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battary=Battary()

    def fill_gas_tank(self):
        print("This car dosen't need a gas tank!")


my_tesla=ElectricCar("tesla",'model s',2017)
print(my_tesla.get_descriptive_name()    )
my_tesla.battary.describe_battary()
my_tesla.fill_gas_tank()


my_byd=ElectricCar('byd','qin',2011)
print(my_byd.get_descriptive_name())



