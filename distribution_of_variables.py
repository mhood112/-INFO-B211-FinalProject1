import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the cleaned CSV file
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "Cleaned_Quality_of_Life.csv")
df = pd.read_csv(file_path)

# Ensure numeric columns are properly converted
numeric_columns = [
    'purchasing_power_value', 'safety_value', 'health_care_value', 'climate_value',
    'cost_of_living_value', 'property_price_to_income_value', 'traffic_commute_time_value',
    'pollution_value', 'quality_of_life_value'
]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Define unique colors for each plot
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'brown', 'pink']

# Create a directory to save the plots
output_dir = os.path.join(current_dir, "Plots")
os.makedirs(output_dir, exist_ok=True)

# Create the first subplot with 4 graphs
fig, axes = plt.subplots(2, 2, figsize=(15, 10))  # 2 rows, 2 columns
for ax, col, color in zip(axes.flatten(), numeric_columns[:4], colors[:4]):
    sns.histplot(df[col], kde=True, bins=20, color=color, edgecolor='black', ax=ax)
    ax.set_title(f'Distribution of {col.replace("_", " ").title()}', fontsize=12)
    ax.set_xlabel(col.replace("_", " ").title(), fontsize=10)
    ax.set_ylabel('Frequency', fontsize=10)
plt.tight_layout()
plt.suptitle("Subplot 1: Distributions of First 4 Variables", fontsize=16, y=1.02)

# Save the first subplot
subplot_1_path = os.path.join(output_dir, "Subplot_1_Distributions.png")
plt.savefig(subplot_1_path)
print(f"Saved Subplot 1 to {subplot_1_path}")
plt.show()

# Create the second subplot with 1 graph
fig, ax = plt.subplots(figsize=(10, 6))  # Single plot
sns.histplot(df[numeric_columns[4]], kde=True, bins=20, color=colors[4], edgecolor='black', ax=ax)
ax.set_title(f'Distribution of {numeric_columns[4].replace("_", " ").title()}', fontsize=16)
ax.set_xlabel(numeric_columns[4].replace("_", " ").title(), fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.suptitle("Subplot 2: Distribution of Fifth Variable", fontsize=16, y=1.02)

# Save the second subplot
subplot_2_path = os.path.join(output_dir, "Subplot_2_Distribution.png")
plt.savefig(subplot_2_path)
print(f"Saved Subplot 2 to {subplot_2_path}")
plt.show()

# Describe the distributions
summary_statistics = df[numeric_columns].describe()

# Save the summary statistics to a CSV file
output_file_path = os.path.join(current_dir, "Numeric_Variables_Summary.csv")
summary_statistics.to_csv(output_file_path)
print(f"Summary statistics saved to {output_file_path}")

