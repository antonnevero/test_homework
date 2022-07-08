import random
JANUARY, MARCH, MAY, JULY, AUGUST, OCTOBER, DECEMBER = 31
FEBRUARY = 28
APRIL, JUNE, SEPTEMBER, NOVEMBER = 30

def main():
    with open("text.txt", "r") as file:
        step = 0
        days = 1
        while days <= 365:
            step += int(file.readline())
            days += 1
        print(step / 12)

main()
