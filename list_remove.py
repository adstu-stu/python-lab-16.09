numbers = []

n = int(input("How many integers? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Remove duplicates while preserving order
seen = set()
unique_numbers = []

for num in numbers:
    if num not in seen:
        seen.add(num)
        unique_numbers.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)