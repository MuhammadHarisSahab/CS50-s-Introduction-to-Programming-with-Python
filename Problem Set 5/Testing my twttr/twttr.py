def main():
    lol = str(input('Enter you text: '))
    print(shorten(lol))

def shorten(word):
    
    vowels = ['a', 'e', 'i', 'o' ,'u']
    result = ''  # Initialize an empty string to store the result
    for i in word:
        if i.lower() not in vowels:  # Check if the character is not a vowel
            result += i  # Add non-vowel characters to the result
    return result 

if __name__ == "__main__":
    main()