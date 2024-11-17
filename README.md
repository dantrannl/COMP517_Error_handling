# COMP517_Error_handling
Contains all the lab assignments I have done for my course this year

1. amIABanana.py

This Python program introduces a custom exception class, NotABananaError, to handle cases where a given string does not contain the word "banana." It features a function, am_I_a_banana(), that checks if a string matches or includes "banana" and returns tailored messages or raises exceptions based on the input.

Skills:
- Custom Exception Handling: Demonstrates how to define and raise custom exceptions using Python's Exception class.
- String Operations: Checks for substring presence and exact matches within strings.
- Control Flow: Uses conditional statements (if, elif, else) and try-except blocks for robust error handling.

2. grade_converter.py

This Python program allows users to convert between numeric grade points and letter grades interactively. It also provides grade point ranges for letter grades. The program features robust error handling and supports both numeric and letter-grade inputs.

Skills:

Implements two conversion functions: 
- grade_point_to_letter(): Converts numeric grade points to corresponding letter grades.
- letter_point_to_grade_point(): Converts letter grades to grade point ranges.
- Interactive Input and Output: Continuously accepts user input until an exit command ("end" or a blank line) is entered.
- String Manipulation: Ensures case-insensitivity by converting input strings to uppercase.
- Conditional Logic: Uses if-elif structures to map grade points to letter grades and vice versa.
- Error Handling: Catches invalid inputs and raises appropriate exceptions (ValueError).

3. sum_init.py

This Python program calculates a running total of user-inputted numbers, demonstrating interactive input handling and error checking. Users can enter numbers continuously, with the option to exit by entering a blank line or 0. Invalid inputs are gracefully handled with an error message.

Skills:
- Interactive User Input: Uses input() to accept and process user data in real time.
- Loop Control: Implements an infinite while loop with break conditions for user-defined exits.
- Error Handling: Catches invalid inputs using a try-except block to handle ValueError exceptions.
- Basic Arithmetic: Continuously updates and prints the total sum of valid numbers.
