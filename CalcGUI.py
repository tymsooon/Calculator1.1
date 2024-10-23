import tkinter as tk
from tkinter import ttk


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

            user_choice = input("Please enter your choice (1-7): ")

            if user_choice not in ['1', '2', '3', '4', '5', '6', '7']:
                print("Invalid input, please select operation assigned to numbers 1-7")
                continue

            elif user_choice == '5':
                self.x = int(input("Please enter positive number for factorial: "))
                print("You've chosen factorial as operation")
                print (self.return_round(self.factorial()))

            # elif user_choice == '7':
            #     figure_type = input("Please enter type of figure: (Rectangle = 1, Triangle = 2, Circle = 3) ")
            #     if figure_type not in ['Rectangle', 'Triangle', 'Circle','1','2','3']:
            #         print("Invalid input, please enter type of figure type")
            #         continue

                # if figure_type == 'Rectangle' or  figure_type == '1':
                #     self.x = int(input("Please enter length of rectangle in cm: "))
                #     self.y = int(input("Please enter width rectangle in cm: "))
                #     rectangle_result = self.return_round(self.rectangle())
                #     print("The area of this rectangle is " + str(rectangle_result) + "cm^2")
                #
                # elif figure_type == 'Triangle' or figure_type == '2':
                #     self.x = int(input("Please enter triangle base length in cm: "))
                #     self.y = int(input("Please enter triangle height in cm: "))
                #     triangle_result = self.return_round(self.triangle())
                #     print("The area of this triangle is " + str(triangle_result) + "cm^2")
                #
                # elif figure_type == 'Circle' or figure_type == '3':
                #     self.x = int(input("Please enter circle radius in cm: "))
                #     circle_result = self.return_round(self.circle())
                #     print("The area of this circle is " + str(circle_result) + "cm^2")


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

            elif user_choice == '7':
                print("You've chosen modulo as operation")
                modulo_result = self.modulo()
                print("The remainder of this division is " + str(modulo_result))


            while True:

                another_calculation = input("Do you wish to perform another calculation? (yes/no): ").lower()

                if another_calculation == 'yes':
                    break

                elif another_calculation == 'no':
                    print("Exiting calculator...")
                    return

                else:
                    print("Invalid input, please enter yes or no")

def main():
    app = CalculatorGUI()
    app.mainloop()


class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.geometry('320x300')

        self.calculator = Calculator()
        self.input_form = InputForm(self,self.calculator)

        frame = InputForm(self,self.calculator)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

class InputForm(ttk.Frame):
    def __init__(self,parent, calculator):
        super().__init__(parent)
        self.calculator = calculator

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=1)

        self.Label = ttk.Label(self, text="Enter first number:")
        self.Label.grid(row=0, column=0)

        self.entry2 = ttk.Entry(self)
        self.entry2.grid(row=1, column=1)

        self.Label2 = ttk.Label(self, text="Enter second number:")
        self.Label2.grid(row=1, column=0)

        self.result = ttk.Label(self, text="Result:")
        self.result.grid(row=2, column=0)

        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self, textvariable=self.result_var)
        self.result_label.grid(row=2, column=1)

        self.operation = ttk.Label(self, text="Please select operation:")
        self.operation.grid(row=3, column=0)

        self.add_btn = ttk.Button(self, text = "Addition", command = self.addition)
        self.add_btn.grid(row=4, column=0, padx=5, pady=5)

        self.subtract_btn = ttk.Button(self, text = "Subtraction", command = self.subtraction)
        self.subtract_btn.grid(row=4, column=1, padx=5, pady=5)

        self.multiply_btn = ttk.Button(self, text = "Multiplication", command = self.multiply)
        self.multiply_btn.grid(row=5, column=0, padx=5, pady=5)

        self.division_btn = ttk.Button(self, text="Division", command=self.division)
        self.division_btn.grid(row=5, column=1, padx=5, pady=5)

        self.factorial_btn = ttk.Button(self, text="Factorial", command=self.factorial)
        self.factorial_btn.grid(row=6, column=0, padx=5, pady=5)

        self.factorial_btn = ttk.Button(self, text="Power of Number", command=self.power_of_number)
        self.factorial_btn.grid(row=6, column=1, padx=5, pady=5)

        self.modulo_btn = ttk.Button(self, text="Modulo", command=self.modulo)
        self.modulo_btn.grid(row=7, column=1, padx=5, pady=5,)

    def addition(self):
        try:
            x = float(self.entry.get())
            y = float(self.entry2.get())
            self.calculator.x = x
            self.calculator.y = y
            result = self.calculator.add()
            self.result_var.set(result)
            self.entry2.configure(state="normal")
        except ValueError:
            print("Invalid input, please enter a number")

    def subtraction(self):
        try:
            x = float(self.entry.get())
            y = float(self.entry2.get())
            self.calculator.x = x
            self.calculator.y = y
            result = self.calculator.subtract()
            self.result_var.set(result)
            self.entry2.configure(state="normal")
        except ValueError:
            print("Invalid input, please enter a number")

    def multiply(self):
        try:
            x = float(self.entry.get())
            y = float(self.entry2.get())
            self.calculator.x = x
            self.calculator.y = y
            result = self.calculator.multiply()
            self.result_var.set(result)
            self.entry2.configure(state="normal")
        except ValueError:
            print("Invalid input, please enter a number")
    def division(self):
        try:
            x = float(self.entry.get())
            y = float(self.entry2.get())
            self.calculator.x = x
            self.calculator.y = y
            result = self.calculator.divide()
            self.result_var.set(result)
            self.entry2.configure(state="normal")
        except ValueError:
            print("Invalid input, please enter a number")

    def factorial(self):
        try:
            x = int(self.entry.get())
            self.calculator.x = x
            result = self.calculator.factorial()
            self.result_var.set(result)
            self.entry2.configure(state = "disabled")
        except ValueError:
            print("Invalid input, please enter a number")

    def power_of_number(self):
        try:
            x = float(self.entry.get())
            y = float(self.entry2.get())
            self.calculator.x = x
            self.calculator.y = y
            result = self.calculator.power_of_number()
            self.result_var.set(result)
            self.entry2.configure(state="normal")
        except ValueError:
            print("Invalid input, please enter a number")

    def modulo(self):
        try:
            x = float(self.entry.get())
            y = float(self.entry2.get())
            self.calculator.x = x
            self.calculator.y = y
            result = self.calculator.modulo()
            self.result_var.set(result)
            self.entry2.configure(state="normal")
        except ValueError:
            print("Invalid input, please enter a number")


if __name__ == '__main__':
    main()

    print("Please select an operation")
    print("1. Add")
    print("2. Multiply")
    print("3. Subtract")
    print("4. Divide")
    print("5. Factorial")
    print("6. Power of a number")
    print("7. Modulo")

    calc = Calculator()
    calc.run()

