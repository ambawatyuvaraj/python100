'''
Find the second largest number in a given list.
'''


def findingnumber(list):
    


def main():
    userinput=input("Enter a list of elements(space separated): ").split()
    userinput=list(map(int,userinput))
    print(f'List: {userinput}')

    result=findingnumber(userinput)
    print(f'The second largest number is: {result}')

if __name__ == "__main__":
    main()