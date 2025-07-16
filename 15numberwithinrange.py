'''
check if a given number falls within a given rangerange.
'''

def checknum(number,start,end):
    if number in range(start,end):
        return True
    else:
        return False

def main():
    number=input("Enter a number: ")
    start,end=input("Enter the starting and ending point of range: ").split()
    number=int(number)
    start=int(start)
    end=int(end)

    result=checknum(number,start,end)
    print(f'The given number falls within given range: {result}')

if __name__=="__main__":
    main()
