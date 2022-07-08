import random

def main():
    print(get_count("antan"))

def get_count(sentence):
    result = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        for j in sentence:
            if j == i:
                result += 1
    return result

main()
