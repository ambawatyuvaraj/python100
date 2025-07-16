'''
Multiply all the elements present in a list and return product.
'''

def multiplyelements(list):
    
    product=1
    for i in list:
        product *= i
    return product

def main():
    userinput=input("Enter a space separated list of elements: ").split()
    userinput=list(map(int,userinput))
    print(userinput)
    result=multiplyelements(userinput)
    print(f'Product of given list is: {result}')

if __name__=="__main__":
    main()