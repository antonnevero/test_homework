import random

def main():
    answers = []

    with open("text.txt", "r") as file:
        for i in file:
            answers.append(i.strip())
    question = input("Write a question or E for exit: ")
    while question != "E" and question != "e":
        number = random.randint(0, 11)
        print(answers[number])
        question = input("Write a question or E for exit: ")




if __name__ == '__main__':
    main()
