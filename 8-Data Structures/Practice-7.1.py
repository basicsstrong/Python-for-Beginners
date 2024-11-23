def main():
    """
    A program to store student names and their grades in a dictionary, 
    calculate the average grade, and print the results.
    """
    # Define a dictionary with student names as keys and their grades as values
    student_grades = {
        "Elevan": 85,
        "Bill": 78,
        "Susen": 92,
        "Diana": 88,
        "Eve": 74
    }

    # Calculate the average grade
    total_grades = sum(student_grades.values())  # Sum of all grades
    num_students = len(student_grades)          # Total number of students
    average_grade = total_grades / num_students  # Average grade calculation

    # Print each student's name and grade
    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

    # Print the average grade
    print("\nAverage Grade:", round(average_grade, 2))  # Rounded to 2 decimal places

if __name__ == "__main__":
    main()
