'''
From a given string create a new string whith first and last characters exchanged.
'''


def changechars(string):

    return string[-1]+string[1:-1]+string[0]

def main():
    userinput=input("Enter a string: ")

    if len(userinput)<6:
        print("String must be atleast 6 characters.")
    else:
        print(changechars(userinput))


if __name__ == "__main__":
    main()