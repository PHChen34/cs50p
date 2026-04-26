from datetime import date
import sys
import inflect
import re

class Date:
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)



    def __str__(self):
        return ("f{self._year}-{self._month}-{self._day}")



def main():
    birthdate = input("Date of Birth: ")
    validate(birthdate)
    years, months, dates = birthdate.split("-")
    d = Date(years, months, dates)
    print(calcu(d))



def validate(date):
    if not re.search(r"^([0-9]{4})-((0[1-9])|(1[0-2]))-((0[1-9])|(1[0-9])|(2[0-9])|(3[01]))$", date):
        sys.exit("Invalid date")

def calcu(live):
    c = inflect.engine()

    birth_date = date(live.year, live.month, live.day)
    current_date = date.today()
    difference = current_date - birth_date
    minutes = difference.days *24*60

    ans = c.number_to_words(minutes, andword="")
    return (f"{ans.capitalize()} minutes")



if __name__ == "__main__":
    main()
