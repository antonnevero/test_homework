import random


def main():
    dict = {}
    with open('text.txt', 'r') as file:
        for w in file.readlines():
            word = w.rstrip('\n')
            if word in dict:
                dict[word] = 2
            else:
                dict[word] = 1
    print(dict)


if __name__ == '__main__':
    main()
