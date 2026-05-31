marks = []

for i in range(10):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

count = 0

for mark in marks:
    if mark > average:
        count += 1

print("Highest =", highest)
print("Lowest =", lowest)
print("Average =", average)
print("Above Average =", count)