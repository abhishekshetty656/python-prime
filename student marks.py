def calculate_average(marks):
    average = sum(marks) / len(marks)
    
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

# Collect marks
marks = []

for i in range(3):
    mark = int(input(f"Enter mark {i + 1} (0 to 100): "))
    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print("The marks should be in between 0 to 100")
        exit()

# Calculate and print grade
calculate_average(marks)
