"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result



# TODO: Students will add multiply, divide, power, sqrt functions

def power(a, b):
    """Raise a to the power of b with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Power requires numeric inputs")
    
    print(f"Calculating {a} ^ {b}")
    result = a ** b
    print(f"Result: {result}")
    return result

def sqrt(a):
    """Return the square root of a with input validation."""
    if not isinstance(a, (int, float)):
        raise TypeError("Sqrt requires numeric input")
    if a < 0:
        raise ValueError(f"Cannot take square root of negative number: {a}")
    
    print(f"Calculating √{a}")
    result = math.sqrt(a)
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")