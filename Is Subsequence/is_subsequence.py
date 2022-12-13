# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/24/2022
# Description: Write a function to tell if a string is a subsequence of another string
def is_subsequence(short_string, long_string):
    """Returns True if the first string is a subsequence of the second string, otherwise False"""
    if len(short_string) == 0:
        return True
    if len(long_string) == 0:
        return False
    if short_string[0] == long_string[0]:
        return is_subsequence(short_string[1:], long_string[1:])
    return is_subsequence(short_string, long_string[1:])


