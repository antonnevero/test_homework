import random


def main():
    dict1 = {
        'CS101': 3004,
        'CS102': 4501,
        'CS103': 6755,
        'NT110': 1244,
        'CM241': 1411
    }

    dict2 = {
        'CS101': 'Хайнс',
        'CS102': 'Альварадо',
        'CS103': 'Рич',
        'NT110': 'Берк',
        'CM241': 'Ли'
    }

    dict3 = {
        'CS101': '08:00',
        'CS102': '09:00',
        'CS103': "10:00",
        'NT110': '11:00',
        'CM241': '13:00'
    }
    answer = input("Input number of course: ")
    if answer not in dict1:
        print("Wrong number of course")
    else:
        print(dict1[answer])
        print(dict2[answer])
        print(dict3[answer])


if __name__ == '__main__':
    main()
