'''
Counting the number of letters and digits in a string.

'''


def counting(inputstring):
    letter_count = 0
    digit_count = 0
    for char in inputstring:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
    return letter_count,digit_count
#   print(f'Letter count:{letter_count},Digit Count:{digit_count}') 

def main():
    inputstring = input("Enter a mix of letters and numbers: ").strip()

    letter_count,digit_count=counting(inputstring)
    print(f'Letter Count:{letter_count},Digit Count:{digit_count}') 
if __name__ == "__main__":
    main()