'''
Print this pattern:

*
**
***
****
*****
****
***
**
*

'''

'''
Notes: 
    1. we'll need  for loops (first half and second half of the pattern)
    2. first loop starting from 1 to n+1 (because in range ending number isn't included so we do +1 )  range (start , end+1 )
    3. another one from n-1 to 0 decreasing every step => range (start , stop , step)
    4. that's all we need to print this pattern 
    
'''


def pattern(n):
    for i in range(1,n+1):
        print("* " * i)
    for i in range(n-1,0,-1):
       print("* "*i)


def main():
 n=int(input("Enter thhe value of n: "))
 pattern(n)



if __name__ == "__main__":
    main()

