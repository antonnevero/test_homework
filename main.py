
def main():
    print(rec_print(2, 3))


def rec_print(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return rec_print(x - 1, 1)
    else:
        return rec_print(x - 1, rec_print(x, y - 1))



if __name__ == '__main__':
    main()
