from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "measure.csv"

print("=" * 60)
print("MOTOR RPM PREDICTION — DATA AUDIT")
print("=" * 60)

print("\n1. DATASET PATH")
print("-" * 60)
print(f"Dataset path: {DATA_PATH}")
print(f"Dataset exists: {DATA_PATH.exists()}")

if not DATA_PATH.exists():
    raise FileNotFoundError(f"\nDataset not found:\n{DATA_PATH}")

print("\n2. LOADING DATASET")
print("-" * 60)
df = pd.read_csv(DATA_PATH)
print("Dataset loaded successfully.")

print("\n3. DATASET SHAPE")
print("-" * 60)
rows, columns = df.shape
print(f"Rows: {rows:,}")
print(f"Columns: {columns}")

print("\n4. COLUMN NAMES")
print("-" * 60)
for i, column in enumerate(df.columns, start=1):
    print(f"{i:2}. {column}")

print("\n5. DATA TYPES")
print("-" * 60)
print(df.dtypes)

print("\n6. MISSING VALUES")
print("-" * 60)
missing = df.isnull().sum()
print(missing)
print(f"\nTotal missing values: {missing.sum():,}")

print("\n7. DUPLICATE ROWS")
print("-" * 60)
duplicates = df.duplicated().sum()
print(f"Duplicate rows: {duplicates:,}")

print("\n8. FIRST FIVE ROWS")
print("-" * 60)
print(df.head().to_string())

print("\n9. STATISTICAL SUMMARY")
print("-" * 60)
print(df.describe().T.to_string())

print("\n10. REQUIRED COLUMN VALIDATION")
print("-" * 60)
required_columns = ["voltage_V", "current_A", "torque_Nm", "rpm"]

for column in required_columns:
    if column in df.columns:
        print(f"[FOUND] {column}")
    else:
        print(f"[MISSING] {column}")

print("\n" + "=" * 60)
print("AUDIT COMPLETE")
print("=" * 60)