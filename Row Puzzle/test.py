def rec_row_puzzle(puzzle, index_pos, memo=None):
    if memo is None:
        memo = []
    row_index = puzzle[index_pos]
    # Add row_index as visited in memo list
    memo.append(row_index)
    # Base condition when index = 0 and at the end of the list
    if row_index == 0 and index_pos == len(puzzle) - 1:
        return True
    else:
        # Next moving position
        left_move = False
        right_move = False
        #
        left_move_index = index_pos - row_index
        if left_move_index >= 0 and left_move_index not in memo:
            left_move = rec_row_puzzle(puzzle, left_move_index, memo)

        right_move = index_pos + row_index
        if right_move < len(puzzle) and right_move not in memo:
            right_move = rec_row_puzzle(puzzle, right_move, memo)

        return right_move or left_move


def row_puzzle(puzzle):
    return rec_row_puzzle(puzzle, 0)


# tests
print(row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0]))
print(row_puzzle([1, 3, 2, 1, 3, 4, 0]))
