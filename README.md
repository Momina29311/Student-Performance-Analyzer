# Student Performance Analyzer

A Python console application that reads student marks, calculates grades and averages, identifies performance levels, and creates a class summary report.

## Features

- Reads student data from a text file
- Stores data using lists, tuples, and dictionaries
- Calculates total marks and average marks
- Assigns grades from A+ to F
- Identifies performance levels
- Displays a complete student report
- Generates a class-level summary
- Adds new students through user input
- Saves reports to `student_summary.txt`
- Handles invalid input and file errors using exception handling

## Concepts Used

- Python functions
- Lists
- Tuples
- Dictionaries
- User input
- Loops and conditional statements
- File handling
- Exception handling
- Modules: `os` and `datetime`

## Files

- `student_analyzer.py` — Main Python program
- `students.txt` — Sample student data
- `student_summary.txt` — Generated report file
- `README.md` — Project documentation

## Student Data Format

Each line in `students.txt` follows this format:

```text
name,roll_number,subject1,subject2,subject3
```

Example:

```text
Ali Raza,CS-001,85,90,88
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python student_analyzer.py
```

## Menu Options

1. Display all student records
2. Display the overall class summary
3. Add a student using keyboard input
4. Save the report to a text file
5. Exit the application

## Grade Scale

| Average Marks | Grade | Performance |
|---|---:|---|
| 90–100 | A+ | Excellent |
| 80–89 | A | Very Good |
| 70–79 | B | Good |
| 60–69 | C | Satisfactory |
| 50–59 | D | Needs Improvement |
| Below 50 | F | Fail |

## Author

Momina Zaheer
Skillify Internship
Artificial Intelligence Batch-07