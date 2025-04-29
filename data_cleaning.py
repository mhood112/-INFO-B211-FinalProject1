import pandas as pd
import numpy as np
import os

# Get the current working directory
current_dir = os.getcwd()

# Dynamically locate the input CSV file in the current directory
input_file_name = "Quality_of_Life.csv"
file_path = os.path.join(current_dir, input_file_name)

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Input file '{input_file_name}' not found in the current directory: {current_dir}")

# Load the CSV file
df = pd.read_csv(file_path)

# Normalize column names: replace spaces with underscores and convert to lowercase
df.columns = df.columns.str.replace(' ', '_').str.lower()

# Remove single quotes from all values in the DataFrame
df.replace(to_replace=r"'", value='', regex=True, inplace=True)

# Replace all 0 values with NaN
df.replace(0, np.nan, inplace=True)

# Remove ':' from the beginning of floats in the 'quality_of_life_value' column
if 'quality_of_life_value' in df.columns:
    df['quality_of_life_value'] = df['quality_of_life_value'].replace(to_replace=r'^:\s*', value='', regex=True)  # Remove leading ':'
    df['quality_of_life_value'] = pd.to_numeric(df['quality_of_life_value'], errors='coerce')  # Ensure numeric

# Drop rows where 'quality_of_life_category' is NaN
if 'quality_of_life_category' in df.columns:
    df = df[df['quality_of_life_category'].notna()]

# Dynamically save the cleaned DataFrame to the current directory
output_file_name = "Cleaned_Quality_of_Life.csv"
cleaned_file_path = os.path.join(current_dir, output_file_name)
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")

