import random


def main():
    user_date = input("Your date: ")
    list_u = user_date.split('/')
    date = list_u[0]
    month = list_u[1]
    year = list_u[2]
    if month == '07':
        month = "July"
    print(date, month, year + ' y.')




if __name__ == '__main__':
    main()
