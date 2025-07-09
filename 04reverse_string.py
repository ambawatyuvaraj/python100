'''
Take a string input from user and reverse it.
'''

'''
Notes:

'''

def revstring(userstring):
    userstring = userstring[::-1]
    print(userstring)


def main():
    userinput=input("Enter a string: ")
    revstring(userinput)

if __name__ == "__main__":
    main()