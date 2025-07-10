'''
check if a triangle is equilateral,isoceles or scalene.

'''

def checktraingle(side1,side2,side3):
    if side1 == side2 == side3:
        print("Triangle is Equilateral.")
    elif side1 == side2 or side2 ==side3 or side3 == side1:
        print("Triangle is isoceles.")
    elif side1 != side2 != side3:
        print("Triangle is scalene.")


def main():
  
    side1,side2,side3=input("Enter the three sides of triangle:").split()
    print(f'Side1:{side1},Side2:{side2},Side3:{side3}')
    side1=int(side1)
    side2=int(side2)
    side3=int(side3)

    if side1+side2 > side3 and side3 +side2 > side1 and side1+side3>side2:
     checktraingle(side1,side2,side3)
    else:
        print("Three sides entered violate the Triangle Inequality Theorem.")


if __name__ == "__main__":
    main()