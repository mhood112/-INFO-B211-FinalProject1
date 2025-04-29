# -INFO-B211-FinalProject1

## Project Overview

This project aims to analyze and provide insights into global quality of life indicators using data from the Quality_of_Life.csv dataset. The analysis focuses on healthcare, cost of living, purchasing power, and other socio-economic factors. The project includes data cleaning, exploratory data analysis, and predictive modeling to answer key analytical questions.

---

## Key Analytical Questions

  1. Healthcare Analysis
     - Identify which countries possess varying levels of healthcare and assess their quality.
  2. Quality of Life Comparison
     - Compare the country with the lowest quality of life against the one with the highest to determine key differentiating factors.
  3. Purchasing Power vs. Cost of Living
     - Analyze how the relationship between purchasing power and cost of living influences the overall quality of life across different countries.
  4. Predictive Modeling
     - Can we predict the cost of living category from other indicators

---

## Files in the Project

  1. Quality_of_Life.csv:
    - The raw dataset containing global quality of life indicators.

  2. Cleaned_Quality_of_Life.csv:
    - The cleaned version of the dataset after handling missing values, converting data types, and filtering invalid entries.

  3. data_cleaning.py:
    - A script for cleaning and preprocessing the raw dataset. It includes:
          - Handling missing values.
          - Converting columns to appropriate data types.
          - Filtering out invalid or incomplete rows.
     
  4. distribution_of_variables.py:
     - A script for visualizing the distribution of key variables in the dataset. It includes:
          - Histograms for numeric variables.
          - Box plots for categorical comparisons.

  5. question_1.py:
     - Analyzes healthcare levels across countries and assesses their quality.
     - Includes visualizations and summary statistics.
     
  6. question_2.py:
     - Compares the country with the lowest quality of life against the one with the highest.
     - Identifies key differentiating factors using statistical and visual analysis.

  7. question_3.py:
     - Explores the relationship between purchasing power and cost of living.
     - Uses scatter plots and correlation analysis to understand their influence on quality of life.

  8. question_4.py:
     - Builds a predictive model to classify the cost of living category based on other indicators.
          - Includes:
                - Data preprocessing.
                - Model training using RandomForestClassifier.
                - Feature importance visualization.

---

## Class Design and Implementation

The project is modular, with each script focusing on a specific aspect of the analysis. Below is an explanation of the key components:

1. data_cleaning.py:
 - **Attributes:**
      - file_path: Path to the raw dataset.
 - **Methods:**
      - clean_data(): Cleans the dataset by handling missing values and converting data types.

2. distribution_of_variables.py:
  - **Attributes:**
      - numeric_columns: List of numeric columns to visualize.
  - **Methods:**
      - plot_histograms(): Generates histograms for numeric variables.
      - plot_boxplots(): Creates box plots for categorical comparisons.

3. question_1.py:
  - **Attributes:**
      - healthcare_column: Column representing healthcare levels.
  - **Methods:**
      - analyze_healthcare(): Analyzes healthcare levels and generates visualizations.

4. question_2.py:
  - **Attributes:**
     - quality_of_life_column: Column representing quality of life scores.
  - **Methods:**
     - compare_countries(): Compares the highest and lowest quality of life countries.

5. question_3.py:
  - **Attributes:**
      - purchasing_power_column: Column representing purchasing power.
      - cost_of_living_column: Column representing cost of living.
  - **Methods:**
      - analyze_relationship(): Explores the relationship between purchasing power and cost of living.

6. question_4.py:
  - **Attributes:**
      - features: List of features used for prediction.
      - target: Target variable (cost_of_living_category).
  - **Methods:**
      - train_model(): Trains a RandomForestClassifier to predict the cost of living category.
      - visualize_feature_importances(): Visualizes feature importances.
      - 
---

### Outputs:
  - Cleaned dataset: Cleaned_Quality_of_Life.csv.
  - Visualizations: Saved in the Plots directory.
  - Analytical insights: Printed in the terminal and saved as plots.

---

## Limitations
 - Data Quality:
    - The analysis depends on the accuracy and completeness of the input dataset.
 - Model Generalization:
   - The predictive model may not generalize well to unseen data if the dataset is imbalanced or limited in size.

---
## Conclusion
This project provides valuable insights into global quality of life indicators by analyzing healthcare, cost of living, purchasing power, and other socio-economic factors. Below are the key takeaways:

1. Healthcare Analysis:
Countries with higher healthcare scores tend to have better overall quality of life. However, healthcare alone is not the sole determinant, as other factors like safety and pollution also play significant roles.

2. Quality of Life Comparison:
The comparison between the country with the lowest quality of life and the one with the highest revealed stark differences in purchasing power, healthcare, and safety. These factors are critical in shaping the overall quality of life.

3. Purchasing Power vs. Cost of Living:
A strong correlation was observed between purchasing power and cost of living. Countries with higher purchasing power generally have a higher quality of life, but this relationship is influenced by other factors like pollution and commute times.

4. Predictive Modeling:
The RandomForestClassifier achieved a high accuracy in predicting the cost of living category based on other indicators. The most important features identified were:
Purchasing Power Value
Safety Value
Healthcare Value
The feature importance analysis highlights the key drivers of cost of living, providing actionable insights for policymakers and researchers.

5. Visualization:
The feature importance plot provides a clear understanding of which factors contribute most to the model's predictions, making the results interpretable and actionable.

