import random
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    # with open('text.txt', "rb")
    contacts = {}

    choice = 0

    while choice != QUIT:
        choice = get_menu()

        if choice == LOOK_UP:
            look_up(contacts)
        elif choice == ADD:
            add(contacts)
        elif choice == CHANGE:
            change(contacts)
        elif choice == DELETE:
            delete(contacts)


def get_menu():
    print("Names and Emails")
    print('----------------')
    print('1 - find email')
    print('2 - add new email')
    print('3 - change email')
    print('4 - delete email')
    print('5 - quit')

    choice = int(input("Make your choice: "))

    if choice < LOOK_UP or choice > QUIT:
        choice = int(input("Make your choice: "))

    return choice


def look_up(contacts):
    name = input("Enter name: ")
    print(contacts.get(name, "Not found"))


def add(contacts):
    name = input('Enter name: ')
    email = input('Enter email: ')

    if name not in contacts:
        contacts[name] = email
    else:
        print("Name is already in the list")


def change(contacts):
    name = input("Enter name: ")

    if name in contacts:
        email = input("Enter email: ")
        contacts[name] = email
    else:
        print("Name is not found")


def delete(contacts):
    name = input("Enter name: ")

    if name in contacts:
        del contacts[name]
    else:
        print("Name is not found")


if __name__ == '__main__':
    main()
