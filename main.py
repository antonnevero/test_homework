import random

def main():
    winners = []
    with open("WorldSeriesWinners.txt", "r") as file:
        for i in file:
            winners.append(i.rstrip())
    count = 0
    team = input("Input team: ")
    for i in winners:
        if i == team:
            count += 1
    print(count)



main()
