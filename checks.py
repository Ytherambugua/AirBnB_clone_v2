#!/usr/bin/python3
# Filename: beautiful_code.py

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            raise ValueError("Cannot divide by zero")

    def get_result(self):
        return self.result


def main():
    calc = Calculator()

    calc.add(5)
    calc.subtract(2)
    calc.multiply(3)
    calc.divide(2)

    result = calc.get_result()

    print(f"Final Result: {result}")


if __name__ == "__main__":
    main()

