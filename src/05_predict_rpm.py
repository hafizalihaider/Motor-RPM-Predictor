from pathlib import Path
import joblib

PROJECT_ROOT=Path(__file__).resolve().parent.parent
MODEL_PATH=PROJECT_ROOT/"models"/"rpm_model.joblib"