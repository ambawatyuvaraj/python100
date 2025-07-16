'''
Find  factorial of any given number.
'''

def factorial(number):
    if number < 0:
       return None
    elif number == 0 or number ==1:
        return 1
    else:
        fact = 1
        for i in range(1, number+1):
            fact *= i                               # fact = fact * i 
        return fact
        
def recursivefactorial(number):
    if number < 0:                                      
        return None
    elif number == 0 or number ==1:                 # base cases 0 and 1
        return 1
    else:
    
        return number * recursivefactorial(number - 1)   #function calling itself eac time with a lower value 

def main():
    number=int(input("Enter a number: ").strip())

    print(f'Factorial of {number} is {factorial(number)}')
    print(f'Factorial of {number} using recursive approach is {recursivefactorial(number)}')

if __name__=="__main__":
    main()