
def main():
    print(rec_print(5, 7))


def rec_print(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + rec_print(x, y - 1)


if __name__ == '__main__':
    main()
