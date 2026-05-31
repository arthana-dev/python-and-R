numbers = [10, 20, 30, 40, 50]

total = 0
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    total += num

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

average = total / len(numbers)

print("Sum =", total)
print("Average =", average)
print("Maximum =", largest)
print("Minimum =", smallest)