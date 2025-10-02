class GradingSystem:
    def __init__(self):
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def _get_remarks(self, avg):
        if avg < 50: return "Dropped"
        if avg < 75: return "Failed"
        if avg < 80: return "Passed - Satisfactory"
        if avg < 85: return "Passed - Good"
        if avg < 90: return "Passed - Average"
        if avg < 100: return "Passed - Very Good"
        return "Passed - Excellent"
    
    def display_results(self):
        if not self.grades:
            print("No valid grades entered.")
            return
        
        avg = sum(self.grades) / len(self.grades)
        point = ((100 - avg) + 10) / 10
        
        print("\n" + "=" * 50)
        print("STUDENT GRADING SYSTEM - RESULTS")
        print("=" * 50)
        print(f"\nEntered Grades: {self.grades}")
        print(f"Average Grade: {avg:.2f}")
        print(f"Point Grade: {point:.2f}")
        print(f"Remarks: {self._get_remarks(avg)}")
        print("=" * 50 + "\n")


# Usage
print("=" * 50)
print("UNIVERSITY OF MINDANAO - GRADING SYSTEM")
print("=" * 50)
print("Enter grades (0-100). Enter -1 to finish.\n")

grading = GradingSystem()

while True:
    try:
        grade = float(input("Enter grade: "))
        if grade == -1:
            break
        if not grading.add_grade(grade):
            print(f"Invalid grade: {grade}. Must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

grading.display_results()
