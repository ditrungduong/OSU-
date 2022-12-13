# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/17/2022
# Description: A function to sum numbers from a text file and return a text file
def file_sum(num_list):
    result = 0
    with open(num_list, 'r') as num_list:
        for number in num_list:
            result += float(number.strip())
    with open('sum.txt', 'w') as outfile:
        outfile.write(str(result))
