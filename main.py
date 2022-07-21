import random
import matplotlib.pyplot as plt

def main():
    expenses = []
    with open("text.txt") as file:
        for i in file:
            expenses.append(int(i.strip()))
    slices = ["Квартплата", "Бензин", "Еда", "Одежда", "Машина", "Разное"]
    plt.pie(expenses, labels=slices)
    plt.show()



if __name__ == '__main__':
    main()
