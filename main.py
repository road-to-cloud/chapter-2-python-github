from calculator import Calculator


def main():
    calculator = Calculator()

    while (True):
        try:
            print(calculator.operation())
        except ValueError:
            print("\nInvalid input, try again\n")


if __name__ == "__main__":
    main()
