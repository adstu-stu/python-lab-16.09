def second_largest(*args):
    unique = []
    for num in args:
        if num not in unique:
            unique.append(num)
    
    if len(unique) < 2:
        return None  # not enough unique numbers
    
    largest = second = float('-inf')
    for num in unique:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    
    return second
print(second_largest(4, 1, 7, 7, 3, 9, 9))  # 7
print(second_largest(5, 5, 5))              # None
print(second_largest(10, 20))               # 10