from quinary_logic import QuinaryCalculator

# Create one calculator instance to reuse
calc = QuinaryCalculator()

def add(a, b) -> str:
    """
    Add two quinary numbers
    :return: The product of a and b in quinary as a string
    """
    return calc.decimal_to_quinary(calc.quinary_to_decimal(a) + calc.quinary_to_decimal(b))

def subtract(a, b) -> str:
    """
    Subtract two quinary numbers
    :return: The product of a and b in quinary as a string
    """
    return calc.decimal_to_quinary(calc.quinary_to_decimal(a) - calc.quinary_to_decimal(b))

def multiply(a, b) -> str:
    """
    Multiply two quinary numbers
    :return: The product of a and b in quinary as a string
    """
    return calc.decimal_to_quinary(calc.quinary_to_decimal(a) * calc.quinary_to_decimal(b))

def divide(a, b) -> str:
    """
    Divide two quinary numbers (integer division)
    :return: The product of a and b in quinary as a string
    """
    b_dec = calc.quinary_to_decimal(b)
    if b_dec == 0:
        return "Error: Division by zero"
    return calc.decimal_to_quinary(calc.quinary_to_decimal(a) // b_dec)
