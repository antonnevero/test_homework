class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, solution):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__solution = solution

    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_solution(self, solution):
        self.__solution = solution

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_solution(self):
        return self.__solution

    def __str__(self):
        result = self.get_question() + '\n' + \
                 '1. ' + self.get_answer1() + '\n' + \
                 '2. ' + self.get_answer2() + '\n' + \
                 '3. ' + self.get_answer3() + '\n' + \
                 '4. ' + self.get_answer4()
        return result

    def isCorrect(self, answer):
        return answer == self.get_solution()


def main():
    first_points = 0
    second_points = 0
    player = ''

    # Создать список вопросов.
    questions = get_questions()

    for i in range(10):

        if i % 2 == 0:
            player = 'Один'
        else:
            player = 'Два'
        print('Вопрос для игрока ', player, ':')

        current = questions[i]
        print(current)
        user_answer = int(input('Введите ваше решение (номер' + \
                                ' между 1 и 4): '))
        if current.isCorrect(user_answer):
            if player == 'Один':
                first_points += 1
            else:
                second_points += 1
            print('Это правильный ответ.')
            print()
        else:
            print('Неправильно. Правильный отет', \
                  current.get_solution())
            print()

    print('Первый игрок заработал', first_points, 'очков.')
    print('Второй игрок заработал', second_points, 'очков.')
    if first_points == second_points:
        print('Ничья.')
    elif first_points > second_points:
        print('Первый игрок побеждает в игре.')
    else:
        print('Второй игрок побеждает в игре.')


def get_questions():
    questions = []

    # Создать словарь вопросов и добавить в список.
    question1 = Question('Сколько дней в лунном ' + \
                                  'году?', '354', '365', \
                                  '243', '379', 1)
    questions.append(question1)
    question2 = Question('Какая самая большая планета?', \
                                  'Марс', 'Юпитер', 'Земля', \
                                  'Плутон', 2)
    questions.append(question2)
    question3 = Question('Какой кит самый ' + \
                                  'большой?', 'Косатка', \
                                  'Горбатый кит', \
                                  'Белуга', 'Синий кит', 4)
    questions.append(question3)
    question4 = Question('Какой динозавр мог летать?', \
                                  'Трицератопс', 'Тираннозавр', \
                                  'Птеранодон', 'Диплодок', 3)
    questions.append(question4)
    question5 = Question('Какой из этих героев книги ' + \
                                  'о Винни Пухе является осликом?', \
                                  'Пух', 'Иа-Иа', 'Пятачок', \
                                  'Канга', 2)
    questions.append(question5)
    question6 = Question('Какая из них самая жаркая планета?', \
                                  'Марс', 'Плутон', 'Земля', \
                                  'Венера', 4)
    questions.append(question6)
    question7 = Question('У какого динозавра был самый ' + \
                                  'большой мозг по сравнению с ' + \
                                  ' телом тела?', 'Троодон', \
                                  'Стегозавр', \
                                  'Ихтиозавр', 'Гигантораптор', 1)
    questions.append(question7)
    question8 = Question('Какой из пингвинов самый ' + \
                                  'крупный?', \
                                  'Антарктический пингвин', \
                                  'Золотоволосый пингвин', \
                                  'Императорский пингвин', \
                                  'Белокрылый пингвин', 3)
    questions.append(question8)
    question9 = Question("В какой сказке героем " + \
                                  'является обезъянка?', \
                                  'Винни Пух', \
                                  'Любопытный Джордж', 'Хортон', \
                                  'Гуфи', 2)
    questions.append(question9)
    question10 = Question('Сколько длится год на Марсе?', \
                                   '550 земных дней', \
                                   '498 земных дней', \
                                   '126 земных дней', \
                                   '687 земных дней', 4)
    questions.append(question10)

    return questions


if __name__ == '__main__':
    main()
