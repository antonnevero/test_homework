import random

def main():
    month = []
    for m in range(12):
        month.append(int(input(f"Month {m+1}:")))

    sum = 0
    for i in month:
        sum += i
    month_average = sum / 12
    maximum = month.index(max(month))
    minimum = month.index(min(month))

    print(month)
    print(sum)
    print(month_average)
    print(maximum, minimum)


main()
