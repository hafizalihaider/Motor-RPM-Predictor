
from pathlib import Path
import joblib
import pandas as pd

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"rpm_model.joblib"
DATA_PATH=PROJECT_ROOT/"data"/"measure.csv"

model=joblib.load(MODEL_PATH)
df=pd.read_csv(DATA_PATH)

voltage_min=df["voltage_V"].min()
voltage_max=df["voltage_V"].max()
current_min=df["current_A"].min()
current_max=df["current_A"].max()

print("Model loaded successfully.")
print(f"Voltage range: {voltage_min:.2f} to {voltage_max:.2f} V")
print(f"Current range: {current_min:.2f} to {current_max:.2f} A")

while True:
    voltage_input=input("Enter voltage (V) or q to quit: ")
    if voltage_input.lower()=="q":
        break
    current_input=input("Enter current (A): ")
    try:
        voltage=float(voltage_input)
        current=float(current_input)
    except ValueError:
        print("Error: Enter valid numeric values.")
        continue
    if voltage<0 or current<0:
        print("Error: Voltage and current cannot be negative.")
        continue
    if not (voltage_min<=voltage<=voltage_max):
        print(f"Error: Voltage must be between {voltage_min:.2f} and {voltage_max:.2f} V.")
        continue
    if not (current_min<=current<=current_max):
        print(f"Error: Current must be between {current_min:.2f} and {current_max:.2f} A.")
        continue
    X_new=pd.DataFrame([[voltage,current]],columns=["voltage_V","current_A"])
    rpm_prediction=model.predict(X_new)
    print("Predicted RPM:",rpm_prediction[0])

print("Prediction program closed.")
