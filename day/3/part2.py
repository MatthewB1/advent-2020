import numpy

class Slope:
    def __init__(self, slope_length, slope_height):
        self.length = slope_length
        self.height = slope_height

slopes = []
slopes.append(Slope(1,1))
slopes.append(Slope(3,1))
slopes.append(Slope(5,1))
slopes.append(Slope(7,1))
slopes.append(Slope(1,2))


file = open('input.txt', 'r')
grid = [list(i.replace('\n','')) for i in file.readlines()]

ROW_LENGTH, COL_LENGTH = len(grid[0]), len(grid)

def find_trees_for_slope(slope_length, slope_height):
    tree_count, i, j = 0, 0, 0

    while i < ROW_LENGTH and j < COL_LENGTH:

        if grid[j][i] == '#':
            tree_count += 1

        i += slope_length
        j += slope_height

        #wrap around row
        if i >= ROW_LENGTH:
            i -= ROW_LENGTH

    return tree_count
    

tree_counts = []

for slope in slopes:
    count = find_trees_for_slope(slope.length, slope.height)
    print(f'Slope {slope.length},{slope.height}: {count}')
    tree_counts.append(count)

product = numpy.product(tree_counts)

print(f'Product of trees encountered: {product}')