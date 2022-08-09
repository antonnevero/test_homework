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

class ShiftSupervisor(Employee):
    def __init__(self, name, number, year_pay, premium_pay):
        Employee.__init__(self, name, number)
        self.__year_pay = year_pay
        self.__premium_pay = premium_pay

    def set_year_pay(self, year_pay):
        self.__year_pay = year_pay

    def set_premium_pay(self, premium_pay):
        self.__premium_pay = premium_pay

    def get_year_pay(self):
        return self.__year_pay

    def get_premium_pay(self):
        return self.__premium_pay

def main():
    name = input("Write name:")
    number = int(input("Write number:"))
    year_pay = int(input("Write year_pay:"))
    premium_pay = float(input("Write premium_pay:"))
    worker1 = ShiftSupervisor(name, number, year_pay, premium_pay)

    print(worker1.get_name(), worker1.get_number(), worker1.get_premium_pay(), worker1.get_year_pay())

if __name__ == '__main__':
    main()
