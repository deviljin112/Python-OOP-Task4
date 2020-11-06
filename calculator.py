class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @property
    def add(self):
        return self.num_1 + self.num_2

    @property
    def subtract(self):
        return self.num_1 - self.num_2

    @property
    def divide(self):
        return self.num_1 / self.num_2

    @property
    def multiply(self):
        return self.num_1 * self.num_2


def main():
    print("-=CALCULATOR=-")

    try:
        first, second = input(
            "What two numbers would you like to use?\nFormat: NUM NUM\n=>"
        ).split(" ")
    except:
        print("You need to provide two numbers in 'NUM NUM' format!!")
    else:
        if first.isdigit() and second.isdigit():
            first, second = int(first), int(second)

            calc = Calculator(first, second)

            while True:
                choice = input(
                    "What would you like to do?\nAdd / Subtract / Divide / Multiply\n=> "
                )

                if choice.lower() == "add":
                    print(calc.add)
                    break
                elif choice.lower() == "subtract":
                    print(calc.subtract)
                    break
                elif choice.lower() == "divide":
                    print(calc.divide)
                    break
                elif choice.lower() == "multiply":
                    print(calc.multiply)
                    break
                else:
                    print("This option is not available.\nTry again!")

        else:
            print("You need to provide two integer numbers!")


if __name__ == "__main__":
    main()