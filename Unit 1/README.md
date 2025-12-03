# UoPeople Programming Assignment - Term 2
## Conditionals and Recursion with Error Handling

This repository contains solutions for the programming assignment focusing on recursive functions and error handling in Python.

---

## Recursive Countdown and Countup Functions

### Overview
Implementation of two recursive functions: `countdown` (counts down from positive numbers) and `countup` (counts up from negative numbers).

### Code
File: `countdown_countup.py`

```python
def countdown(n):
    """
    Recursive function that counts down from n to 0.
    Args:
        n: A positive number to count down from
    """
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


def countup(n):
    """
    Recursive function that counts up from a negative number to 0.
    Args:
        n: A negative number to count up from
    """
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


def main():
    """
    Main function that prompts user for input and calls appropriate function.
    """
    try:
        # Get user input
        number = int(input("Enter a number: "))
        
        # Decide which function to call based on the input
        if number > 0:
            print(f"\nCalling countdown with {number}:")
            countdown(number)
        elif number < 0:
            print(f"\nCalling countup with {number}:")
            countup(number)
        else:  # number == 0
            # For zero, we call countdown as it naturally leads to Blastoff!
            print(f"\nCalling countdown with {number}:")
            countdown(number)
            
    except ValueError:
        print("Error: Please enter a valid integer!")
```

### Output Examples

#### 1. Positive Number Input (5):
```
Enter a number: 5

Calling countdown with 5:
5
4
3
2
1
Blastoff!
```

#### 2. Negative Number Input (-3):
```
Enter a number: -3

Calling countup with -3:
-3
-2
-1
Blastoff!
```

#### 3. Zero Input (0):
```
Enter a number: 0

Calling countdown with 0:
Blastoff!
```

### Explanation: Choice for Zero Input

**I chose to call `countdown` for input of zero** for the following reasons:

1. **Natural Flow**: The `countdown` function's base case checks if `n <= 0`, which naturally includes zero. When zero is passed, it immediately prints "Blastoff!" without any additional processing.

2. **Mathematical Logic**: Zero is neither positive nor negative. However, in the context of counting, zero represents the completion point. The countdown function treats zero as the "finish line," which aligns with the rocket launch metaphor ("Blastoff!" represents the moment of launch at T=0).

3. **Consistency with Base Case**: The `countdown` function is already designed to handle zero as its terminating condition. Using it for zero input maintains consistency with the function's existing logic.

4. **Simplicity**: Calling `countdown(0)` produces the cleanest output - just "Blastoff!" - which appropriately represents the "launch moment" without unnecessary counting.

---

## Division by Zero Error Handling

### Overview
This program demonstrates runtime error handling for division operations, specifically focusing on the division by zero error. It includes three versions: without error handling, with try-except blocks, and with preventive checking.

### Code Demonstration

#### Without Error Handling
File: `test_error_without_handling.py`

```python
print("=== DEMONSTRATION: Runtime Error WITHOUT Error Handling ===\n")

num1 = 10
num2 = 0

print(f"Attempting to divide {num1} by {num2}...")
result = num1 / num2  # This will cause a ZeroDivisionError
print(f"Result: {result}")
```

**Output (Runtime Error):**
```
=== DEMONSTRATION: Runtime Error WITHOUT Error Handling ===

Attempting to divide 10 by 0...
Traceback (most recent call last):
  File "C:\Users\...\test_error_without_handling.py", line 11, in <module>
    result = num1 / num2  # This will cause a ZeroDivisionError
             ~~~~~^~~~~~
ZeroDivisionError: division by zero

Command exited with code 1
```

#### With Error Handling (Try-Except)
File: `test_error_with_handling.py`

```python
print("=== DEMONSTRATION: Runtime Error WITH Error Handling ===\n")

try:
    num1 = 10
    num2 = 0
    
    print(f"Attempting to divide {num1} by {num2}...")
    
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ZeroDivisionError as e:
    print(f"\nERROR CAUGHT: {type(e).__name__}")
    print(f"Error Message: {e}")
    print("The program handled the error gracefully and continues running.")
    
print("\n=== Program completed successfully ===")
```

