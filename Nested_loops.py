number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# The first square bracket represents the row while the second represents the column
print(number_grid[0,2])

for row in number_grid:
    for col in row:
        print(col)
    