"""
Question 2: Division by Zero Error Handling
This program demonstrates runtime error handling for division operations,
specifically focusing on the division by zero error.
"""

def divide_without_error_handling():
    """
    Demonstrates division WITHOUT error handling.
    This will crash if the user enters 0 as the divisor.
    """
    print("\n=== PROGRAM WITHOUT ERROR HANDLING ===")
    num1 = float(input("Enter the first number (numerator): "))
    num2 = float(input("Enter the second number (denominator): "))
    
    # This will cause a runtime error if num2 is zero
    result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")


def divide_with_error_handling():
    """
    Demonstrates division WITH proper error handling.
    This handles the division by zero error gracefully.
    """
    print("\n=== PROGRAM WITH ERROR HANDLING ===")
    
    try:
        num1 = float(input("Enter the first number (numerator): "))
        num2 = float(input("Enter the second number (denominator): "))
        
        # Check for division by zero before performing the operation
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
        print("Division completed successfully!")
        
    except ZeroDivisionError as e:
        print(f"\nERROR: Division by zero detected!")
        print(f"Error message: {e}")
        print("Please enter a non-zero denominator.")
        
    except ValueError as e:
        print(f"\nERROR: Invalid input!")
        print(f"Error message: {e}")
        print("Please enter valid numbers.")
        
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred!")
        print(f"Error message: {e}")


def divide_with_alternative_handling():
    """
    Demonstrates an alternative approach using if-else conditions
    to prevent the error before it occurs.
    """
    print("\n=== PROGRAM WITH PREVENTIVE ERROR CHECKING ===")
    
    try:
        num1 = float(input("Enter the first number (numerator): "))
        num2 = float(input("Enter the second number (denominator): "))
        
        # Preventive check before division
        if num2 == 0:
            print("\nERROR: Division by zero is not allowed!")
            print("Mathematical rule: Any number divided by zero is undefined.")
            print("Please run the program again with a non-zero denominator.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
            print("Division completed successfully!")
            
    except ValueError:
        print("\nERROR: Please enter valid numeric values!")


def main():
    """
    Main function to demonstrate different error handling approaches.
    """
    print("=" * 60)
    print("DIVISION BY ZERO ERROR HANDLING DEMONSTRATION")
    print("=" * 60)
    
    while True:
        print("\nChoose an option:")
        print("1. Demonstrate division WITHOUT error handling (will crash on zero)")
        print("2. Demonstrate division WITH error handling (try-except)")
        print("3. Demonstrate division WITH preventive checking (if-else)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            try:
                divide_without_error_handling()
            except ZeroDivisionError as e:
                print(f"\n*** PROGRAM CRASHED ***")
                print(f"Runtime Error: {type(e).__name__}")
                print(f"Error Message: {e}")
                print("This is what happens without error handling!")
                
        elif choice == '2':
            divide_with_error_handling()
            
        elif choice == '3':
            divide_with_alternative_handling()
            
        elif choice == '4':
            print("\nThank you for using the program!")
            break
            
        else:
            print("\nInvalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
