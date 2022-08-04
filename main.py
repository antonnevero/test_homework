import random


def main():
    START = 1903
    FINISH = 2009
    dict1 = {}
    teams = []
    years = []
    team = ''
    with open("text.txt", 'r') as file:
        for i in file.readlines():
            teams.append(i.rstrip('\n'))

    for i in teams:
        score = 0
        for j in teams:
            if i == j:
                score += 1
        dict1[i] = score

    for i in range(START, FINISH+1):
        if i == 1904 or i == 1994:
            continue
        else:
            years.append(i)

    dict2 = dict(zip(years, teams))

    answer = int(input("Enter the year: "))
    for k, v in dict2.items():
        if answer == k:
            team = v
            print(f"In {answer} winner - {v}")
    for k,v in dict1.items():
        if team == k:
            print(f"Number of all win - {v}")



if __name__ == '__main__':
    main()
