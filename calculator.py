from typing import Union
from operations import addition, subtraction, multiplication, division


class Calculator():

    def input_equation(self) -> Union[str, str, str]:
        equation: str = input("Enter an equation:\n")
        return equation.split(" ")

    def interprete_equation(self, equation: str) -> Union[float, str, float]:
        a = int(equation[0])
        b = int(equation[2])
        operator = equation[1]
        return [a, operator, b]

    def operation(self) -> str:
        operation: Union[str, str, str] = self.input_equation()

        print(f"Calculating: {' '.join(operation)} ...")
        a, operand, b = self.interprete_equation(operation)

        match operand:
            case "+":
                return f"{a} + {b} = {addition(a, b)}"
            case "-":
                return f"{a} - {b} = {subtraction(a, b)}"
            case "*":
                return f"{a} * {b} = {multiplication(a, b)}"
            case "/":
                return f"{a} / {b} = {division(a, b)}"
            case _:
                return "Invalid operator"
