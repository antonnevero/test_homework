class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
            self.__name = name

    def set_address(self, address):
            self.__address = address

    def set_number(self, phone):
            self.__phone = phone

    def get_name(self):
            return self.__name

    def get_addressr(self):
            return self.__address

    def get_phone(self):
            return self.__phone


class Customer(Person):
    def __init__(self, name, address, phone, number, mailing):
        Person.__init__(self, name, address, phone)
        self.__number = number
        self.__mailing = mailing

    def set_number(self, number):
        self.__number = number

    def set_mailing(self, mailing):
        self.__mailing = mailing

    def get_number(self):
        return self.__number

    def get_mailing(self):
        return self.__mailing


def main():
    name = input("Write name:")
    address = input("Write address:")
    phone = input("Write phone:")
    number = int(input("Write number:"))
    mailing = input("Do you want mailing: y or n").lower()
    customer = Customer(name, address, phone, number, mailing)
    if mailing == "y":
        customer.set_mailing(True)
    else:
        customer.set_mailing(False)

    print(customer.get_name(), customer.get_phone(), customer.get_number(), customer.get_addressr(), customer.get_mailing())

if __name__ == '__main__':
    main()
