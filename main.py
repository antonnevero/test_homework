
def main():
    print(rec_print(2, 50))


def rec_print(x, y):
    if y == 0:
        return 1
    else:
        return x * rec_print(x, y - 1)



if __name__ == '__main__':
    main()
