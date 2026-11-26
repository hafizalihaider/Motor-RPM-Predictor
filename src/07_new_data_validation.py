from pathlib import Path
import pandas as pd
import joblib
import numpy as np

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"rpm_model.joblib"
DATA_PATH=PROJECT_ROOT/"data"/"measure.csv"

model=joblib.load(MODEL_PATH)
df=pd.read_csv(DATA_PATH)

print("Model loaded successfully.")
print("Voltage range:",df["voltage_V"].min(),df["voltage_V"].max())
print("Current range:",df["current_A"].min(),df["current_A"].max())

new_data=pd.DataFrame({
    "voltage_V":[8.0,14.0,20.0],
    "current_A":[2.0,4.0,6.0]
})

predicted_rpm=model.predict(new_data)
print("Predicted RPM:")
print(predicted_rpm)

R=0.8
Ke=0.05
expected_rpm=np.maximum(0,(new_data["voltage_V"]-new_data["current_A"]*R)/Ke*(60/(2*np.pi)))
print("Theoretical RPM:")
print(expected_rpm)

difference=predicted_rpm-expected_rpm
print("Prediction Difference:")
print(difference)

absolute_error=np.abs(difference)
print("Absolute Error:")
print(absolute_error)

new_mae=np.mean(absolute_error)
print("New Data MAE:",new_mae)

test_data=pd.DataFrame({
    "voltage_V":[3.0,30.0,36.0],
    "current_A":[2.0,2.0,2.0]
})
test_predictions=model.predict(test_data)
print("Extrapolation Predictions:")
print(test_predictions)

theoretical_test=np.maximum(0,(test_data["voltage_V"]-test_data["current_A"]*0.8)/0.05*(60/(2*np.pi)))
print("Theoretical Extrapolation RPM:")
print(theoretical_test)

extrapolation_error=test_predictions-theoretical_test
print("Extrapolation Error:")
print(extrapolation_error)

extrapolation_mae=np.mean(np.abs(extrapolation_error))
print("Extrapolation MAE:",extrapolation_mae)