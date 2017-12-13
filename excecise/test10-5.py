file_name='guest.txt'

with open(file_name,"a") as file_object:

    while True:
        reason = input("why do you like coding? Or press 'q' for exit...\n")
        if reason!="q":
            file_object.write(reason+"\n")
        else:
            break