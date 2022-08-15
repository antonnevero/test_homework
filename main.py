
def main():
    print(rec_print([5, 7, 9, 3]))


def rec_print(x):
    n = len(x)
    if n == 1:
        return x[0]
    else:
        temp = rec_print(x[0:n-1])
        if x[n-1] > temp:
            return x[n-1]
        else:
            return temp



if __name__ == '__main__':
    main()
