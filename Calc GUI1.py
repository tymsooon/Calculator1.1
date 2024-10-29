import tkinter as tk
from tkinter import ttk, messagebox


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
        for i in range(1, int(self.x) + 1):
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

class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.geometry('370x270')

        self.calculator = Calculator()
        self.input_form = InputForm(self,self.calculator)

        frame = InputForm(self,self.calculator)
        frame.grid(row=0, column=0, sticky="nsew")

class InputForm(ttk.Frame):

    history = []

    def __init__(self,parent,calculator):
        super().__init__(parent)
        self.calculator = calculator

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=1, columnspan= 3)

        self.Label = ttk.Label(self, text="Enter first number:")
        self.Label.grid(row=0, column=0,sticky = "e")

        self.entry2 = ttk.Entry(self)
        self.entry2.grid(row=1, column=1)

        self.Label2 = ttk.Label(self, text="Enter second number:")
        self.Label2.grid(row=1, column=0,sticky = "e")

        self.result_lbl = ttk.Label(self, text="Result:")
        self.result_lbl.grid(row=2, column=0,sticky ='e')

        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self, textvariable=self.result_var)
        self.result_label.grid(row=2, column=1)

        self.operation = ttk.Label(self, text="Please select operation:")
        self.operation.grid(row=3, column=0)

        self.add_btn = ttk.Button(self, text = "Addition",width = 20, command = lambda: self.perform_operations('add'))
        self.add_btn.grid(row=4, column=0, padx=5, pady=5)

        self.clear_btn = ttk.Button(self, text = "Clear",width = 20, command = self.clear_list)
        self.clear_btn.grid(row=3, column=1, padx=5, pady=5)

        self.subtract_btn = ttk.Button(self, text = "Subtraction",width = 20, command = lambda: self.perform_operations('subtract'))
        self.subtract_btn.grid(row=4, column=1, padx=5, pady=5)

        self.multiply_btn = ttk.Button(self, text = "Multiplication",width = 20, command = lambda: self.perform_operations('multiply'))
        self.multiply_btn.grid(row=5, column=0, padx=5, pady=5)

        self.division_btn = ttk.Button(self, text="Division",width = 20,command = lambda: self.perform_operations('divide'))
        self.division_btn.grid(row=5, column=1, padx=5, pady=5)

        self.factorial_btn = ttk.Button(self, text="Factorial",width = 20, command = lambda: self.perform_operations('factorial'))
        self.factorial_btn.grid(row=6, column=0, padx=5, pady=5)

        self.factorial_lbl_btn = ttk.Label(self, text="Factorial is calculated for 1st number")
        self.factorial_lbl_btn.grid(row=7, column=0, padx=5, pady=5)

        self.power_btn = ttk.Button(self, text="Power of Number", width = 20,command = lambda: self.perform_operations('power_of_number'))
        self.power_btn.grid(row=6, column=1, padx=5, pady=5)

        self.modulo_btn = ttk.Button(self, text="Modulo",width = 20, command = lambda:self.perform_operations('modulo'))
        self.modulo_btn.grid(row=7, column=1, padx=5, pady=5,)

    def display_error(self,message):
        messagebox.showerror("Error", "Please input a number")

    def perform_operations(self,operation):
        try:
            x = float(self.entry.get())
            self.calculator.x = x
            if operation in ['add', 'subtract', 'multiply', 'divide','power_of_number', 'modulo']:
                y = float(self.entry2.get())
                self.calculator.y = y
                self.entry2.configure(state = 'normal')
            else:
                x = int(self.entry.get())
                self.entry2.configure(state = 'disabled')
            result = getattr(self.calculator,operation)()
            self.result_var.set(result)
            self.entry2.configure(state = 'normal')


        except ValueError:
            self.display_error("Invalid input, please select a number")

    def clear_list(self):
        self.entry.delete(0, 'end')
        self.entry2.delete(0, "end")

if __name__ == '__main__':
    app = CalculatorGUI()
    app.mainloop()

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

