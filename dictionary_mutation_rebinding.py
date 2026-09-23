def add_entry(d):
    d["new_key"] = "new_value"  # modifies the dictionary in place
    return d

def reassign_dict(d):
    d = {"completely": "different"}  # rebinds local variable to a new dict
    return d

# Test both on the same dictionary
my_dict = {"a": 1, "b": 2}
print("Original before:", my_dict)

add_entry(my_dict)
print("After add_entry:", my_dict)

reassign_dict(my_dict)
print("After reassign_dict:", my_dict)