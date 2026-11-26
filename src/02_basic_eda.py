from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "measure.csv"

df = pd.read_csv(DATA_PATH)

print(df.head())
print(df.shape)

plt.figure(figsize=(8,5))
plt.hist(df["voltage_V"], bins=20)
plt.xlabel("Voltage (V)")
plt.ylabel("Frequency")
plt.title("Voltage Distribution")
plt.show()