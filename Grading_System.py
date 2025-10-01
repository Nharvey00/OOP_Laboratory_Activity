def get_remarks(avg):
    if avg < 0 or avg > 100:
        return "Invalid"
    elif avg < 50:
        return "Dropped"
    elif avg < 75:
        return "Failed"
    elif avg <= 79:
        return "Passed – Satisfactory"
    elif avg <= 84:
        return "Passed – Good"
    elif avg <= 89:
        return "Passed – Average"
    elif avg <= 99:
        return "Passed – Very Good"
    else:
        return "Passed – Excellent"

print("=" * 50)
print("   University of Mindanao - Grade Checker")
print("=" * 50)
print()

grades = []

print("Enter grades (0-100), enter -1 to finish:")
while True:
    grade = int(input("Enter grade: "))
    if grade == -1:
        break
    if 0 <= grade <= 100:
        grades.append(grade)
    else:
        print(f"Invalid grade: {grade} (ignored)")

print("\n" + "=" * 50)
print("RESULTS")
print("=" * 50)

if not grades:
    print("No valid grades entered.")
else:
    print("Grades entered:", grades)
    average = sum(grades) / len(grades)
    point_grade = ((100 - average) + 10) / 10
    print(f"Average Grade: {average:.2f}")
    print(f"Point Grade: {point_grade:.2f}")
    print(f"Remarks: {get_remarks(average)}")

print("=" * 50)