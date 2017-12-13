file_name='learning_python.txt'

with open(file_name) as file_object:
    lines=file_object.readlines()

string=""
for line in lines:
    line=line.replace("python","c")
    print(line.strip())
    string+=line.strip()+"   "

print(string)