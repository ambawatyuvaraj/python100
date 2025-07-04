'''
Find the numbers between a range that are divisible by a certain number and multiples of a certain number. 

'''

'''
Notes:

'''


def divmult(starting_num,ending_num,todivide,tomulti):
    for i in range(starting_num,ending_num + 1):
        if i % todivide == 0 and i % tomulti == 0:
            print(i)



def main():
    starting_number = input("Enter the starting number of range: ")
    ending_number = input("Enter the ending number of range: ")
    todivide = input("Enter the number with which the numbers in range should be divisible: ")
    tomulti = input("Enter the number with which the numbers in range should also multiply: ")

    divmult(int(starting_number),int(ending_number),int(todivide),int(tomulti))


if __name__ == "__main__":
    main()