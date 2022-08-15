
def main():
    print(rec_print(50))


def rec_print(x):
    if x == 0:
        return x
    else:
        return x + rec_print(x-1)



if __name__ == '__main__':
    main()
