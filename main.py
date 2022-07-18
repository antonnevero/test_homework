import random

def main():
    answer = int(input("Enter number: "))
    list_numbers = []
    for i in range(2, answer+1):
        list_numbers.append(i)

    for i in list_numbers:
        simple_number(i)

def simple_number(number):
    flag = False
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
        else:
            flag = True
    if flag:
        print(number)




if __name__ == '__main__':
    main()
