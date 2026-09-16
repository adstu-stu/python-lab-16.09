def student_result(**kwargs):
    if not kwargs:
        print("No subjects provided.")
        return

    total = sum(kwargs.values())
    percentage = total / len(kwargs)
    highest_subject = max(kwargs, key=kwargs.get)
    result = "Pass" if all(marks >= 40 for marks in kwargs.values()) else "Fail"

    print("Subjects and Marks:", kwargs)
    print("Total Marks:", total)
    print("Percentage: {:.2f}%".format(percentage))
    print("Highest Scoring Subject:", highest_subject, "with", kwargs[highest_subject], "marks")
    print("Result:", result)


# Example
student_result(Math=85, Science=39, English=72, History=60)