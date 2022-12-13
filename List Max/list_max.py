# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/29/2022
# Description: Return max value from a list of number

def rec_list_max(num_list, max_num, pos=0):
    """Return the max number in the list using recursive"""
    if len(num_list) == 1:
        return max_num
    if pos == len(num_list):
        return max_num
    if max_num > num_list[0]:
        return rec_list_max(num_list[1:], max_num, pos)
    else:
        return rec_list_max(num_list[1:], num_list[0], pos)


def list_max(num_list):
    """"Return the max number in the list using rec_list_max"""
    max_num = num_list[0]
    return rec_list_max(num_list, max_num, pos=0)



