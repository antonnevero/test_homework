import random


def main():
    answer = input("Enter the sentence: ")
    answer_upper = to_upper(answer)
    print(answer_upper)


def to_upper(word):
    result = ''
    new_sentence = True
    result_word = ''

    words = word.split()
    for item in words:
        if new_sentence:
            result_word = item[0].upper() + item[1:]
        else:
            result_word = item
        result = result + result_word + ' '
        if item[-1] == '.' or item[-1] == '?' or item[-1] == '!':
            new_sentence = True
        else:
            new_sentence = False
    return result

if __name__ == '__main__':
    main()
