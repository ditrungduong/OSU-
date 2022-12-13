# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/25/2022
# Description:Write a function that return true if it
# is possible to solve the puzzle from the starting configuration and false if it is impossible.
def row_puzzle(num_list, start_index=0, memo=None):
    """Given a list of number, return True if puzzle can be solved otherwise return False"""
    if memo is None:
        memo = []
    # Base condition: value = 0
    current_index = num_list[start_index]
    # Checking if the current position is at the end of the list by +1 into the current index pos

    if current_index == 0 and len(num_list) == start_index + 1:
        return True
    else:
        # If function has not gone to this position yet
        if start_index not in memo:
            # Add this index into memory list
            memo.append(start_index)
            left_move = False
            right_move = False
            # Calculate next left index position
            left_start_index = start_index - current_index
            # Check whether the next move hit the beginning of the list. Should not be negative. Max value is index 0
            if left_start_index >= 0:
                # Recursion using new left start index
                left_move = row_puzzle(num_list, left_start_index, memo)
            # Calculate next right index position
            right_start_index = start_index + current_index
            # Check whether the next index move go beyond the list by comparing with list length
            if right_start_index < len(num_list):
                # Recursion using new right start index
                right_move = row_puzzle(num_list, right_start_index, memo)
                # Return value if we have a left or right path or False.
            return left_move or right_move

print(row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0]))
print(row_puzzle([1, 3, 2, 1, 3, 4, 0]))
print(row_puzzle([3,2,2,1,2,0]))