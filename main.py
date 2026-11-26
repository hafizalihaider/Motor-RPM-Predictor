
import joblib
import numpy as np
from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error

PROJECT_ROOT=Path(__file__).resolve().parent
TRAINING_DATA_PATH=PROJECT_ROOT/"data"/"measure.csv"
MODEL_PATH=PROJECT_ROOT/"models"/"rpm_model.joblib"
OUTPUT_DIR=PROJECT_ROOT/"output"
OUTPUT_PATH=OUTPUT_DIR/"predictions.csv"
required_columns=["voltage_V","current_A"]

print("\nMOTOR RPM PREDICTOR")
print("="*40)

try:
    if not TRAINING_DATA_PATH.exists():
        raise FileNotFoundError(f"Training dataset not found: {TRAINING_DATA_PATH}")

    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Trained model not found: {MODEL_PATH}. Run src/03_train_model.py first.")

    file_path=input("\nEnter CSV file path (press Enter for default dataset): ").strip().strip('"')
    DATA_PATH=Path(file_path) if file_path else TRAINING_DATA_PATH

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"CSV file not found: {DATA_PATH}")

    df=pd.read_csv(DATA_PATH)

    if df.empty:
        raise ValueError("The CSV file contains no measurement rows.")

    missing_columns=[column for column in required_columns if column not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    X=df[required_columns].copy()

    for column in required_columns:
        X[column]=pd.to_numeric(X[column],errors="raise")

    if X.isnull().any().any():
        raise ValueError("CSV contains missing voltage or current values.")

    if not np.isfinite(X.to_numpy()).all():
        raise ValueError("Voltage and current must contain finite numeric values.")

    if X.lt(0).any().any():
        raise ValueError("Voltage and current must be non-negative.")

    if (X["voltage_V"]==0).any():
        raise ValueError("Voltage must be greater than zero.")

    training_data=pd.read_csv(TRAINING_DATA_PATH)

    for column in required_columns:
        minimum=training_data[column].min()
        maximum=training_data[column].max()

        if (X[column]<minimum).any() or (X[column]>maximum).any():
            raise ValueError(
                f"{column} contains values outside the training range "
                f"({minimum:.3f} to {maximum:.3f})."
            )

    model=joblib.load(MODEL_PATH)
    predictions=model.predict(X)
    df["predicted_RPM"]=predictions

    if "rpm" in df.columns:
        df["rpm"]=pd.to_numeric(df["rpm"],errors="raise")

        if df["rpm"].isnull().any() or not np.isfinite(df["rpm"].to_numpy()).all():
            raise ValueError("Actual RPM contains missing or invalid values.")

        if (df["rpm"]<0).any():
            raise ValueError("Actual RPM cannot be negative.")

        errors=df["rpm"]-df["predicted_RPM"]
        mae=mean_absolute_error(df["rpm"],df["predicted_RPM"])
        rmse=mean_squared_error(df["rpm"],df["predicted_RPM"])**0.5

        print("\nPrediction Evaluation:")
        print("MAE:",mae)
        print("RMSE:",rmse)
        print("Mean Error:",errors.mean())
    else:
        print("\nActual RPM unavailable. Prediction errors cannot be calculated.")

    OUTPUT_DIR.mkdir(parents=True,exist_ok=True)
    df.to_csv(OUTPUT_PATH,index=False)

    print("\nPrediction Summary:")
    print("Dataset loaded:",len(df),"rows")
    print("Model loaded successfully")
    print("Predictions generated:",len(predictions))
    print("Minimum predicted RPM:",df["predicted_RPM"].min())
    print("Maximum predicted RPM:",df["predicted_RPM"].max())
    print("Average predicted RPM:",df["predicted_RPM"].mean())

    print("\nPrediction Preview:")
    preview_columns=required_columns.copy()

    if "rpm" in df.columns:
        preview_columns.append("rpm")

    preview_columns.append("predicted_RPM")
    print(df[preview_columns].head(10).to_string(index=False))
    print("\nResults saved to:",OUTPUT_PATH)
    print("\nPROCESS COMPLETED")

except (FileNotFoundError,ValueError,KeyError,pd.errors.ParserError) as error:
    print(f"\nERROR: {error}")
    print("PROCESS TERMINATED")

except Exception as error:
    print(f"\nUNEXPECTED ERROR: {error}")
    print("PROCESS TERMINATED")
