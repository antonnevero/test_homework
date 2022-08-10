
def main():
    rec_print(5)


def rec_print(n):
    if n > 1:
        rec_print(n - 1)
    print(n)


if __name__ == '__main__':
    main()
