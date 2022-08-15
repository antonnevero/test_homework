
def main():
    print(rec_print([5, 7, 9, 3]))


def rec_print(x):
    n = len(x)
    if n == 1:
        return x[0]
    else:
        return x[n-1] + rec_print(x[0:n-1])



if __name__ == '__main__':
    main()
