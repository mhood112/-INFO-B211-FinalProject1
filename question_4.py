import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import os
import matplotlib.pyplot as plt

# Dynamically locate the cleaned CSV file
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "Cleaned_Quality_of_Life.csv")

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Input file 'Cleaned_Quality_of_Life.csv' not found in the current directory: {current_dir}")

# Load the dataset
df = pd.read_csv(file_path)

# Ensure relevant columns are numeric
columns_to_convert = [
    'purchasing_power_value', 'safety_value', 'health_care_value', 'traffic_commute_time_value',
    'pollution_value', 'cost_of_living_value'
]
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values in the relevant columns
df = df.dropna(subset=columns_to_convert + ['cost_of_living_category'])

# Analyze class distribution
print("Class Distribution in the Dataset (Before Filtering):")
print(df['cost_of_living_category'].value_counts())

# Remove classes with fewer than two samples
class_counts = df['cost_of_living_category'].value_counts()
valid_classes = class_counts[class_counts >= 2].index
df = df[df['cost_of_living_category'].isin(valid_classes)]

print("\nClass Distribution in the Dataset (After Filtering):")
print(df['cost_of_living_category'].value_counts())

# Encode the target variable (Cost of Living Category)
label_encoder = LabelEncoder()
df['cost_of_living_category_encoded'] = label_encoder.fit_transform(df['cost_of_living_category'])

# Define features and target
X = df[['purchasing_power_value', 'safety_value', 'health_care_value', 'traffic_commute_time_value', 'pollution_value']]
y = df['cost_of_living_category_encoded']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")

# Ensure all classes are included in the classification report
all_classes = label_encoder.transform(label_encoder.classes_)  # Get all encoded class labels
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=all_classes,
        target_names=label_encoder.classes_,
        zero_division=0  # Handle undefined precision/recall by setting them to 0
    )
)



# Feature importance analysis
feature_importances = model.feature_importances_
feature_names = X.columns
print("\nFeature Importances:")
for name, importance in zip(feature_names, feature_importances):
    print(f"{name}: {importance:.4f}")

# Visualization of feature importances
plt.figure(figsize=(10, 6))
bars = plt.barh(feature_names, feature_importances, color='skyblue')

# Add numerical values inside the bars
for bar, importance in zip(bars, feature_importances):
    plt.text(
        bar.get_width() - 0.02,  # Position slightly to the left of the bar's end
        bar.get_y() + bar.get_height() / 2,  # Center vertically
        f"{importance:.4f}",  # Format the number to 4 decimal places
        va='center',  # Align vertically
        ha='right',  # Align horizontally to the right
        color='black',  # Use white text for better contrast
        fontsize=10  # Font size
    )

plt.xlabel('Feature Importance', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.title('Feature Importances in RandomForestClassifier', fontsize=16)
plt.tight_layout()

# Save the plot
output_dir = os.path.join(current_dir, "Plots")
os.makedirs(output_dir, exist_ok=True)
plot_path = os.path.join(output_dir, "Feature_Importances_With_Values_Inside.png")
plt.savefig(plot_path)
print(f"\nFeature importance plot with values saved to {plot_path}")

# Show the plot
plt.show()