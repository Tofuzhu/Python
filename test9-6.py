class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.name=restaurant_name
        self.cuisine=cuisine_type
        self.number_served=number_served

    def describe_restaurant(self):
        print("This is a restaurant named "+self.name+".")
        print("It's "+self.cuisine+".")

    def open_restaurant(self):
        print("It's "+self.cuisine+".")

    def set_number_served(self):
        kfc.number_served=int(input("Please set the number of people served..."))

    def increment_number_served(self,increnum):
        kfc.number_served+=increnum

kfc=Restaurant("kfc","opened",11)
kfc.describe_restaurant()
kfc.open_restaurant()
print(kfc.number_served)

kfc.number_served=28
print(kfc.number_served)

kfc.set_number_served()
print("The number is "+str(kfc.number_served))

kfc.increment_number_served(99)
print("The number is "+str(kfc.number_served))
