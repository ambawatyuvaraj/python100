'''
Count the occurences of a given word in a string.
'''


def countword(word,string):
    wordcount=string.count(word)
    return wordcount 

def main():
    inputstring=input("Enter a string: ")
    inputword=input("Enter the word to count: ")

    result=countword(inputword,inputstring)
    print(f'Total times the word {inputword} occurs is {result} times.')

if __name__ == "__main__":
    main()