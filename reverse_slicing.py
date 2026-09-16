numbers = []

n = int(input("How many elements? "))

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Reverse without reverse() or slicing
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)