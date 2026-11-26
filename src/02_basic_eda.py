from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "measure.csv"

df = pd.read_csv(DATA_PATH)

print(df.head())
print(df.shape)

# plt.figure(figsize=(8,5))
# plt.hist(df["voltage_V"], bins=20)
# plt.xlabel("Voltage (V)")
# plt.ylabel("Frequency")
# plt.title("Voltage Distribution")
# plt.show()

# plt.figure(figsize=(8,5))
# plt.hist(df["current_A"], bins=20)
# plt.xlabel("Current (A)")
# plt.ylabel("Frequency")
# plt.title("Current Distribution")
# plt.show()

# plt.figure(figsize=(8,5))
# plt.hist(df["torque_Nm"], bins=20)
# plt.xlabel("Torque (Nm)")
# plt.ylabel("Frequency")
# plt.title("Torque Distribution")
# plt.show()

# plt.figure(figsize=(8,5))
# plt.hist(df["rpm"], bins=20)
# plt.xlabel("RPM")
# plt.ylabel("Frequency")
# plt.title("RPM Distribution")
# plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["voltage_V"],df["rpm"],alpha=0.5)
plt.xlabel("Voltage (V)")
plt.ylabel("RPM")
plt.title("Voltage vs RPM")
plt.show()