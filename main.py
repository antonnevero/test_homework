import random

def main():
    population = []
    with open("USPopulation.txt", "r") as file:
        for p in file:
            population.append(int(p.rstrip()))
    average = (population[-1] - population[0]) / 40
    print(average)

    base_max = 0
    base_min = population[1] - population[0]
    year = 1950
    i = 0
    y = 0
    for p in range(1, len(population)):
        change = population[p] - population[p - 1]
        if change > base_max:
            base_max = change
            i = p
        elif change < base_min:
            base_min = change
            y = p
    print(year + i)
    print(year + y)




main()
