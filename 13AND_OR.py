'''
Take two boolean values(true,yes,1,on - false,no,0,off) as input and return logical AND - OR of those values.
'''

def logicalvalues(a,b):
    andresult = a and b
    orresult = a or b

    return andresult,orresult
def stringtobool(value):
    if value in ("True","TRUE","true","yes","1","on"):
        return True
    elif value in ("False","FALSE","false","no","0","off"):
        return False
    else:
        return None

def main():
    a,b=input("Enter two values(a b): ").split()
    print(f'A: {a}, B: {b}')


    a=stringtobool(a)
    b=stringtobool(b)
    andresult,orreuslt=logicalvalues(a,b)

    print(f'AND RESULT: {andresult}, OR RESULT: {orreuslt}')

if __name__ =="__main__":
    main()