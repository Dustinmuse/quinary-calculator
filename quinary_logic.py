class QuinaryCalculator:
    def __init__(self):
        self.first_number = None
        self.second_number = None
        self.operation = None
        self.quinaryDisplay = True
    
    def decimal_to_quinary(self, n: int) -> str:
        if n == 0:
            return "0"
        s = ""
        while n:
            s = str(n%5) + s
            n //= 5
        return s
    
    def quinary_to_decimal(self, q: str) -> int:
        dec = 0
        for dig in q:
            if dig not in "01234":
                raise ValueError(f"Invalid digit '{dig}' in quinary number")
            dec = dec * 5 + int(dig)
        return dec