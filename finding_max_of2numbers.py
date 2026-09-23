def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Test
print(find_max(10, 25))   # 25
print(find_max(37, 12))   # 37
print(find_max(8, 8))     # 8 (equal, returns either)