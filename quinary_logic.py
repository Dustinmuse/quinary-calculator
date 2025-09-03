class QuinaryCalculator:
    def __init__(self):
        self.first_number = None
        self.second_number = None
        self.operation = None
        self.quinaryDisplay = True

    def decimal_to_quinary(self, n: int) -> int:
        if n == 0:
            return 0
        s = 0
        place = 1
        while n:
            digit = n % 5
            s = digit * place + s
            n //= 5
            place *= 10
        return s

    def quinary_to_decimal(self, q: int) -> int:
        dec = 0
        place = 1
        while q:
            digit = q % 10   # get last quinary digit
            dec += digit * place
            place *= 5
            q //= 10
        return dec
