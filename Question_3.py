import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "Cleaned_Quality_of_Life.csv")
df = pd.read_csv(file_path)


# Ensure relevant columns are numeric
columns_to_convert = ['purchasing_power_value', 'cost_of_living_value', 'quality_of_life_value']
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values in the relevant columns
df = df.dropna(subset=columns_to_convert)

# Reorder the 'quality_of_life_category' column to have 'Very Low' before 'Low'
if 'quality_of_life_category' in df.columns:
    category_order = ['Very Low', 'Low', 'Moderate', 'High', 'Very High']
    df['quality_of_life_category'] = pd.Categorical(df['quality_of_life_category'], categories=category_order, ordered=True)

# Calculate correlation matrix
correlation_matrix = df[['purchasing_power_value', 'cost_of_living_value', 'quality_of_life_value']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Visualize the relationships using scatter plots with color based on 'quality_of_life_category'
sns.pairplot(
    df,
    vars=['purchasing_power_value', 'cost_of_living_value', 'quality_of_life_value'],
    kind='reg',
    hue='quality_of_life_category',  # Add color based on this column
    palette='Set1'  # Use a more distinguishable color palette
)
plt.suptitle("Scatter Plots of Purchasing Power, Cost of Living, and Quality of Life", y=1.02)
plt.show()

