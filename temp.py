

def get_formatted_name(first,middle,last):
    full_name=first+' '+middle+' '+last
    return full_name.title()

if __name__=='__main__':
    print("Enter 'q' at any time to quit.")
    while True:
        first=input('\nPlease give me a first name:')
        if first=='q':
            break
        last=input("\nPlease give me a last name:")
        if last=='q':
            break

        formatted_name=get_formatted_name(first,last)
        print("\tNeatly formatted name: "+formatted_name+".")