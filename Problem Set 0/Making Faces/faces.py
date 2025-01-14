def convert(word):
    # Replace ":)" with "🙂" and ":(" with "🙁"
    word = word.replace(":)", "🙂")
    word = word.replace(":(", "🙁")
    return word

def main():
    # Prompt the user for input
    text = input("Enter your text: ")
    # Convert the text and print the result
    print(convert(text))

# Call main at the bottom of the file
main()
