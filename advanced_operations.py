from quinary_logic import QuinaryCalculator
import math

# Create one calculator instance to reuse
calc = QuinaryCalculator()

def square(a: int) -> int:
    """
    :return: The squared result of the inputed number
    """
    return calc.decimal_to_quinary((calc.quinary_to_decimal(a)**2))

def square_root(a: int) -> int:
    """
    :return: The square root of the inputed number
    """
    return calc.decimal_to_quinary(int(math.sqrt((calc.quinary_to_decimal(a)))))
