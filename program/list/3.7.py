numbers = [1, 2, 2, 3, 1, 1]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key, value in freq.items():
    print(key, "->", value)