import random
JANUARY, MARCH, MAY, JULY, AUGUST, OCTOBER, DECEMBER = 31
FEBRUARY = 28
APRIL, JUNE, SEPTEMBER, NOVEMBER = 30

def main():
    with open("text.txt", "r") as file:
        step = 0
        for i in file:
            step += i
        calculate(step, )

def calculate(steps, month):
    return steps / month
main()
