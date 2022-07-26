import random


def main():
    global index
    digit_list = ['2', '3', '4', '5', '6', '7', '8', '9']
    tel_num = ''
    num_phone_number = ''
    tel_num = input("Telephone number: ")
    for ch in tel_num:
        if ch.isalpha():
            ch = ch.upper()
            if ch == "A" or ch == "B" or ch == "C":
                index = 0
            elif ch == 'D' or ch == 'E' or ch == 'F':
                index = 1
            elif ch == 'G' or ch == 'H' or ch == 'I':
                index = 2
            elif ch == 'J' or ch == 'K' or ch == 'L':
                index = 3
            elif ch == 'M' or ch == 'N' or ch == 'O':
                index = 4
            elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
                index = 5
            elif ch == 'T' or ch == 'U' or ch == 'V':
                index = 6
            elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
                index = 7
            ch = digit_list[index]
        num_phone_number = num_phone_number + ch
    print(num_phone_number)


if __name__ == '__main__':
    main()
