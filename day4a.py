with open('day4.txt') as f:
    lines = [line.rstrip() for line in f]

grid = []
for line in lines:
    new_line = []
    new_mooo = []
    for c in line:
        new_line.append(c)
    grid.append(new_line)

# [row, col]
directions = [
    (-1,-1),(-1, 0),(-1, 1),
    (0, -1),(0, 1),
    (1, -1),(1, 0),(1, 1)
]
word = "MAS"
counter = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        char = grid[row][col]

        if char == "X":
            for direction in directions:
                d_r, d_c = direction
                good = True

                for i in range(len(word)):
                    n_r = row + d_r * (i + 1)
                    n_c = col + d_c * (i + 1)

                    if n_r < 0 or n_r >= len(grid) or n_c < 0 or n_c >= len(grid[0]) or grid[n_r][n_c] != word[i]:
                        good = False
                        break
                if good:
                    counter += 1

print(counter)






