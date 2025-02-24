import math
import sys

def squareRoot(x):
    if x < 0:
        return "Square root cannot be computed for negative numbers"
    return math.sqrt(x)

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
