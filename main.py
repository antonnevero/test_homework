import random

def main():
    numbers = [1, 2, 5, 8, 10]
    num = 4
    bigger_that_n(numbers, num)

def bigger_that_n(list_of_numbers, n):
    for l in list_of_numbers:
        if l > n:
            print(l)




main()
