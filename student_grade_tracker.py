"""
Assignment — Part 1: Python Basics & Control Flow
Theme: Student Grade Tracker

This script completes all four tasks:
1) Data parsing & profile cleaning
2) Marks analysis with loops & conditionals
3) Class performance summary
4) String manipulation utility

Author: (Student)
"""

# =========================
# Task 1 — Data Parsing & Profile Cleaning
# =========================

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    # Clean name: strip spaces and convert to title case
    cleaned_name = student["name"].strip().title()

    # Convert roll number to integer
    roll = int(student["roll"])

    # Convert marks string to list of integers
    marks = [int(m.strip()) for m in student["marks_str"].split(",")]

    # Validate name: all words must be alphabetic
    name_parts = cleaned_name.split()
    is_valid = all(part.isalpha() for part in name_parts)

    if is_valid:
        print(f"✓ Valid name: {cleaned_name}")
    else:
        print(f"✗ Invalid name: {cleaned_name}")

    # Print formatted profile card
    print("=" * 32)
    print(f"Student : {cleaned_name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

    cleaned_students.append({
        "name": cleaned_name,
        "roll": roll,
        "marks": marks
    })

# Print name in ALL CAPS and lowercase for roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print("
Student with Roll 103:")
        print("Uppercase:", student["name"].upper())
        print("Lowercase:", student["name"].lower())


# =========================
# Task 2 — Marks Analysis Using Loops & Conditionals
# =========================

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"
Marks Report for {student_name}")

for subject, mark in zip(subjects, marks):
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject}: {mark} → Grade {grade}")

# Calculations
total_marks = sum(marks)
average_marks = round(total_marks / len(marks), 2)

max_mark = max(marks)
min_mark = min(marks)

highest_subject = subjects[marks.index(max_mark)]
lowest_subject = subjects[marks.index(min_mark)]

print("
Summary:")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print(f"Highest: {highest_subject} ({max_mark})")
print(f"Lowest : {lowest_subject} ({min_mark})")

# While-loop marks entry system
new_subjects = []
new_marks = []

while True:
    subject = input("
Enter subject name (or 'done'): ")

    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0–100): ")

    if not mark_input.isdigit():
        print("Invalid marks. Please enter a number.")
        continue

    mark_value = int(mark_input)

    if mark_value < 0 or mark_value > 100:
        print("Marks must be between 0 and 100.")
        continue

    new_subjects.append(subject)
    new_marks.append(mark_value)

print(f"
New subjects added: {len(new_subjects)}")

all_marks = marks + new_marks
updated_average = round(sum(all_marks) / len(all_marks), 2)
print("Updated Average:", updated_average)


# =========================
# Task 3 — Class Performance Summary
# =========================

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("
Class Performance Report")
print("Name              | Average | Status")
print("-" * 40)

pass_count = 0
fail_count = 0
averages = []

topper_name = ""
topper_avg = 0

for name, marks_list in class_data:
    avg = round(sum(marks_list) / len(marks_list), 2)
    averages.append(avg)

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    print(f"{name.ljust(18)} | {str(avg).rjust(7)} | {status}")

class_average = round(sum(averages) / len(averages), 2)

print("
Summary:")
print("Passed:", pass_count)
print("Failed:", fail_count)
print(f"Topper: {topper_name} ({topper_avg})")
print("Class Average:", class_average)


# =========================
# Task 4 — String Manipulation Utility
# =========================

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip whitespace
clean_essay = essay.strip().lower()
print("
Clean Essay:")
print(clean_essay)

# Step 2: Title Case
print("
Title Case:")
print(clean_essay.title())

# Step 3: Count occurrences of 'python'
count_python = clean_essay.count("python")
print("
Count of 'python':", count_python)

# Step 4: Replace 'python' with 'Python 🐍'
replaced_essay = clean_essay.replace("python", "Python 🐍")
print("
Replaced Essay:")
print(replaced_essay)

# Step 5: Split into sentences
sentences = clean_essay.split(". ")
print("
Sentence List:")
print(sentences)

# Step 6: Print numbered sentences
print("
Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
