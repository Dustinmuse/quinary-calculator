from quinary_logic import QuinaryCalculator
import math

# Create one calculator instance to reuse
calc = QuinaryCalculator()

def square(a) -> str:
    """
    :return: The sqaured result of the inputed number
    """
    return calc.decimal_to_quinary((calc.quinary_to_decimal(a)**2))

def square_root(a) -> str:
    """
    :return: The square root of the inputed number
    """
    return calc.decimal_to_quinary(math.sqrt((calc.quinary_to_decimal(a))))
