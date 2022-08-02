import random


def main():
    answer = input("Enter the sentence: ").upper()
    answer_list = answer.split()
    final_list = []

    for i in answer_list:
        final_list.append(i[1:] + i[0] + "КИ")
    print(' '.join(final_list))



if __name__ == '__main__':
    main()
