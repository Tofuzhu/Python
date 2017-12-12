file_name='guest.txt'

with open(file_name,"a") as file_object:
    while True:
        guest_name=input("Please enter your name...")
        if guest_name!="q":
            file_object.write(guest_name+"\n")
        else:
            break