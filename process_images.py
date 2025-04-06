import os
import requests
from PIL import Image
from io import BytesIO
from pyspark.sql import SparkSession

def download_and_compress_image(image_url, output_path):
    """Downloads an image and compresses it by 50%."""
    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = img.convert("RGB")
        output_size = (img.width // 2, img.height // 2)
        img = img.resize(output_size)
        img.save(output_path, "JPEG", quality=85)
        return output_path
    return None