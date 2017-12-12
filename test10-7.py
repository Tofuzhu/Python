while True:
    try:
        a=int(input('input num a:'))
        b=int(input('input num b:'))
    except ValueError:
        print('You entered a wrong type data')
    else:
        sum = a + b
        print(sum)