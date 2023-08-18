num_students = int(input("Enter the number of students: "))
for student in range(1, num_students + 1):
    num_marks = int(input(f"Enter the number of marks for student {student}: "))

    marks = []
    for mark_num in range(1, num_marks + 1):
        mark = float(input(f"Enter mark {mark_num} for student {student}: "))
        marks.append(mark)

    average = sum(marks) / num_marks
    max_mark = max(marks)
    min_mark = min(marks)

    print(f"Average mark for student {student}: {average}")
    print(f"Max mark for student {student}: {max_mark}")
    print(f"Min mark for student {student}: {min_mark:}")
    print("-" * 40)
x=int(5)
print(x)
