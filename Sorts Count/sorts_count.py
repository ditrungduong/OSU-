# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/13/2022
# Description: Count the amount of comparisons and exchanges for bubble sort and insertion sort

def bubble_count(test_list):
    """  Sorts a_list in ascending order & count number of shift """
    number_of_comparisons = 0
    number_of_exchanges = 0
    for pass_num in range(len(test_list) - 1):
        for index in range(len(test_list) - 1 - pass_num):
            if test_list[index] <= test_list[index + 1]:
                number_of_comparisons += 1
            if test_list[index] > test_list[index + 1]:
                number_of_comparisons += 1
                temp = test_list[index]
                test_list[index] = test_list[index + 1]
                test_list[index + 1] = temp
                number_of_exchanges += 1
    return number_of_comparisons, number_of_exchanges


def insertion_count(test_list):
    """Sorts a_list in ascending order & count the amount of comparisons and exchanges
     """
    number_of_comparisons = 0
    number_of_exchanges = 0
    for index in range(1, len(test_list)):
        current_value = test_list[index]
        pos = index - 1
        if pos >= 0 and test_list[pos] <= current_value:
            number_of_comparisons += 1
        while pos >= 0 and test_list[pos] > current_value:
            number_of_comparisons += 1
            test_list[pos + 1] = test_list[pos]
            number_of_exchanges += 1
            pos -= 1
        test_list[pos + 1] = current_value
    return number_of_comparisons, number_of_exchanges
