import pandas as pd
import requests


def display_categorical_values(df: pd.DataFrame) -> None:
    """Display the unique values and their counts for a categorical column in a DataFrame."""
    for column in df.select_dtypes(include=['object', 'category']).columns:
        print(f"Column: {column}, Unique Values: {df[column].unique()}")


def download_file(url: str, destination: str) -> None:
    """Download a file from a URL to a local destination."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File downloaded to {destination}")

