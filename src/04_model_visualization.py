from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "measure.csv"

df = pd.read_csv(DATA_PATH)

X = df[["voltage_V","current_A"]]
y = df["rpm"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(8,5))
plt.scatter(y_test,y_pred,alpha=0.5)
min_value=min(y_test.min(),y_pred.min())
max_value=max(y_test.max(),y_pred.max())
plt.plot([min_value,max_value],[min_value,max_value],"r--",label="Perfect Prediction")
plt.xlabel("Actual RPM")
plt.ylabel("Predicted RPM")
plt.title("Actual vs Predicted RPM")
plt.legend()
plt.show()

residuals = y_test - y_pred
print(residuals.head())

plt.figure(figsize=(8,5))
plt.scatter(y_pred,residuals,alpha=0.5)
plt.axhline(y=0,color="red",linestyle="--")
plt.xlabel("Predicted RPM")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

print("Mean Residual:",residuals.mean())
print("Minimum Residual:",residuals.min())
print("Maximum Residual:",residuals.max())