import tkinter as tk
from tkinter import ttk

class CustomButton(ttk.Button):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(style="Custom.TButton")