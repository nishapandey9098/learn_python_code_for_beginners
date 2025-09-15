number_grid = [
    [1, 2, 3],
    [4, 5, 6],      
    [7, 8, 9],
    [0] 
]
print(number_grid[0][0])  # Output: 1
print(number_grid[2][1])  # Output: 8
for row in number_grid:
    print(row)
    for col in row:
        print(col)