
def main():
    print(ackerman(2, 3))


def ackerman(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ackerman(x - 1, 1)
    else:
        return ackerman(x - 1, ackerman(x, y - 1))



if __name__ == '__main__':
    main()
