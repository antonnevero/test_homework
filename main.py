import random


def main():
    name = input("YOur name: ")
    answer = name.split(' ')
    for i in answer:
        print(i[0].upper(), end='')
        print('.', end='')



if __name__ == '__main__':
    main()
