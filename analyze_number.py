def analyze_numbers(*args):
    evens = []
    odds = []

    for num in args:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    even_sum = sum(evens)
    odd_sum = sum(odds)

    print("Even numbers:", evens)
    print("Odd numbers:", odds)
    print("Sum of even numbers:", even_sum)
    print("Sum of odd numbers:", odd_sum)
    print("Count of even numbers:", len(evens))
    print("Count of odd numbers:", len(odds))


# Example
analyze_numbers(4, 7, 2, 9, 10, 3, 6)