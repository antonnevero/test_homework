class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def __str__(self):
        return self.__author, self.__header, self.__publisher


def main():
    name = input("Name: ")
    animal_type = input("Animal_type: ")
    age = input("age: ")
    pet = Pet(name, animal_type, age)

    print(pet.get_name())
    print(pet.get_animal_type())
    print(pet.get_age())


if __name__ == '__main__':
    main()
