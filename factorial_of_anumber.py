def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test
print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(1))   # 1
print(factorial(7))   # 5040