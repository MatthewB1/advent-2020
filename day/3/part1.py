file = open('input.txt', 'r')
grid = [list(i.replace('\n','')) for i in file.readlines()]

row_length, col_length = len(grid[0]), len(grid)

slope_length, slope_height = 3, 1

tree_count, i, j = 0, 0, 0

while i < row_length and j < col_length:

    if grid[j][i] == '#':
        tree_count += 1

    i += slope_length
    j += slope_height

    #wrap around row
    if i >= row_length:
        i -= row_length

print(f'Trees encountered: {tree_count}')