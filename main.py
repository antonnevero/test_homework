import random

def main():
    numbers = []
    with open("text.txt") as file:
        for c in file:
            numbers.append(c.strip("\n"))

    account_number = input("Enter number: ")
    if account_number in numbers:
        print("Ok")
    else:
        print("Not ok")




main()
