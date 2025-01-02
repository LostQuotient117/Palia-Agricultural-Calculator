import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Calculator")

#        Labels
        self.labels = {
            "description": "What is the description of the product?",
            "fields": "How many fields should be populated with the product?",
            "production": "How high is the production per field?",
            "price": "What is the selling price per product?",
            "seeds": "How many seeds are produced per product in the seed machine?",
            "time": "How much time in minutes does it take to produce the seeds?"
        }

        self.create_widgets()

    def create_widgets(self):
        self.entries = {}

        for i, (key, text) in enumerate(self.labels.items()):
            label = tk.Label(self.root, text=text)
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

            entry = tk.Entry(self.root, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[key] = entry

        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=len(self.labels), column=0, pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.grid(row=len(self.labels), column=1, pady=10)

    def calculate(self):
        try:
            # Collect inputs
            description = self.entries["description"].get()
            fields = int(self.entries["fields"].get())
            production_per_field = int(self.entries["production"].get())
            price_per_product = int(self.entries["price"].get())
            seeds_per_product = int(self.entries["seeds"].get())
            seed_time = int(self.entries["time"].get())

            # Perform calculations
            one = fields * production_per_field
            two = one - (fields // seeds_per_product)
            three = two * price_per_product
            four = three // seed_time

            # Show results
            results = f"""
            {description}
            Production yield of the fields: {one}
            Minus the products required for seed production: {two}
            Monetary profit from all fields: {three}
            Monetary profit per minute: {four}
            """
            messagebox.showinfo("Calculation Results", results)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
