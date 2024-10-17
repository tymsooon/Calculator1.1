class Calculator:
    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    def add(self):
        return self.return_round(self.x + self.y)
        
    def multiply(self):
        return self.return_round(self.x * self.y)

    def subtract(self):
        return self.return_round(self.x - self.y)

    def divide(self):
        if self.y == 0:
            print("Division by 0, error")
            return None
        return self.return_round(self.x / self.y)

    def factorial(self):
        if self.x < 0:
            print("Invalid input, please select positive number")
            return None
        result = 1
        for i in range(1, self.x + 1):
            result = result * i
        return self.return_round(result)

    def power_of_number(self):
        if self.x < 0:
            print("Invalid input, please select positive number")
            return None
        return self.return_round(self.x ** self.y)

    def rectangle(self):
        if self.x < 0:
            print("Invalid input, please select positive number")
            return None
        return self.return_round(self.x * self.y)

    def triangle(self):
        if self.x < 0:
            print("Invalid input, please select positive number")
            return None
        return self.return_round(0.5*self.x*self.y)

    def circle(self):
        if self.x < 0:
            print("Invalid input, please select positive number")
            return None
        return self.return_round(3.141592 * self.x**2)

    def modulo(self):
        return self.return_round(self.x % self.y)

    @staticmethod
    def get_number(input_number):
        while True:
            user_input = input(input_number)
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input, please enter a number")
    @staticmethod
    def return_round(value):
        return round(value,2)

    def run(self):

        while True:

            user_choice = input("Please enter your choice (1-8): ")

            if user_choice not in ['1', '2', '3', '4', '5', '6', '7','8']:
                print("Invalid input, please select operation assigned to numbers 1-8")
                continue

            elif user_choice == '5':
                self.x = int(input("Please enter positive number for factorial: "))
                print("You've chosen factorial as operation")
                print (self.return_round(self.factorial()))

            elif user_choice == '7':
                figure_type = input("Please enter type of figure: (Rectangle = 1, Triangle = 2, Circle = 3) ")
                if figure_type not in ['Rectangle', 'Triangle', 'Circle','1','2','3']:
                    print("Invalid input, please enter type of figure type")
                    continue

                if figure_type == 'Rectangle' or  figure_type == '1':
                    self.x = int(input("Please enter length of rectangle in cm: "))
                    self.y = int(input("Please enter width rectangle in cm: "))
                    rectangle_result = self.return_round(self.rectangle())
                    print("The area of this rectangle is " + str(rectangle_result) + "cm^2")

                elif figure_type == 'Triangle' or figure_type == '2':
                    self.x = int(input("Please enter triangle base length in cm: "))
                    self.y = int(input("Please enter triangle height in cm: "))
                    triangle_result = self.return_round(self.triangle())
                    print("The area of this triangle is " + str(triangle_result) + "cm^2")

                elif figure_type == 'Circle' or figure_type == '3':
                    self.x = int(input("Please enter circle radius in cm: "))
                    circle_result = self.return_round(self.circle())
                    print("The area of this circle is " + str(circle_result) + "cm^2")

            else:

                self.x = self.get_number("Please select first number: ")
                self.y = self.get_number("Please select second number: ")

            if user_choice == "1":
                print("You've chosen addition as operation")
                print("The result is",self.add())

            elif user_choice == "2":
                print("You've chosen multiplication as operation")
                print("The result is",self.multiply())

            elif user_choice == "3":
                print("You've chosen subtraction as operation")
                print("The result is",(self.subtract()))

            elif user_choice == "4":
                print("You've chosen divide as operation")
                print("The result is",self.divide())

            elif user_choice == "6":
                print("You've chosen power as operation")
                print("The result is",self.power_of_number())

            elif user_choice == '8':
                print("You've chosen modulo as operation")
                modulo_result = self.modulo()
                print("The remainder of this division is " + str(modulo_result))

            while True:

                another_calculation = input("Do you wish to perform another calculation? (yes/no): ").lower()

                if another_calculation == 'yes':  # do everything here
                    break

                elif another_calculation == 'no':
                    print("Exiting calculator...")
                    return

                else:
                    print("Invalid input, please enter yes or no")

if __name__ == '__main__':

    print("Please select an operation")
    print("1. Add")
    print("2. Multiply")
    print("3. Subtract")
    print("4. Divide")
    print("5. Factorial")
    print("6. Power of a number")
    print("7. Area of figure")
    print("8. Modulo")

    calc = Calculator()
    calc.run()
