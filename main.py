import random

def main():
    print(sum_two_smallest_numbers([2, 4, 6, 8]))

def sum_two_smallest_numbers(numbers):
    min_num = min(numbers)
    numbers.remove(min_num)
    min_num_2 = min(numbers)
    return min_num + min_num_2

main()
