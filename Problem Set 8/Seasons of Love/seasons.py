import re
import sys
import inflect
from datetime import date, timedelta

eng = inflect.engine()

def main():
    birth = date_of_birth(input(("What's your date of birth? ")))
    mins = get_mins(birth)
    print(get_in_words(mins))

...
def date_of_birth(birth_date):
    if match:= re.search('^[0-9]{4}-[0-9]{2}-[0-9]{2}$' , birth_date):
        return birth_date
    else:
        sys.exit('Invalid type')

def get_mins(birth_date):
    years, months, days = birth_date.split('-')
    years, months, days = int(years), int(months), int(days)

    birth_date = date(years, months, days)
    current_date = date.today()
    difference = current_date - birth_date
    days = difference.days
    mins = int(days) * 24 * 60
    return mins

def get_in_words(mins):
    x = eng.number_to_words(mins, andword= '')
    x = x.capitalize()
    final = f'{x} minutes'
    return final


if __name__ == "__main__":
    main()