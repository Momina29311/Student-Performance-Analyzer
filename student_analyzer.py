import os
from datetime import datetime


# Grade boundaries stored as tuples: (minimum percentage, grade)
GRADE_SCALE = (
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F")
)


def load_students(filename):
    """
    Load student data from a text file.
    File format:
    name,roll_number,subject1,subject2,subject3
    """
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                parts = line.split(",")

                if len(parts) != 5:
                    print(f"Skipping invalid line: {line}")
                    continue

                try:
                    student = {
                        "name": parts[0].strip(),
                        "roll_number": parts[1].strip(),
                        "marks": [
                            float(parts[2].strip()),
                            float(parts[3].strip()),
                            float(parts[4].strip())
                        ]
                    }

                    students.append(student)

                except ValueError:
                    print(f"Skipping line because marks are invalid: {line}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")

    return students


def calculate_average(marks):
    """Return the average of a list of marks."""
    if not marks:
        return 0

    return sum(marks) / len(marks)


def calculate_total(marks):
    """Return the total marks."""
    return sum(marks)


def get_grade(average):
    """Return grade based on average marks."""
    for minimum_percentage, grade in GRADE_SCALE:
        if average >= minimum_percentage:
            return grade

    return "F"


def get_performance_level(average):
    """Return performance level based on average."""
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Very Good"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    elif average >= 50:
        return "Needs Improvement"
    else:
        return "Fail"


def analyze_students(students):
    """Add calculated information to every student dictionary."""
    for student in students:
        marks = student["marks"]
        student["total"] = calculate_total(marks)
        student["average"] = calculate_average(marks)
        student["grade"] = get_grade(student["average"])
        student["performance"] = get_performance_level(student["average"])

    return students


def display_students(students):
    """Display complete student information."""
    if not students:
        print("\nNo student data is available.")
        return

    print("\n" + "=" * 78)
    print("STUDENT PERFORMANCE REPORT")
    print("=" * 78)

    print(
        f"{'Roll No.':<12}"
        f"{'Name':<20}"
        f"{'Marks':<20}"
        f"{'Average':<10}"
        f"{'Grade':<8}"
        f"{'Performance'}"
    )
    print("-" * 78)

    for student in students:
        marks_text = ", ".join(str(int(mark)) for mark in student["marks"])

        print(
            f"{student['roll_number']:<12}"
            f"{student['name']:<20}"
            f"{marks_text:<20}"
            f"{student['average']:<10.2f}"
            f"{student['grade']:<8}"
            f"{student['performance']}"
        )

    print("=" * 78)


def generate_summary(students):
    """Generate overall class summary using dictionaries."""
    if not students:
        return {}

    averages = [student["average"] for student in students]

    highest_student = max(students, key=lambda student: student["average"])
    lowest_student = min(students, key=lambda student: student["average"])

    grade_count = {}

    for student in students:
        grade = student["grade"]
        grade_count[grade] = grade_count.get(grade, 0) + 1

    passed_students = len(
        [student for student in students if student["grade"] != "F"]
    )

    failed_students = len(
        [student for student in students if student["grade"] == "F"]
    )

    summary = {
        "total_students": len(students),
        "class_average": calculate_average(averages),
        "highest_student": highest_student,
        "lowest_student": lowest_student,
        "passed_students": passed_students,
        "failed_students": failed_students,
        "grade_distribution": grade_count
    }

    return summary


def display_summary(summary):
    """Display the generated summary."""
    if not summary:
        print("\nSummary cannot be generated because no students were loaded.")
        return

    highest = summary["highest_student"]
    lowest = summary["lowest_student"]

    print("\n" + "=" * 50)
    print("CLASS SUMMARY")
    print("=" * 50)
    print(f"Total Students: {summary['total_students']}")
    print(f"Class Average: {summary['class_average']:.2f}")
    print(
        f"Highest Performer: {highest['name']} "
        f"({highest['average']:.2f}, Grade {highest['grade']})"
    )
    print(
        f"Lowest Performer: {lowest['name']} "
        f"({lowest['average']:.2f}, Grade {lowest['grade']})"
    )
    print(f"Passed Students: {summary['passed_students']}")
    print(f"Failed Students: {summary['failed_students']}")

    print("\nGrade Distribution:")
    for grade, count in sorted(summary["grade_distribution"].items()):
        print(f"Grade {grade}: {count} student(s)")

    print("=" * 50)


def add_student(students):
    """Take student information from the user and add it to the list."""
    print("\nEnter New Student Information")

    try:
        name = input("Enter student name: ").strip()
        roll_number = input("Enter roll number: ").strip()

        if not name or not roll_number:
            print("Name and roll number cannot be empty.")
            return

        marks = []

        for subject_number in range(1, 4):
            mark = float(input(f"Enter marks for Subject {subject_number}: "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        student = {
            "name": name,
            "roll_number": roll_number,
            "marks": marks
        }

        students.append(student)
        analyze_students(students)

        print(f"\nStudent '{name}' added successfully.")

    except ValueError:
        print("Invalid input. Please enter numeric marks only.")


def save_summary_to_file(students, filename):
    """Save student report and class summary to a file."""
    summary = generate_summary(students)

    if not summary:
        print("No data available to save.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
            file.write("=" * 60 + "\n")
            file.write(
                f"Generated on: "
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            )

            for student in students:
                file.write(f"Name: {student['name']}\n")
                file.write(f"Roll Number: {student['roll_number']}\n")
                file.write(f"Marks: {student['marks']}\n")
                file.write(f"Total: {student['total']:.2f}\n")
                file.write(f"Average: {student['average']:.2f}\n")
                file.write(f"Grade: {student['grade']}\n")
                file.write(f"Performance: {student['performance']}\n")
                file.write("-" * 60 + "\n")

            file.write("\nCLASS SUMMARY\n")
            file.write("=" * 60 + "\n")
            file.write(f"Total Students: {summary['total_students']}\n")
            file.write(f"Class Average: {summary['class_average']:.2f}\n")
            file.write(
                f"Highest Performer: "
                f"{summary['highest_student']['name']} "
                f"({summary['highest_student']['average']:.2f})\n"
            )
            file.write(
                f"Lowest Performer: "
                f"{summary['lowest_student']['name']} "
                f"({summary['lowest_student']['average']:.2f})\n"
            )
            file.write(f"Passed Students: {summary['passed_students']}\n")
            file.write(f"Failed Students: {summary['failed_students']}\n")

            file.write("\nGrade Distribution:\n")
            for grade, count in sorted(
                summary["grade_distribution"].items()
            ):
                file.write(f"Grade {grade}: {count} student(s)\n")

        print(f"\nReport saved successfully in '{filename}'.")

    except PermissionError:
        print(f"Permission denied. Cannot write to '{filename}'.")

    except OSError as error:
        print(f"File error: {error}")


def main():
    """Main function that runs the program."""
    input_file = "students.txt"
    output_file = "student_summary.txt"

    students = load_students(input_file)
    analyze_students(students)

    while True:
        print("\n" + "=" * 40)
        print("STUDENT ANALYZER MENU")
        print("=" * 40)
        print("1. Display all students")
        print("2. Display class summary")
        print("3. Add a new student")
        print("4. Save report to file")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            summary = generate_summary(students)
            display_summary(summary)

        elif choice == "3":
            add_student(students)

        elif choice == "4":
            save_summary_to_file(students, output_file)

        elif choice == "5":
            print("\nThank you for using Student Performance Analyzer.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()