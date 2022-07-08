import random

def main():
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    names_of_months = ["january", "february", "march", "may", "june", "july", "august", "september", "october",
                       "november", "december"]
    with open("text.txt", "r") as file:
        num_of_month = 1
        for i in month:
            days = 1
            step = 0
            while days <= i:
                step += int(file.readline())
                days += 1
            print(f"Month {names_of_months[num_of_month-1]}: {round(step / i)}")
            num_of_month += 1

main()
