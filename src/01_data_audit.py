from pathlib import Path

import pandas as pd


# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_ROOT / "data" / "measures_v2.csv"


print("=" * 60)
print("MOTOR RPM PREDICTION — DATA AUDIT")
print("=" * 60)

print(f"\nDataset path:")
print(DATA_PATH)

print(f"\nDataset exists: {DATA_PATH.exists()}")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"\nDataset not found:\n{DATA_PATH}"
    )


# Load dataset
print("\nLoading dataset...")
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")


# --------------------------------------------------
# Basic dimensions
# --------------------------------------------------

print("\n" + "=" * 60)
print("1. DATASET SHAPE")
print("=" * 60)

rows, columns = df.shape

print(f"Rows:    {rows:,}")
print(f"Columns: {columns}")


# --------------------------------------------------
# Column names
# --------------------------------------------------

print("\n" + "=" * 60)
print("2. COLUMNS")
print("=" * 60)

for i, column in enumerate(df.columns, start=1):
    print(f"{i:2}. {column}")


# --------------------------------------------------
# Data types
# --------------------------------------------------

print("\n" + "=" * 60)
print("3. DATA TYPES")
print("=" * 60)

print(df.dtypes)


# --------------------------------------------------
# Missing values
# --------------------------------------------------

print("\n" + "=" * 60)
print("4. MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum()

print(missing)

print(
    f"\nTotal missing values: {missing.sum():,}"
)


# --------------------------------------------------
# Duplicate rows
# --------------------------------------------------

print("\n" + "=" * 60)
print("5. DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()

print(f"Duplicate rows: {duplicates:,}")


# --------------------------------------------------
# First rows
# --------------------------------------------------

print("\n" + "=" * 60)
print("6. FIRST 5 ROWS")
print("=" * 60)

print(df.head().to_string())


# --------------------------------------------------
# Statistical summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("7. STATISTICAL SUMMARY")
print("=" * 60)

print(df.describe().T.to_string())


# --------------------------------------------------
# Unique profile IDs
# --------------------------------------------------

if "profile_id" in df.columns:

    print("\n" + "=" * 60)
    print("8. PROFILE INFORMATION")
    print("=" * 60)

    print(
        f"Unique profiles: {df['profile_id'].nunique():,}"
    )

    print("\nSamples per profile:")

    print(
        df["profile_id"]
        .value_counts()
        .sort_index()
        .to_string()
    )


print("\n" + "=" * 60)
print("AUDIT COMPLETE")
print("=" * 60)