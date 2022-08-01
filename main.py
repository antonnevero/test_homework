import random


def main():
    answer = input("Enter the sentence: ").lower()
    result = ''
    count1 = 0
    for i in answer:
        count = 0
        for j in answer:
            if j == i:
                count += 1
        if count > count1:
            count1 = count
            result = i
    print(result)

if __name__ == '__main__':
    main()
