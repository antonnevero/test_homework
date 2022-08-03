import random


def main():
    crypted_word = ''
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
        if i in codes:
            crypted_word += codes[i]
    print(crypted_word)


if __name__ == '__main__':
    main()
