import random

def main():
    lo_shu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    print(magic(lo_shu))

def magic(magic_list):
    first_row = magic_list[0][0] + magic_list[0][1] + magic_list[0][2]
    second_row = magic_list[1][0] + magic_list[1][1] + magic_list[1][2]
    third_row = magic_list[2][0] + magic_list[2][1] + magic_list[2][2]
    first_col = magic_list[0][0] + magic_list[1][0] + magic_list[2][0]
    second_col = magic_list[0][1] + magic_list[1][1] + magic_list[2][1]
    third_col = magic_list[0][2] + magic_list[1][2] + magic_list[2][2]
    first_diag = magic_list[0][2] + magic_list[1][1] + magic_list[2][0]
    second_diag = magic_list[0][0] + magic_list[1][1] + magic_list[2][2]


    return first_row == second_row == third_row == first_col == second_col == third_col == first_diag == second_diag


if __name__ == '__main__':
    main()
