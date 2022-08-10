
def main():
    print(rec_print(7))


def rec_print(x):
    if x > 1:
        rec_print(x - 1)
    for i in range(x):
        print("*", end='')
    print()

if __name__ == '__main__':
    main()
