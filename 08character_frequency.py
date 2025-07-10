'''
count a character frequency in a given string.

'''

def countfreq(string):
    frequency={}
    for char in string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency

def main():
    userinput=input("Enter a string: ").strip()

    frequency=countfreq(userinput)
    for char,count in frequency.items():
     print(f'Char: {char}, Count: {count}')

if __name__ == "__main__":
    main()