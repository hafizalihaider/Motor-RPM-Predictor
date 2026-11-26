# Motor RPM Predictor

A machine learning project that predicts DC motor speed (RPM) using voltage and current as input features.

## Project Overview

This project uses Python and Scikit-learn to train and evaluate regression models for RPM prediction.

Two models are compared:
- Linear Regression
- Random Forest Regressor

Linear Regression currently performs better on the project's test split.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Joblib

## Project Structure

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
└── README.md
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Project

Run scripts from the project root directory.

Generate the dataset:

```bash
python src/01_data_generation.py
```

Train the model:

```bash
python src/03_train_model.py
```

Run the prediction interface:

```bash
python src/05_predict_rpm.py
```

Compare models:

```bash
python src/08_model_comparison.py
```

## Model Performance

| Model | MAE (RPM) | RMSE (RPM) | R² |
|---|---:|---:|---:|
| Linear Regression | 24.83 | 30.78 | 0.99889 |
| Random Forest | 35.85 | 46.85 | 0.99743 |

These metrics are from one train-test split using the generated dataset.

## Important Limitations

- The dataset is synthetically generated, not collected from physical motor experiments.
- The assumed motor parameters are educational assumptions, not experimentally measured constants.
- High test performance does not establish real-world prediction accuracy.
- The model should not be used for physical motor control or safety-critical decisions without independent experimental validation.

## Current Status

Software implementation, model comparison, prediction interface, and input validation are complete. Further work should focus on independent experimental data and rigorous model validation.