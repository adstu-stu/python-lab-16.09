def remove_last(lst):
    lst.pop()  # modifies the list in place
    return lst

# Test
my_list = [1, 2, 3, 4, 5]
print("Before:", my_list)

remove_last(my_list)

print("After:", my_list)