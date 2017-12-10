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




class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        super().__init__(restaurant_name,cuisine_type,number_served)
        self.name=restaurant_name
        self.cuisine=cuisine_type
        self.number_served=number_served
        flavors=[]

    def describe_icecreamstand(self):
        print("the shop named "+self.name+" and it's "+self.cuisine+" and it served "+str(self.number_served)+" peoples.")

dq=IceCreamStand("DQ","opened",100)
dq.describe_icecreamstand()