**Output (Error Handled):**
```
=== DEMONSTRATION: Runtime Error WITH Error Handling ===

Attempting to divide 10 by 0...

ERROR CAUGHT: ZeroDivisionError
Error Message: Cannot divide by zero!
The program handled the error gracefully and continues running.

=== Program completed successfully ===
```

### Comprehensive Error Handling Program
File: `division_error_handling.py`

This file contains a complete interactive program with three different approaches:
1. Division without error handling (demonstrates crash)
2. Division with try-except error handling
3. Division with preventive if-else checking

### Significance of Error Handling

#### 1. **What is Error Handling?**
Error handling is a programming technique that allows a program to detect, respond to, and recover from errors that occur during execution. In Python, this is primarily achieved through try-except blocks.

#### 2. **Why is Error Handling Important?**

**In the Division by Zero Scenario:**
- **Without Error Handling**: The program crashes immediately when dividing by zero, displaying a cryptic error message and terminating abruptly. This provides a poor user experience and can lead to data loss.
- **With Error Handling**: The program catches the error, displays a user-friendly message, and continues running, allowing the user to try again or exit gracefully.

#### 3. **Potential Impact of NOT Handling Errors**

**Immediate Consequences:**
- **Program Crash**: The application terminates unexpectedly, potentially losing unsaved data
- **Poor User Experience**: Users see technical error messages instead of helpful guidance
- **Data Corruption**: If the program was in the middle of a transaction, data might be left in an inconsistent state

**Long-term Consequences:**
- **Loss of Trust**: Users lose confidence in the application's reliability
- **Debugging Difficulty**: Unhandled errors in production environments are harder to trace and fix
- **Security Vulnerabilities**: Error messages might expose sensitive system information
- **Operational Disruption**: In critical systems (medical, financial, industrial), crashes can have serious real-world consequences

#### 4. **Best Practices Demonstrated**

1. **Specific Exception Handling**: Catch specific exceptions (ZeroDivisionError) rather than generic ones
2. **User-Friendly Messages**: Provide clear, actionable error messages
3. **Graceful Degradation**: Allow the program to continue running after handling the error
4. **Preventive Checks**: Use conditional statements to prevent errors before they occur
5. **Input Validation**: Validate user input to catch errors early

#### 5. **Error Handling in Expressions and Conditions**

Error handling in expressions involves:
- **Detection**: Identifying potential error conditions (denominator == 0)
- **Prevention**: Using conditionals to avoid errors before they occur
- **Recovery**: Using try-except to catch and handle errors that do occur
- **Communication**: Providing meaningful feedback to users and developers

### Mathematical Context
Division by zero is mathematically undefined because:
- No number multiplied by 0 equals a non-zero number
- The result would be infinite or undefined
- It violates fundamental mathematical rules

---

## How to Run the Programs

### Recursive Countdown/Countup:
```bash
python countdown_countup.py
```
Then enter a number when prompted.

### Division Error Handling:
```bash
# Interactive version with menu
python division_error_handling.py

# Simple demonstrations
python test_error_without_handling.py
python test_error_with_handling.py
```

---

## Key Learning Outcomes

1. **Recursion**: Understanding how functions can call themselves with modified parameters
2. **Base Cases**: Importance of defining termination conditions in recursive functions
3. **Error Handling**: Using try-except blocks to manage runtime errors
4. **Preventive Programming**: Checking conditions before operations that might fail
5. **User Experience**: Providing helpful feedback instead of letting programs crash

---

## Files in This Repository

- `countdown_countup.py` - Recursive countdown and countup functions
- `division_error_handling.py` - Interactive error handling demonstration
- `test_error_without_handling.py` - Simple demonstration of unhandled error
- `test_error_with_handling.py` - Simple demonstration of handled error
- `README.md` - This documentation file

---

## Author
**Student Name**: Lois Adu Yeboah  
**Course**: UoPeople Programming Course  
**Assignment**: Term 2 - Conditionals and Recursion with Error Handling  
**Date**: December 3, 2025
