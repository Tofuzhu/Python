import json

def input_num():
    a=input("Please enter your favorite number...")
    filename='username.json'
    with open(filename,"w") as ob:
        json.dump(a,ob)
    return filename


filename=input_num()
with open(filename) as ob:
    number=json.load(ob)
print("I know your favorite number is "+number)
