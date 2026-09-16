numbers = []

for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Find sum without using sum()
total = 0
for num in numbers:
    total += num

# Find average
average = total / len(numbers)

print("List:", numbers)
print("Sum:", total)
print("Average:", average)