import math
import sys

def squareRoot(x):
    if x < 0:
        return "Square root cannot be computed for negative numbers"
    return math.sqrt(x)

def factorial(x):
    if x<0:
        return "Negative numbers doesn't have factorial"
    elif x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Undefined"
    return math.log(x, base)

def powerFunction(x,b):
    return x**b

def main():
    if len(sys.argv) < 2:
        print("Insufficient arguements passed")
        return
    choice = int(sys.argv[1])
    if choice == 1:
        if len(sys.argv) < 3:
            print("Error: Please provide a number for square root.")
            return
        x = float(sys.argv[2])
        print("Result:", squareRoot(x))

    elif choice == 2:
        if len(sys.argv) < 3:
            print("Error: Please provide a number for factorial.")
            return
        x = float(sys.argv[2])
        if x != int(x): 
                print("Error: Invalid input! Factorial is only defined for integers.")
                return
        x = int(x)
        print("Result:", factorial(x))

    elif choice == 3:  
        if len(sys.argv) < 4:
            print("Error: Please provide both base and exponent.")
            return
        x = float(sys.argv[2])
        b = float(sys.argv[3])
        print("Result:", logarithm(x, b))

    elif choice == 4:
        if len(sys.argv)<4:
            print("Error: Please provide both base (x) and exponent (b).")
            return
        x = float(sys.argv[2])
        b = float(sys.argv[3])
        print("Result:", powerFunction(x, b))
        
    elif choice == 5:
        print("Exiting\n")
        return

    else:
        print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
