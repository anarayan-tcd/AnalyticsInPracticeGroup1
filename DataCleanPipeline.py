"""
Purpose: Load, clean, and transform raw data, output one cleaned CSV
         for downstream analysis.
"""

import pandas as pd


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

# read and run the pipeline
if __name__ == "__main__":
    run_pipeline(
        input_path="WA_Fn-UseC_-Telco-Customer-Churn.csv",
        output_path="telco_churn_cleaned.csv"
    )
