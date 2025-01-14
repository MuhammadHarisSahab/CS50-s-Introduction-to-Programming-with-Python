# Define valid characters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Combine all checks
    return (
        letters_check(s) and
        numbers_check(s) and
        punctuation_check(s) and
        characters_amount_check(s)
    )

def numbers_check(n):
    number_started = False
    for char in n:  # Loop  through each character
        if char in numbers:  # If the character is a number
            if not number_started:  # If this is the first number
                if char == '0':  # Check if the first number is '0'
                    return False  # Invalid if the first number is '0'
            number_started = True  # Mark that numbers have started
        elif char in letters and number_started:
            return False  # Invalid if a letter appears after numbers
    return True


def letters_check(s):
    # Ensure the first two characters are letters
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()

def characters_amount_check(c):
    # Ensure the length is between 2 and 6
    return 2 <= len(c) <= 6

def punctuation_check(n):
    # Ensure all characters are valid
    for i in n:
        if i not in letters and i not in numbers:
            return False
    return True

main()
