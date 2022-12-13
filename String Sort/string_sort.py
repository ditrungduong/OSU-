# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/13/2022
# Description: Initate a box class with volume calculating function. Create selection sort for volume after calculation

def string_sort(string_example):
    """
     Sorts a_list of string in ascending order
     """
    sorted_example = string_example
    for index in range(1, len(string_example)):
        current_value = string_example[index].lower()
        pos = index - 1
        while pos >= 0 and string_example[pos] > current_value:
            string_example[pos + 1] = string_example[pos]
            pos -= 1
        string_example[pos + 1] = current_value
    return sorted_example
fruits = ['grape', 'banana', 'strawberry', 'apple', 'peach', 'cherry']
print(string_sort(fruits))
