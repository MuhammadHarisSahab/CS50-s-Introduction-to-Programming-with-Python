from rich.console import Console
import requests

console = Console()

def main():
    console.print(
        "Welcome to the 'Not Get Bored' Program! 🎉\n"
        "Choose an option:\n"
        "1. Maths Facts Entertainer 📚\n"
        "2. Countries Capitals Teller 🌍\n"
        "3. Random Memes Generator 😂\n"
        "4. Useful Quotes Finder 💡\n",
        style='bold blue'
    )

    while True:
        choice = console.input('Enter your choice (1, 2, 3, 4, or 0 to exit): ').strip()
        
        if choice == '1':
            try:
                year = int(console.input('Enter a year: '))
                console.print(maths_facts(year))
            except ValueError:
                print('Please enter a valid year')
                pass
        elif choice == '2':
            country = console.input('Enter your country: ')
            console.print(capital(country))
        elif choice == '3':
            console.print(random_memes())
        elif choice == '4':
            console.print(useful_quotes())
        elif choice == '0':
            console.print("Goodbye! 👋", style='bold red')
            break
        else:
            console.print("Invalid option. Please select 1, 2, 3, 4, or 0.", style='bold red')

def maths_facts(year):
    response = requests.get(f'http://numbersapi.com/{year}/year?json')
    data = response.json()
    if 'text' in data:
        return data['text']
    return 'No facts found for this year.'

def capital(country):
    response = requests.get(f'https://restcountries.com/v3.1/name/{country}?fields=capital')
    try:  
        data = response.json()[0]
        return f"The capital of {country.capitalize()} is {data['capital'][0]}."
    except (KeyError, IndexError):
        return 'Invalid country name. Please try again.'

def random_memes():
    response = requests.get('https://api.kanye.rest/')
    data = response.json()
    return f"Random Meme: {data['quote']}"

def useful_quotes():
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()
    return f"A quote by {data[0]['a']}: {data[0]['q']}"

if __name__ == '__main__':
    main()