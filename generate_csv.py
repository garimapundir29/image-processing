import pandas as pd

def generate_sample_csv(filename="sample_products.csv"):
    """Generates a sample CSV file with product names and image URLs."""
    data = {
        "Serial Number": [1, 2, 3],
        "Product Name": ["Laptop", "Smartphone", "Headphones"],
        "Image URLs": [
            "https://example.com/laptop.jpg",
            "https://example.com/smartphone.jpg",
            "https://example.com/headphones.jpg"
        ]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return filename