import pandas as pd

def read_excel(file_path):
    """Reads an Excel file and returns a DataFrame."""
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        raise Exception(f"Failed to read Excel file: {e}")