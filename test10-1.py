file_name='learning_python.txt'

with open(file_name) as file_object:
    lines=file_object.readlines()

string=""
for line in lines:
    print(line.strip())
    string+=line.strip()+"   "

print(string)
