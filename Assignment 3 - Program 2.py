import tkinter as tk
from tkinter import messagebox

class apple_and_money(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Assignment 3 - Program 2 :)")

        # Left Side of the Window
        self.left_frame = tk.Frame(self, bg="#CAE1FF", width=400, height=200)
        self.left_frame.pack(side="left", fill="both", expand=True)
        
        # Right Side of the Window
        self.right_frame = tk.Frame(self, bg="#CAE1FF", width=200, height=100)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Widgets

        # Input Label and Entry
        self.apples_and_money_label = tk.Label(self.left_frame, text="Apples and Money", bg="white", font=("20"))
        self.apples_and_money_label.pack(padx=10, pady=10)
        
        self.amount_of_money = tk.Label(self.left_frame, bg="white", text="How much money do you have?")
        self.amount_of_money.pack(padx=10, pady=10)
        
        self.money_entry = tk.Entry(self.left_frame)
        self.money_entry.pack(padx=10, pady=10)
        
        self.price_of_apple = tk.Label(self.left_frame, bg="white", text="What is the price of an apple?")
        self.price_of_apple.pack(padx=10, pady=10)
        
        self.apple_price_entry = tk.Entry(self.left_frame)
        self.apple_price_entry.pack(padx=10, pady=10)
        
        self.total_cost_label = tk.Label(self.right_frame, text="Maximum Apples and Remaining Money:", bg="white", font=("20"))
        self.total_cost_label.pack(padx=10, pady=10)
         
        self.total_cost_text = tk.Text(self.right_frame)
        self.total_cost_text.pack(padx=10, pady=10)

        # Buttons
        self.calculate_button = tk.Button(self.left_frame, text="Calculate", command=self.calculate)
        self.calculate_button.pack(padx=10, pady=10)
        
        #Validation
    def validate_input(self, P):
        if P.isalpha() or P.isspace():
            messagebox.showerror("Error", "Invalid input. Please enter only numbers.")
            return False
        return True
        
    def calculate(self):
        if not self.validate_input(self.money_entry.get()) or not self.validate_input(self.apple_price_entry.get()):
            return
        
        money = int(self.money_entry.get())
        apple_price = int(self.apple_price_entry.get())
        max_apples = money // apple_price
        remaining_money = money % apple_price
        output = "Maximum Apples: " + str(max_apples) + "\nRemaining Money: " + str(remaining_money) + " Pesos"
        self.total_cost_text.delete(1.0, "end")
        self.total_cost_text.insert("end", output)
        
app = apple_and_money()
app.mainloop()