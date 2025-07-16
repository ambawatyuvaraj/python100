'''
Count the number of upper and lower case characters in a given string.
'''

def countingchars(string):
    uppercase=0
    lowercase=0
    for char in string:
        if char.islower():
            lowercase+=1
        elif char.isupper():
            uppercase+=1

    return uppercase,lowercase

def main():
    userinput=input("Enter a string: ").strip()

    uppercount,lowercount=countingchars(userinput)
    print(f'Lower chars count: {lowercount}, Upper chars count: {uppercount}')

if __name__=="__main__":
    main()