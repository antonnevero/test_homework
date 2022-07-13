import random

def main():
    lottery = []
    for money in range(7):
        lottery.append(random.randint(0, 9))
    for i in lottery:
        print(i)


main()
