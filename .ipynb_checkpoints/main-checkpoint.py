import tkinter as tk
from gui.main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("Loan Interest Calculator")
    root.geometry("800x600")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()