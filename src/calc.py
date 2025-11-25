def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print("Simple CLI Calculator")
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    op = input("Enter operation (+,-,*,/): ")

    match op:
        case "+":
            print("Result:", add(a, b))
        case "-":
            print("Result:", sub(a, b))
        case "*":
            print("Result:", mul(a, b))
        case "/":
            print("Result:", div(a, b))
        case _:
            print("Invalid Operation")
