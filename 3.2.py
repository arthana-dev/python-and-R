numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Complete List:", numbers)
print("Total Elements:", len(numbers))