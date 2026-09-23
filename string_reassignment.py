def change_string(s):
    s = "X" + s[1:]  # creates a new string; can't modify s in place
    return s

# Test
my_string = "hello"
print("Before:", my_string)

new_string = change_string(my_string)

print("After (original):", my_string)
print("Returned (new):", new_string)