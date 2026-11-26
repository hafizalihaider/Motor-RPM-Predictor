from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "measure.csv"

df = pd.read_csv(DATA_PATH)

print(df.head())
print(df.shape)

# # VOLTAGE DISTRIBUTION
# plt.figure(figsize=(8,5))
# plt.hist(df["voltage_V"], bins=20)
# plt.xlabel("Voltage (V)")
# plt.ylabel("Frequency")
# plt.title("Voltage Distribution")
# plt.show()

# # CURRENT DISTRIBUTION
# plt.figure(figsize=(8,5))
# plt.hist(df["current_A"], bins=20)
# plt.xlabel("Current (A)")
# plt.ylabel("Frequency")
# plt.title("Current Distribution")
# plt.show()

# # TORQUE DISTRIBUTION
# plt.figure(figsize=(8,5))
# plt.hist(df["torque_Nm"], bins=20)
# plt.xlabel("Torque (Nm)")
# plt.ylabel("Frequency")
# plt.title("Torque Distribution")
# plt.show()

# # RPM DISTRIBUTION
# plt.figure(figsize=(8,5))
# plt.hist(df["rpm"], bins=20)
# plt.xlabel("RPM")
# plt.ylabel("Frequency")
# plt.title("RPM Distribution")
# plt.show()

# # VOLTAGE VS RPM
# plt.figure(figsize=(8,5))
# plt.scatter(df["voltage_V"],df["rpm"],alpha=0.5)
# plt.xlabel("Voltage (V)")
# plt.ylabel("RPM")
# plt.title("Voltage vs RPM")
# plt.show()

# # CURRENT VS RPM
# plt.figure(figsize=(8,5))
# plt.scatter(df["current_A"],df["rpm"],alpha=0.5)
# plt.xlabel("Current (A)")
# plt.ylabel("RPM")
# plt.title("Current vs RPM")
# plt.show()

# # TORQUE VS RPM
# plt.figure(figsize=(8,5))
# plt.scatter(df["torque_Nm"],df["rpm"],alpha=0.5)
# plt.xlabel("Torque (Nm)")
# plt.ylabel("RPM")
# plt.title("Torque vs RPM")
# plt.show()

# # VOLTAGE VS CURRENT
# plt.figure(figsize=(8,5))
# plt.scatter(df["voltage_V"],df["current_A"],alpha=0.5)
# plt.xlabel("Voltage (V)")
# plt.ylabel("Current (A)")
# plt.title("Voltage vs Current")
# plt.show()

# # VOLTAGE VS TORQUE
# plt.figure(figsize=(8,5))
# plt.scatter(df["voltage_V"],df["torque_Nm"],alpha=0.5)
# plt.xlabel("Voltage (V)")
# plt.ylabel("Torque (Nm)")
# plt.title("Voltage vs Torque")
# plt.show()

# # CURRENT VS TORQUE
# plt.figure(figsize=(8,5))
# plt.scatter(df["current_A"],df["torque_Nm"],alpha=0.5)
# plt.xlabel("Current (A)")
# plt.ylabel("Torque (Nm)")
# plt.title("Current vs Torque")
# plt.show()

correlation = df.corr(numeric_only=True)
print(correlation)

# plt.figure(figsize=(8,6))
# sns.heatmap(correlation,annot=True,cmap="coolwarm",fmt=".2f")
# plt.title("Correlation Matrix")
# plt.show()

X = df[["voltage_V","current_A"]]
y = df["rpm"]

print(X.head())
print(y.head())
print(X.shape)
print(y.shape)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

model = LinearRegression()
model.fit(X_train, y_train)
print(model.intercept_)
print(model.coef_)