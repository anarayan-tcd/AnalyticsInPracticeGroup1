"""
Purpose: Load, clean, and transform raw data, output one cleaned CSV
         for downstream analysis.
"""

import pandas as pd
import numpy as np

# Load Data & Check for Duplicates
def load_and_check(filepath: str) -> pd.DataFrame:
    """Read raw CSV and check for duplicate rows or duplicate customer IDs."""
    df = pd.read_csv(filepath)
    print(f"Data loaded: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(f"Duplicate customerIDs: {df['customerID'].duplicated().sum()}")
    return df

# Fix Data Types
def fix_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert to float, fill blanks with 0.0.
    """
    df = df.copy()
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    n_blank = df['TotalCharges'].isnull().sum()
    df['TotalCharges'] = df['TotalCharges'].fillna(0.0)
    print(f"TotalCharges: converted to float, filled {n_blank} blanks with 0.0")
    return df

# Standardize Category Values
def standardize_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    1. Replace "No internet service" and "No phone service" with "No"
    2. Convert all Yes/No columns to 1/0 (SeniorCitizen is already 1/0, skip it)
    """
    df = df.copy()
    # Unify "No internet service" / "No phone service" → "No"
    internet_cols = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    for col in internet_cols:
        df[col] = df[col].replace('No internet service', 'No')

    df['MultipleLines'] = df['MultipleLines'].replace('No phone service', 'No')
    print("Replaced 'No internet service' / 'No phone service' with 'No'")

    # Convert all Yes/No columns → 1/0
    yes_no_cols = [
        'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies',
        'PaperlessBilling', 'Churn'
    ]
    for col in yes_no_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})

    print(f"Converted {len(yes_no_cols)} Yes/No columns to 1/0")
    # Note: gender, InternetService, Contract, PaymentMethod are multi-value columns, kept as-is
    # Note: SeniorCitizen is already 0/1, no change needed
    return df

# Add New Feature
def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add has_streaming column:
    If StreamingTV = 1 OR StreamingMovies = 1, then has_streaming = 1.
    Used to answer Q3: "Do customers who use streaming services churn less?"
    """
    df = df.copy()
    df['has_streaming'] = np.where(
        (df['StreamingTV'] == 1) | (df['StreamingMovies'] == 1),
        1, 0
    )
    print("Added new feature: has_streaming")
    return df

# Save Cleaned CSV
def save_cleaned(df: pd.DataFrame, output_path: str):
    """Save the cleaned dataframe to CSV """
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data → {output_path}")

# Pipeline Runner
def run_pipeline(input_path: str, output_path: str):
    """Run the entire data cleaning workflow in one call."""
    print("Starting Data Engineering Pipeline...\n")

    df = load_and_check(input_path)
    df = fix_dtypes(df)
    df = standardize_categories(df)
    df = add_features(df)
    save_cleaned(df, output_path)

    print(f"\n Pipeline complete! Final data: {df.shape[0]} rows × {df.shape[1]} columns")
    return df

# read and run the pipeline
if __name__ == "__main__":
    run_pipeline(
        input_path="WA_Fn-UseC_-Telco-Customer-Churn.csv",
        output_path="telco_churn_cleaned.csv"
    )
