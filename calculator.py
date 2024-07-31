class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return abs(a - b)

    def multiply(self, a, b):
        return a * b

    def divide(self, divisor, dividend):
        if divisor == 0:
            raise ZeroDivisionError
        return dividend / divisor
