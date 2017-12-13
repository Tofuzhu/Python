import json

filename='username.json'
try:
    with open(filename) as ob:
        favnum=json.load(ob)
except FileNotFoundError:
    with open(filename,'w') as ob:
        favnum=input('Enter a number...')
        json.dump(favnum,ob)
else:
    print('I know your favorite number is '+favnum)