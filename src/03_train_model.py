import joblib
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "measure.csv"

df = pd.read_csv(DATA_PATH)

X = df[["voltage_V","current_A"]]
y = df["rpm"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print("Training features:",X_train.shape)
print("Testing features:",X_test.shape)
print("Training targets:",y_train.shape)
print("Testing targets:",y_test.shape)

model = LinearRegression()
model.fit(X_train,y_train)

print("Intercept:",model.intercept_)
print("Coefficients:",model.coef_)

y_pred=model.predict(X_test)

print("Actual RPM:")
print(y_test.iloc[:5])
print("Predicted RPM:")
print(y_pred[:5])

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
r2=r2_score(y_test,y_pred)

print("MAE:",mae)
print("RMSE:",rmse)
print("R2 Score:",r2)

MODEL_DIR=PROJECT_ROOT/"models"
MODEL_DIR.mkdir(exist_ok=True)
MODEL_PATH=MODEL_DIR/"rpm_model.joblib"
joblib.dump(model,MODEL_PATH)
print("Model saved to:",MODEL_PATH)