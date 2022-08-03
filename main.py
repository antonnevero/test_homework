import random


def main():
    word_set = set()
    with open('text.txt', 'r') as file:
        for w in file.readlines():
            word_set.add(w.rstrip('\n'))

    for i in word_set:
        print(i)


if __name__ == '__main__':
    main()
