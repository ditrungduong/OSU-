def find_gold(maze, position):
    """
    maze is a list of lists that represents a square maze
    ' ' is an empty square
    '#' is a wall
    'G' is where the gold is hidden
    position is a tuple of the current row and column

    returns a list of coordinates that leads to the gold
    """
    row_index, col_index = position  # tuple unpacking
    if row_index < 0 or row_index >= len(maze):  # base case for row out of bounds
        return None
    if col_index < 0 or col_index >= len(maze[row_index]):  # base case for column out of bounds
        return None
    if maze[row_index][col_index] == '#':  # base case for hitting a wall
        return None
    if maze[row_index][col_index] == '.':  # base case for repeating a position
        return None
    if maze[row_index][col_index] == 'G':  # base case for finding the goal
        return [(row_index, col_index)]

    maze[row_index][col_index] = '.'  # mark current square to avoid revisiting
    partial_route = find_gold(maze, (row_index-1, col_index))  # try "up"
    if partial_route is not None:
        maze[row_index][col_index] = ' '  # unmark current square
        return [(row_index, col_index)] + partial_route
    partial_route = find_gold(maze, (row_index+1, col_index))  # try "down"
    if partial_route is not None:
        maze[row_index][col_index] = ' '  # unmark current square
        return [(row_index, col_index)] + partial_route



    partial_route = find_gold(maze, (row_index, col_index-1))  # try "left"
    if partial_route is not None:
        maze[row_index][col_index] = ' '  # unmark current square
        return [(row_index, col_index)] + partial_route


    partial_route = find_gold(maze, (row_index, col_index+1))  # try "right"
    if partial_route is not None:
        maze[row_index][col_index] = ' '  # unmark current square
        return [(row_index, col_index)] + partial_route
    maze[row_index][col_index] = ' '  # unmark current square


maiz = [[' ', '#', ' ', ' ', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', '#', ' ', '#'],
        [' ', '#', ' ', '#', ' ', ' '],
        ['G', '#', '#', '#', '#', ' ']]

print(find_gold(maiz, (0,0)))
