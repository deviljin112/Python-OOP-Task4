import os

os.system("color")


class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    @property
    def add(self):
        answer = 0
        for i in self.numbers:
            answer += i
        return answer

    @property
    def subtract(self):
        answer = self.numbers[0]
        for i in self.numbers:
            answer -= i
        return answer

    @property
    def divide(self):
        answer = self.numbers[0]
        for i in self.numbers:
            answer /= i
        return answer

    @property
    def multiply(self):
        answer = self.numbers[0]
        for i in self.numbers:
            answer *= i
        return answer

    @property
    def modulus(self):
        return self.numbers[0] % self.numbers[1]

    @property
    def power(self):
        return self.numbers[0] ** self.numbers[1]

    @property
    def divisible(self):
        if self.numbers[0] % self.numbers[1] == 0:
            return True
        else:
            return False

    @property
    def triangle(self):
        area = (self.numbers[0] * self.numbers[1]) / 2
        return area

    def converter(self, choice):
        rate = 2.54

        if choice == "cm":
            return self.numbers[0] * rate
        elif choice == "inch":
            return self.numbers[0] / rate


options = ["add", "subtract", "divide", "multiply"]
options_2 = ["modulus", "power", "triangle", "divisible"]
options_3 = ["convert"]

END = "\033[0m"
RED = "\033[91m"
CYAN = "\033[96m"


def main():
    print(CYAN, "-=CALCULATOR=-", END)

    print(
        f"""
What would you like to do?

Multi digit operations: {RED}{", ".join(options).title()}{END}
Two digit operations: {RED}{", ".join(options_2).title()}{END}
Single digit operations: {RED}{", ".join(options_3).title()}{END}

NOTE: Subtraction and Division will use the first number
        as the base for its operations.

"""
    )

    choice = input("=> ")

    if choice.lower() in options:
        print(f"Please input your numbers.\nFormat: {CYAN}NUM NUM NUM ... NUM{END}")
        numbers = input("=> ").split(" ")

        if len(numbers) > 1:
            can_continue = True
            for i in range(len(numbers)):
                if numbers[i].isdigit():
                    numbers[i] = int(numbers[i])
                else:
                    can_continue = False
                    break

            if can_continue:
                calc = Calculator(numbers)

                if choice.lower() == "add":
                    print(f"Answer is: {CYAN}{calc.add}{END}")
                elif choice.lower() == "subtract":
                    print(f"Answer is: {CYAN}{calc.subtract}{END}")
                elif choice.lower() == "multiply":
                    print(f"Answer is: {CYAN}{calc.multiply}{END}")
                elif choice.lower() == "divide":
                    print(f"Answer is: {CYAN}{calc.divide}{END}")

            else:
                print(f"You need to provide an {RED}INTEGER{END}")
        else:
            print(f"You need to input more than {RED}1{END} number")

    elif choice.lower() in options_2:
        print(f"Please input 2 numbers.\nFormat: {CYAN}NUM NUM{END}")
        numbers = input("=> ").split(" ")

        if len(numbers) == 2:
            if numbers[0].isdigit() and numbers[1].isdigit():
                first, second = int(numbers[0]), int(numbers[1])

                calc = Calculator([first, second])

                if choice.lower() == "divisible":
                    print(f"Answer is: {CYAN}{calc.divisible}{END}")
                elif choice.lower() == "triangle":
                    print(f"Answer is: {CYAN}{calc.triangle}{END}")
                elif choice.lower() == "power":
                    print(f"Answer is: {CYAN}{calc.power}{END}")
                elif choice.lower() == "modulus":
                    print(f"Answer is: {CYAN}{calc.modulus}{END}")

            else:
                print(f"Please provide an {RED}INTEGER{END}")
        else:
            print(f"Please provide {RED}TWO{END} numbers.")

    elif choice.lower() in options_3:
        print("Would you like to convert cm to inch or inch to cm?")
        choice2 = input(
            f"Options:\n {CYAN}'cm'{END} to inch\n {CYAN}'inch'{END} to cm.\n=> "
        )
        if choice2.lower() == "cm" or choice2.lower() == "inch":
            number = input("Please provide the number to convert.\n=> ")

            if number.isdigit():
                number = int(number)
                calc = Calculator([number])

                if choice2.lower() == "cm":
                    print(f"Answer is: {CYAN}{calc.converter('cm')}{END}")
                elif choice2.lower() == "inch":
                    print(f"Answer is: {CYAN}{calc.converter('inch')}{END}")
            else:
                print(f"Please provide a single {RED}INTEGER{END}")
        else:
            print(f"That's not an options.\n{RED}Please try again!{END}")

    else:
        print(f"That's not an options.\n{RED}Please try again!{END}")


if __name__ == "__main__":
    main()