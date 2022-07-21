import random
import matplotlib.pyplot as plt
WEEKS = 52
def main():
    y_coor = []
    with open("text.txt") as file:
        for i in file:
            y_coor.append(float(i.strip()))
    x_coor = []
    for i in range(WEEKS):
        x_coor.append(i)
    plt.plot(x_coor, y_coor, marker='o')
    plt.title("Стоимость бензина за 1994 год")
    plt.xlabel("Недели")
    plt.ylabel("Стоимость")
    plt.grid(True)
    plt.show()




if __name__ == '__main__':
    main()
