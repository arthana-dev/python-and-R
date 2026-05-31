matrix = []

for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Row sums:")
for row in matrix:
    print(sum(row))

print("Column sums:")
for j in range(3):
    col_sum = 0
    for i in range(3):
        col_sum += matrix[i][j]
    print(col_sum)

total = 0
for row in matrix:
    total += sum(row)

print("Total sum =", total)