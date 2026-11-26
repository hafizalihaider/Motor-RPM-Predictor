from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import joblib

PROJECT_ROOT=Path(__file__).resolve().parent.parent
DATA_PATH=PROJECT_ROOT/"data"/"measure.csv"

df=pd.read_csv(DATA_PATH)
X=df[["voltage_V","current_A"]]
y=df["rpm"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

models={
    "Linear Regression":LinearRegression(),
    "Random Forest":RandomForestRegressor(n_estimators=100,random_state=42)
}

results=[]

for name,model in models.items():
    model.fit(X_train,y_train)
    predictions=model.predict(X_test)
    mae=mean_absolute_error(y_test,predictions)
    rmse=mean_squared_error(y_test,predictions)**0.5
    r2=r2_score(y_test,predictions)
    results.append({
        "Model":name,
        "MAE":mae,
        "RMSE":rmse,
        "R2":r2
    })
    print("\n",name)
    print("MAE:",mae)
    print("RMSE:",rmse)
    print("R2:",r2)

results_df=pd.DataFrame(results)
RESULTS_DIR=PROJECT_ROOT/"results"
RESULTS_DIR.mkdir(exist_ok=True)
RESULTS_PATH=RESULTS_DIR/"model_comparison.csv"
results_df.to_csv(RESULTS_PATH,index=False)
print("Results saved to:",RESULTS_PATH)