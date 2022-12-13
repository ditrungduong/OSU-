# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/03/2022
# Description: Modify the binary search function from the exploration so that, instead of returning -1 when the target value is not in the list, raises a TargetNotFound exception

class TargetNotFound(Exception):
    """User defined exception for target not found in the list"""
    pass

def bin_except(a_list, target):
    """
  Searches a_list for an occurrence of target    
  If found, returns the index of its position in the list    
  If not found, returns -1, indicating the target value isn't in the list    
  """

    try:
        first = 0
        last = len(a_list) - 1
        while first <= last:
            middle = (first + last) // 2
            if a_list[middle] == target:
                return middle
            if a_list[middle] > target:
                last = middle - 1
            else:
                first = middle + 1
        raise TargetNotFound
    except TargetNotFound:
        return "TargetNotFound"
