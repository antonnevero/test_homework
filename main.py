import random

def main():
    right_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    student_answers = []
    wrong_answers = []
    with open("text.txt") as file:
        for c in file:
            student_answers.append(c.strip("\n"))
    count = 0
    count_not_right = 0
    for i in range(len(right_answers)):
        if right_answers[i] == student_answers[i]:
            count += 1
        else:
            count_not_right += 1
            wrong_answers.append(i + 1)
    if count > 14:
        print("You're good!")
    else:
        print("Fuck you!")
    print(count)
    print(count_not_right)
    print(f"Wrong answers for questions: {wrong_answers}")


main()
