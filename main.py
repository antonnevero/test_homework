import random


def main():
    text1 = set()
    text2 = set()
    with open('text.txt', 'r') as file:
        for i in file.readlines():
            i = i.rstrip('\n')
            text1.add(i)

    with open('text2.txt', 'r') as file:
        for i in file.readlines():
            i = i.rstrip('\n')
            text2.add(i)
    print(text1.symmetric_difference(text2))
    print(text1 | text2)
    print(text1 - text2)
    print(text2 - text1)
    print(text2 & text1)



if __name__ == '__main__':
    main()
