import pandas as pd
file_path='data.xlsx'
def load_data(file_path):
    """
    Read data from Excel file.

    Parameters:
    - file_path (str): Path to the Excel file.

    Returns:
    - DataFrame or None: DataFrame containing the data, or None if an error occurs.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading data from '{file_path}': {e}")
        return None
