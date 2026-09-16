def employee_salary(*args, **kwargs):
    # Combine all salaries: positional (unnamed) + keyword (named employees)
    all_salaries = list(args) + list(kwargs.values())

    if not all_salaries:
        print("No salary data provided.")
        return

    average = sum(all_salaries) / len(all_salaries)
    highest = max(all_salaries)
    lowest = min(all_salaries)

    above_average = {name: salary for name, salary in kwargs.items() if salary > average}

    print("All Salaries:", all_salaries)
    print("Average Salary: {:.2f}".format(average))
    print("Highest Salary:", highest)
    print("Lowest Salary:", lowest)
    print("Employees Above Average Salary:", above_average)


# Example
employee_salary(30000, 45000, John=60000, Alice=25000, Bob=50000)