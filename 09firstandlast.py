'''
Make a string using first and last two characters of a given bigger string.

'''


def customstring(string):
    firststring = string[0:2]
    laststring= string[-2:]
    combinedstring = firststring + laststring

    print(combinedstring)

def main():
    userinput=input("Enter your string: ")

    if len(userinput)<6:
        print("String must be atleast 6 characters.")
    else:
        customstring(userinput)
if __name__ == "__main__":
    main()