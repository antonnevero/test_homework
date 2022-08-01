import random


def main():
    answer = input("Enter the sentence: ").upper()
    vowels = vowel_counter(answer)
    consonants = consonant_counter(answer)
    print(vowels, consonants)

def vowel_counter(word):
    count = 0
    vowels = 'AEIOU'
    for i in word:
        if vowels.find(i) >= 0:
            count += 1
    return count


def consonant_counter(word):
    consonants = "BCDFGJKLMNPQSTVXZHRWY"
    count = 0
    for i in word:
        if consonants.find(i) >= 0:
            count += 1
    return count

if __name__ == '__main__':
    main()
