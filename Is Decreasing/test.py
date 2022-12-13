def is_decreasing(num_list):
    """Return True if the elements of the list are strictly decreasing but return False otherwise"""
    if len(num_list) == 2:
        if num_list[0] > num_list[1]:
            return True
        else:
            return False
    if num_list[0] > num_list[1]:
       return is_decreasing(num_list[1:])
    else:
        return False

