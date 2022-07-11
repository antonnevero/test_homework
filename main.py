import random
ROWS = 3
COLS = 4
def main():
    list_2d = [[0 for r in range(COLS)] for c in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            print(list_2d[r][c])

    # print(list_2d)



main()
