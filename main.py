import random


def main():
    right = 0
    wrong = 0
    next = 0
    dict = {
        'Ukraine': "Kyiv",
        'USA': "Washington",
        'Australia': 'Canberra',
        'Portugal': 'Lisbon',
        'England': 'London'
    }
    while next < 5:
        country, capital = dict.popitem()
        answer = input(f"What is the capital of {country}: ").title()
        if answer == capital:
            print('Right!')
            right += 1
        else:
            print("Wrong!")
            wrong += 1
        next += 1
        print(next)

    print(f"Right answers - {right}, wrong answers - {wrong}")


if __name__ == '__main__':
    main()
