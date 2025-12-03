"""
Simple test script to demonstrate division by zero error WITH handling
"""

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
