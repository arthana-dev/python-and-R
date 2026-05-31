numbers = [10, 20, 30, 40, 50]

target = int(input("Enter number to search: "))

if target in numbers:
    print("Found at index:", numbers.index(target))
else:
    print("Not found")