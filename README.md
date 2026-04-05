# -part1_grade_tracker.ipynb
# Student Grade Tracker

 

## Assignment Overview

This project is part of **Assignment – Part 1: Python Basics & Control Flow**. 

The objective is to build a **command‑line Student Grade Tracker** that processes student data, analyses marks, and generates summary reports using only core Python concepts.

 

The assignment focuses on:

- Data cleaning and parsing

- Loops and conditional logic

- String manipulation

- Basic statistics and reporting

- Defensive input handling

 

No external libraries are used.

 

---

 

## Tasks Implemented

 

### ✅ Task 1: Data Parsing & Profile Cleaning

- Parsed raw student data containing inconsistent casing, spacing, and data types

- Cleaned and normalised:

  - Student names (trimmed whitespace, Title Case)

  - Roll numbers (converted from string to integer)

  - Marks (converted from comma‑separated string to list of integers)

- Validated each student’s name to ensure all words contain only alphabetic characters

- Printed formatted student profile cards

- Displayed name in **uppercase and lowercase** for the student with roll number 103

 

This task demonstrates real‑world data cleaning, which is essential when working with user input, forms, or external data sources.

 

---

 

### ✅ Task 2: Marks Analysis Using Loops & Conditionals

- Displayed subject‑wise marks along with grade labels based on predefined ranges

- Calculated and printed:

  - Total marks

  - Average marks (rounded to 2 decimal places)

  - Highest scoring subject

  - Lowest scoring subject

- Implemented a marks entry system using a `while` loop:

  - Allowed dynamic addition of new subjects

  - Handled invalid inputs (non‑numeric or out‑of‑range marks) gracefully

  - Prevented program crashes due to invalid input

- Computed updated averages after adding valid new subjects

 

This task highlights control flow, validation, and user‑interaction logic.

 

---

 

### ✅ Task 3: Class Performance Summary

- Processed class‑level data for multiple students

- Computed individual student averages and assigned Pass/Fail status

- Printed a formatted class performance table

- Calculated and displayed:

  - Number of students who passed and failed

  - Class topper (highest average)

  - Overall class average

 

This task demonstrates nested looping, aggregation logic, and formatted reporting.

 

---

 

### ✅ Task 4: String Manipulation Utility

- Cleaned an essay string by removing extra whitespace

- Performed multiple string operations:

  - Converted text to Title Case

  - Counted occurrences of the word “python” (case‑insensitive)

  - Replaced occurrences with `"Python 🐍"`

  - Split text into sentences

  - Printed each sentence on a new line with numbering and proper punctuation

 

This task reinforces Python string methods and text‑processing techniques.

 

---

 

## Technologies Used

- Python 3

- Core Python features:

  - Lists

  - Tuples

  - Dictionaries

  - Loops (`for`, `while`)

  - Conditionals

  - String methods

  - Built‑in functions

 

No external libraries were used as per assignment rules.

 

---

 

## Files in This Repository

 
