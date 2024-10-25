#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Assign command line arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Perform calculation based on the operator
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Print the result
    print(f"{a} {operator} {b} = {result}")
