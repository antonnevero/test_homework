class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
            self.__name = name

    def set_number(self, number):
            self.__number = number

    def get_name(self):
            return self.__name

    def get_number(self):
            return self.__number


class ProdactionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__pay = pay

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    def get_shift(self):
        return self.__shift

    def get_pay(self):
        return self.__pay


def main():
    name = input("Write name:")
    number = int(input("Write number:"))
    shift = int(input("Write shift:"))
    pay = float(input("Write pay:"))
    worker1 = ProdactionWorker(name, number, shift, pay)

    print(worker1.get_pay(), worker1.get_shift(), worker1.get_name(), worker1.get_number())

if __name__ == '__main__':
    main()
