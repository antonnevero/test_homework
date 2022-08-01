import random


def main():
    answer = input("Enter the sentence: ")
    result = answer[0]

    for i in range(1, len(answer)):
        ch = answer[i]

        if ch.isupper():
            ch = ch.lower()
            result = result + " "
        result = result + ch
    print(result)

if __name__ == '__main__':
    main()
