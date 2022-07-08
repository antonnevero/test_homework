import random

def main():
    print(get_count("antan"))

def get_count(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")

main()
