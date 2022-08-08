class Patient:

    def __init__(self, name, address, tel_number, emergency):
        self.__name = name
        self.__address = address
        self.__tel_number = tel_number
        self.__emergency = emergency

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tel_number(self):
        return self.__tel_number

    def get_emergency(self):
        return self.__emergency

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_tel_number(self, tel_number):
        self.__tel_number = tel_number

    def set_emergency(self, emergency):
        self.__emergency = emergency


class Procedure:

    def __init__(self, name, date, doctor, price):
        self.__name = name
        self.__date = date
        self.__doctor = doctor
        self.__price = price

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_doctor(self):
        return self.__doctor

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"{self.get_name()}, {self.get_date()}, {self.get_doctor()}, {self.get_price()}"

def main():
    patient = Patient("Carl", "New York", 5555555555, "Jessica")
    procedure1 = Procedure("osmotr", "08.08.2022", "Irvin", 250)
    procedure2 = Procedure("rentgenoscopia", "08.08.2022", "Jameson", 500)
    procedure3 = Procedure("krov", "08.08.2022", "Smith", 200)

    print(patient.get_name(), patient.get_address(), patient.get_tel_number(), patient.get_emergency())
    print(procedure1)
    print(procedure2)
    print(procedure3)
    print(f"Sum is {procedure1.get_price() + procedure2.get_price() + procedure3.get_price()}")

if __name__ == '__main__':
    main()
