class Calculator:
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self):
        return self.__op1 + self.__op2

    def substract(self):
        return self.__op1 - self.__op2

    def multiply(self):
        return self.__op1 * self.__op2

    def divide(self):
        try:
            result = self.__op1 / self.__op2
            return result
        except ZeroDivisionError:
            print("Division Error: cannot divide by zero.")
            return None

if __name__ == "__main__":
    calculator = Calculator(op1=0, op2=2)
    print(calculator.divide())


