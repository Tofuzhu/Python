def print_name(filename):
    try:
        with open(filename) as file_object:
            lines=file_object.readlines()
            for line in lines:
                print('the pet name is '+line.strip())
    except FileNotFoundError:
        print('the file is not exist.')

print_name('cats.txt')
print_name('dogs.txt')