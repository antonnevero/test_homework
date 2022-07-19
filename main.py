import random

def main():
    answers = []
    try:
        with open("text.txt", "r") as file:
            for i in file:
                answers.append(i.strip())
        question = input("Write a question or E for exit: ")
        while question != "E" or question != "e":
            number = random.randint(0, 11)
            print(answers[number])
            question = input("Write a question or E for exit: ")
    except FileNotFoundError:
        print("Error")



if __name__ == '__main__':
    main()
