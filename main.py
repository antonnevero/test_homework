import random


def main():
    upper_case = 0
    lower_case = 0
    isdigit = 0
    isspace = 0
    with open('text.txt', "r") as file:
        file = file.readlines()
    for i in file:
        for j in i:
            if j.isupper():
                upper_case += 1
            if j.islower():
                lower_case += 1
            if j.isdigit():
                isdigit += 1
            if j.isspace():
                isspace += 1
    print(upper_case)
    print(lower_case)
    print(isdigit)
    print(isspace)




if __name__ == '__main__':
    main()
