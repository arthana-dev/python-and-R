numbers = [10, 40, 20, 50, 30]

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest =", second)