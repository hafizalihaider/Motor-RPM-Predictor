# Motor RPM Predictor

A machine learning project that predicts DC motor speed (RPM) using voltage and current as input features.

## 1. Project Overview

This project uses Python and Scikit-learn to develop and evaluate regression models for motor RPM prediction.

The project includes:
- Synthetic dataset generation
- Exploratory data analysis (EDA)
- Linear Regression model training
- Random Forest model training
- Model evaluation and comparison
- Prediction using new input values
- Input validation
- Model persistence using Joblib

## 2. Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Joblib

## 3. Project Structure

```text
Motor-RPM-Predictor/
├── data/
│   └── measure.csv
├── models/
│   └── rpm_model.joblib
├── results/
│   └── model_comparison.csv
├── src/
│   ├── 01_data_generation.py
│   ├── 02_basic_eda.py
│   ├── 03_train_model.py
│   ├── 04_model_visualization.py
│   ├── 05_predict_rpm.py
│   ├── 06_model_validation.py
│   ├── 07_new_data_validation.py
│   └── 08_model_comparison.py
├── .gitignore
├── README.md
└── requirements.txt
```

The local `.venv/` directory is excluded from version control.

## 4. Installation

### Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Motor-RPM-Predictor
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Running the Project

Run all commands from the project root directory.

### Generate the dataset

```bash
python src/01_data_generation.py
```

### Perform exploratory data analysis

```bash
python src/02_basic_eda.py
```

### Train the model

```bash
python src/03_train_model.py
```

### Visualize model predictions and residuals

```bash
python src/04_model_visualization.py
```

### Predict motor RPM

```bash
python src/05_predict_rpm.py
```

The prediction interface accepts voltage and current values and checks that inputs are numeric, non-negative, and within the observed dataset ranges.

### Validate the saved model

```bash
python src/06_model_validation.py
```

### Test predictions with new data

```bash
python src/07_new_data_validation.py
```

### Compare regression models

```bash
python src/08_model_comparison.py
```

## 6. Model Performance

Two regression algorithms were evaluated using the same train-test split.

| Model | MAE (RPM) | RMSE (RPM) | R² |
|---|---:|---:|---:|
| Linear Regression | 24.83 | 30.78 | 0.99889 |
| Random Forest | 35.85 | 46.85 | 0.99743 |

Linear Regression achieved lower MAE and RMSE and a higher R² score on this test split.

### Evaluation Metrics

- **MAE:** Mean Absolute Error measures the average absolute difference between actual and predicted RPM.
- **RMSE:** Root Mean Squared Error penalizes larger prediction errors more heavily.
- **R²:** Measures how much of the variation in the test target values is explained by the model.

## 7. Dataset and Model Limitations

- The dataset is synthetically generated rather than collected through physical motor experiments.
- Motor parameters used during generation are assumed educational values, not experimentally measured constants.
- The high evaluation scores reflect the mathematical structure of the synthetic dataset.
- Testing against the same underlying theoretical equations does not establish real-world accuracy.
- Predictions should not be used for physical motor control or safety-critical applications without independent experimental validation.

## 8. Current Project Status

The software implementation includes dataset generation, exploratory analysis, model training, evaluation, visualization, model comparison, prediction, and input validation.

Future improvements should focus on:
- Collecting real motor measurement data.
- Testing on independent experimental datasets.
- Applying cross-validation.
- Evaluating prediction uncertainty.
- Improving generalization to unseen operating conditions.

## 9. Author

**Muhammad Ali Haider**

GitHub: [Add your GitHub profile URL here]