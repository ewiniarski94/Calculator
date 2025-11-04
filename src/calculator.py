class Calculator:
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self):
        return self.__op1 + self.__op2

    def subtract(self):
        return self.__op1 - self.__op2

    def multiply(self):
        return self.__op1 * self.__op2

    def divide(self):
        if self.__op2 == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        return self.__op1 / self.__op2

if __name__ == "__main__":
    calculator = Calculator(op1=5.5, op2=4)
    print(calculator.sum())
    print(calculator.subtract())
    print(calculator.multiply())
    print(calculator.divide())

