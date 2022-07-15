import random

def main():
    boys = []
    girls = []
    with open("BoyNames.txt") as file:
        for n in file:
            boys.append(n.rstrip())
    with open("GirlNames.txt") as file:
        for n in file:
            girls.append(n.rstrip())
    answer = input("Do you want to check Boy, Girl or Both names? B, G, BOTH: ").upper()
    if answer == "B":
        boy_name = input("Write boys name: ")
        if boy_name in boys:
            print(f"{boy_name} is in the list")
    elif answer == "G":
        girl_name = input("Write girls name: ")
        if girl_name in girls:
            print(f"{girl_name} is in the list")
    elif answer == "BOTH":
        boy_name = input("Write boys name: ")
        girl_name = input("Write girls name: ")
        if boy_name in boys:
            print(f"{boy_name} is in the list")
        if girl_name in girls:
            print(f"{girl_name} is in the list")



main()
