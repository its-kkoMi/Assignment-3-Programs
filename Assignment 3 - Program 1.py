import tkinter as tk
from tkinter import messagebox

class apple_and_orange(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Assignment 3 - Program 1 :)")

        # Left Side of the Window
        self.left_frame = tk.Frame(self, bg="#CAE1FF", width=400, height=200)
        self.left_frame.pack(side="left", fill="both", expand=True)
        
        # Right Side of the Window
        self.right_frame = tk.Frame(self, bg="#CAE1FF", width=200, height=100)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Widgets

        # Input Label and Entry
        self.apples_and_oranges_label = tk.Label(self.left_frame, text="Apples and Oranges", bg="white", font=("20"))
        self.apples_and_oranges_label.pack(padx=10, pady=10)
        
        self.amount_of_apples = tk.Label(self.left_frame, bg="white", text="How many apples will you buy? (20 Pesos)")
        self.amount_of_apples.pack(padx=10, pady=10)
        
        self.apple_entry = tk.Entry(self.left_frame)
        self.apple_entry.pack(padx=10, pady=10)
        
        self.amount_of_oranges = tk.Label(self.left_frame, bg="white", text="How many oranges will you buy? (25 Pesos)")
        self.amount_of_oranges.pack(padx=10, pady=10)
        
        self.orange_entry = tk.Entry(self.left_frame)
        self.orange_entry.pack(padx=10, pady=10)
        
        self.total_cost_label = tk.Label(self.right_frame, text="Total Cost:", bg="white", font=("20"))
        self.total_cost_label.pack(padx=10, pady=10)
         
        self.total_cost_text = tk.Text(self.right_frame)
        self.total_cost_text.pack(padx=10, pady=10)

        # Buttons
        self.calculate_button = tk.Button(self.left_frame, text="Calculate", command=self.calculate)
        self.calculate_button.pack(padx=10, pady=10)
        
        #Validation
    def validate_input(self, P):
        if P == "" or P.isalpha() or P.isspace():
            messagebox.showerror("Error", "Invalid input. Please enter only numbers.")
            return False
        return True
        
    def calculate(self):
        if not self.validate_input(self.apple_entry.get()) or not self.validate_input(self.orange_entry.get()):
            return    
        
        apples = int(self.apple_entry.get())
        oranges = int(self.orange_entry.get())
        total_cost = (apples * 20) + (oranges * 25)
        output = "Total Cost: " + str(total_cost) + " Pesos"
        self.total_cost_text.delete(1.0, "end")
        self.total_cost_text.insert("end", output)
        
app = apple_and_orange()
app.mainloop()