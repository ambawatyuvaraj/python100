'''
sum of all elements in a list.
'''

userinput=input("Enter a list of elements(separated by space): ")
userinput=list(map(int,userinput.split()))     # applies the int function to each item in the list returned by split()
print(f'Values in list: {userinput}')

result=sum(userinput)
print(f'Sum of values in list: {result}')