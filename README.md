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
