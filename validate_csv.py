import pandas as pd
def validate_csv(file):
    """Validates the uploaded CSV file format."""
    required_columns = {"Serial Number", "Product Name", "Image URLs"}
    df = pd.read_csv(file)
    if not required_columns.issubset(df.columns):
        return False, "CSV format incorrect. Required columns: Serial Number, Product Name, Image URLs"
    return True, df
