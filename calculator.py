import math

def squareRoot(x):
    if x < 0:
        return "Square root cannot be computed for negative numbers"
    return math.sqrt(x)

def main():
    while True:
        print("\nCalculator")
        print("******************")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            x = float(input("Enter a number: "))
            print("Result:", squareRoot(x))

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
