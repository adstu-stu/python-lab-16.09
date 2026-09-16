fruits = []

for i in range(5):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

# Print 2nd and 4th items (index 1 and 3)
print("2nd item:", fruits[1])
print("4th item:", fruits[3])

# Replace last item with "Mango"
fruits[-1] = "Mango"

# Print updated list
print("Updated list:", fruits)