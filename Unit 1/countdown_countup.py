"""
Question 1: Recursive Countdown and Countup Functions
This program implements recursive functions for counting down and counting up.
"""

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


if __name__ == "__main__":
    main()
