def countdown(n):
    while n >= 1:
        yield n
        n -= 1


for num in countdown(5):
    print(num)