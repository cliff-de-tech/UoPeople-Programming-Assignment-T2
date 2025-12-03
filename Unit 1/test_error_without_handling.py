"""
Simple test script to demonstrate division by zero error WITHOUT handling
"""

print("=== DEMONSTRATION: Runtime Error WITHOUT Error Handling ===\n")

num1 = 10
num2 = 0

print(f"Attempting to divide {num1} by {num2}...")
result = num1 / num2  # This will cause a ZeroDivisionError
print(f"Result: {result}")
