class Employee:

    def __init__(self, name, id, department, job_title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job_title = job_title

    def __str__(self):
        return f'Name - {self.__name}, id - {self.__id}, department - {self.__department}, job title - {self.__job_title}'

def main():
    e1 = Employee('Susan', 47899, 'Account', 'Vice-President')
    e2 = Employee('Mark', 39119, 'IT', 'Programmer')
    e3 = Employee('Joe', 81774, 'Account', 'production')

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
    main()
