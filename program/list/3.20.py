runs = []

for i in range(15):
    score = int(input(f"Match {i+1}: "))
    runs.append(score)

total = sum(runs)
average = total / len(runs)

highest = max(runs)
lowest = min(runs)

half_centuries = 0
centuries = 0

for score in runs:
    if score >= 50:
        half_centuries += 1

    if score >= 100:
        centuries += 1

print("Total Runs =", total)
print("Average =", average)
print("Highest =", highest)
print("Lowest =", lowest)
print("Half-centuries =", half_centuries)
print("Centuries =", centuries)