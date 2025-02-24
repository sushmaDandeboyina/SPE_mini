import math
import sys

def squareRoot(x):
    if x < 0:
        return "Square root cannot be computed for negative numbers"
    return math.sqrt(x)

def main():
    if len(sys.argv) < 2:
        print("Insufficient arguements passed")
        return
    choice = int(sys.argv[1])
    # while True:
    #     print("\nCalculator")
    #     print("******************")
    #     print("1. Square Root (√x)")
    #     print("2. Factorial (x!)")
    #     print("3. Natural Logarithm (ln(x))")
    #     print("4. Power Function (x^b)")
    #     print("5. Exit")

        # choice = input("Enter choice (1-5): ")

    if choice == 1:
        if len(sys.argv) < 3:
            print("Error: Please provide a number for square root.")
            return
        x = float(sys.argv[2])
        print("Result:", squareRoot(x))
        
    elif choice == 5:
        print("Exiting\n")
        return

    else:
        print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
