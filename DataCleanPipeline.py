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

# read and run the pipeline
if __name__ == "__main__":
    run_pipeline(
        input_path="WA_Fn-UseC_-Telco-Customer-Churn.csv",
        output_path="telco_churn_cleaned.csv"
    )
