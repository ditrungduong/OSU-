# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 11/8/2022
# Description: Write count_seq function to print
# a sequence that starts like this: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112,

def seq_generator(num):
    """Sequence generator"""
    # Initial number sequence
    if num == 1:
        return "2"
    if num == 2:
        return "12"
    # Beginning of sequence development
    num_str = "12"
    # For loop begin from 3 to the nth position
    for char in range(3, num + 1):
        num_str += " "  # add a space for new number
        num_count = 1  # Initial count for each digit
        num_temp = ""  # temp number of each iteration
        for index in range(1, len(num_str)):
            if num_str[index] != num_str[index - 1]:
                num_temp += str(num_count)  # add count amount to temp number for new number character
                num_temp += num_str[index - 1]  # add same digit character to num temp
                num_count = 1  # keep count as one because not the same
            else:
                num_count += 1  # adding
        num_str = num_temp  # assigning temp number as new number string
    return num_str  # return new string of number


def count_seq():
    """Write a generator function named count_seq that doesn't require any arguments
    and generates a sequence that starts like this: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112 """
    num = 1
    while num > 0:
        yield seq_generator(num)
        num += 1



