class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def break_car(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

def main():
    car = Car(2017, 'Dodge')
    for i in range(5):
        car.accelerate()
        print(car.get_speed())

    for i in range(5):
        car.break_car()
        print(car.get_speed())

if __name__ == '__main__':
    main()
