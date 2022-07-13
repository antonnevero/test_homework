import random

def main():
    sum = []
    sum_7days = 0
    for day in range(7):
        sum.append(int(input(f"Type sales of day {day+1}: ")))

    for money in sum:
        sum_7days += money
    print(sum_7days)



main()
