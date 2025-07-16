'''
Check if a string is palindrome.
'''

def checkbool(string):
    if len(string) < 6 or string == "":
        print("String must be 6 characters atleast.")
    elif string == string[::-1]:
        print("String is a boolean.")
    else:
        print("String is not boolean.")

def main():
    userinput = input("Enter a string: ")

    checkbool(userinput)

if __name__ == "__main__":
    main()