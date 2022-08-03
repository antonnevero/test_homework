import random


def main():
    uncrypted_word = ''
    codes = {
        'a': '%',
        'n': '!',
        't': '$',
        'o': '#'
    }
    with open('text.txt', 'r') as file:
        text_list = file.readlines()
    word = (''.join(text_list)).lower()
    for i in word:
        for k, v in codes.items():
            if i == v:
                uncrypted_word += k
    print(uncrypted_word)


if __name__ == '__main__':
    main()
