numbers = [10, 20, 30]

numbers.append(40)
print("append:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.remove(20)
print("remove:", numbers)

numbers.pop()
print("pop:", numbers)

copy_list = numbers.copy()
print("copy:", copy_list)

numbers.clear()
print("clear:", numbers)