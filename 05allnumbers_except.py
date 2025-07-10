'''
Print all numbers between a given range except any two numbers that you dont want.
'''

'''
Notes: 


'''

def allnumbers(start,end,firstexception,secondexception):
    for i in range(start,end+1):
        if i == firstexception or i==secondexception:
            continue
        else:
            print(i)


def main():
    start,end = input("Enter the start and end of range: ").split()
    print(f'Start:{start},End:{end}')

    firstexception,secondexception=input("Enter two exceptions to exclude from list: ").split()
    print(f"First Exclusion:{firstexception},Second Exclusion:{secondexception}")

    allnumbers(int(start),int(end),int(firstexception),int(secondexception))

if __name__ == "__main__":
    main()
        
