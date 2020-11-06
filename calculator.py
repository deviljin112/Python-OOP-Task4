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

    @property
    def divisible(self):
        if self.num_1 % self.num_2 == 0:
            return True
        else:
            return False

    @property
    def triangle(self):
        area = (self.num_1 * self.num_2) / 2
        return area

    @property
    def converter(self):
        rate = 2.54

        if self.num_1 != 0:
            return self.num_1 * rate
        elif self.num_2 != 0:
            return self.num_2 / rate


def main():
    print("-=CALCULATOR=-")

    try:
        first, second = input(
            "What two numbers would you like to use?\nFormat: NUM NUM\nFor conversion use first NUM for cm to inch, or second for inch to cm\nUse 0 for the number you dont want to convert\n=>"
        ).split(" ")
    except:
        print("You need to provide two numbers in 'NUM NUM' format!!")
    else:
        if first.isdigit() and second.isdigit():
            first, second = int(first), int(second)

            calc = Calculator(first, second)

            while True:
                choice = input(
                    "What would you like to do?\nAdd / Subtract / Divide / Multiply / Divisible / Triangle / Converter\n=> "
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
                elif choice.lower() == "divisible":
                    print(calc.divisible)
                    break
                elif choice.lower() == "trianlge":
                    print(calc.triangle)
                    break
                elif choice.lower() == "converter":
                    print(calc.converter)
                    break
                else:
                    print("This option is not available.\nTry again!")

        else:
            print("You need to provide two integer numbers!")


if __name__ == "__main__":
    main()