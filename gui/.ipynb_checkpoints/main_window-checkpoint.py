import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utils.interest_calculator import process_customer_data

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        # Input file selection
        input_label = ttk.Label(self.root, text="Input Excel File:")
        input_label.pack(pady=10)

        self.input_entry = ttk.Entry(self.root, width=50)
        self.input_entry.pack(pady=5)

        input_button = ttk.Button(self.root, text="Browse", command=self.browse_input_file)
        input_button.pack(pady=5)

        # Output file selection
        output_label = ttk.Label(self.root, text="Output Excel File:")
        output_label.pack(pady=10)

        self.output_entry = ttk.Entry(self.root, width=50)
        self.output_entry.pack(pady=5)

        output_button = ttk.Button(self.root, text="Browse", command=self.browse_output_file)
        output_button.pack(pady=5)

        # Process button
        process_button = ttk.Button(self.root, text="Process Data", command=self.process_data)
        process_button.pack(pady=20)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def browse_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, file_path)

    def process_data(self):
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()

        if not input_file or not output_file:
            messagebox.showerror("Error", "Please select both input and output files.")
            return

        try:
            process_customer_data(input_file, output_file)
            messagebox.showinfo("Success", f"Data processed and saved to {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")