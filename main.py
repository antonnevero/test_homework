import random

def main():
    list_2d = [[0 for i in range(3)] for i in range(5)]

    for r in range(5):
        for c in range(3):
            list_2d[r][c] = int(input("Enter number: "))
    print(list_2d)



main()
