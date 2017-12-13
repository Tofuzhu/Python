from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        result=randint(1,self.sides)
        return result

a=Die()
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())
print(a.roll_die())


