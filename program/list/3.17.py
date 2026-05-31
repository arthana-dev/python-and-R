matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("First row:", matrix[0])

print("Last column:",
      [matrix[0][2], matrix[1][2], matrix[2][2]])

total = 0

for row in matrix:
    for num in row:
        total += num

print("Sum =", total)