from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

PROJECT_ROOT=Path(__file__).resolve().parent.parent
DATA_PATH=PROJECT_ROOT/"data"/"measure.csv"
MODEL_PATH=PROJECT_ROOT/"models"/"rpm_model.joblib"

df=pd.read_csv(DATA_PATH)
model=joblib.load(MODEL_PATH)

X=df[["voltage_V","current_A"]]
y=df["rpm"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

y_pred=model.predict(X_test)

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
r2=r2_score(y_test,y_pred)

print("MAE:",mae)
print("RMSE:",rmse)
print("R2 Score:",r2)