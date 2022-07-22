import random


def main():
    numbers = input("Your numbers: ")
    list_num = []
    for i in numbers:
        list_num.append(int(i))
    count = 0
    for i in list_num:
        count += i
    print(count)



if __name__ == '__main__':
    main()
