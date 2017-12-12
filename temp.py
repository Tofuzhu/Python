def count_words(file_name):
    try:
        with open(file_name) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        print("Sorry,the file is not exist.")
    else:
        words=contents.split()
        num_words=len(words)
        print('The file '+file_name+' has about '+str(num_words)+'words.')

file_name='alice.txt'
count_words(file_name)

