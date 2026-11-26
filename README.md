# Motor RPM Predictor

A Python-based machine learning project that predicts DC motor rotational speed (RPM) using voltage and current measurements.

The project includes data generation, exploratory data analysis, model training, visualization, model validation, feature comparison, and a command-line prediction application.

## Project Objectives

- Generate and analyze a motor measurement dataset.
- Explore relationships between voltage, current, torque, and RPM.
- Train machine learning models to predict RPM.
- Evaluate model performance using regression metrics.
- Compare models using different input features.
- Accept new CSV measurement files and generate RPM predictions.
- Export prediction results to a CSV file.

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
│
├── data/
│   └── measure.csv
│
├── models/
│   ├── rpm_model.joblib
│   └── rpm_model_with_torque.joblib
│
├── output/
│   └── predictions.csv
│
├── results/
│   └── feature_comparison.csv
│
├── src/
│   ├── 01_data_generation.py
│   ├── 02_basic_eda.py
│   ├── 03_train_model.py
│   ├── 04_model_visualization.py
│   ├── 05_predict_rpm.py
│   ├── 06_model_validation.py
│   ├── 07_new_data_validation.py
│   └── 08_model_comparison.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/hafizalihaider/Motor-RPM-Predictor.git
cd Motor-RPM-Predictor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Model Training

The training script uses the dataset in `data/measure.csv`.

Run:

```bash
python .\src\03_train_model.py
```

The script trains and saves two models:

| Model | Input Features |
|---|---|
| Model A | Voltage and Current |
| Model B | Voltage, Current, and Torque |

The trained models are saved in the `models/` directory.

Feature comparison results are saved in `results/feature_comparison.csv`.

## Running the Prediction Application

Run the main application from the project root:

```bash
python main.py
```

The application asks for a CSV file path.

- Enter a valid CSV path to predict RPM from new measurements.
- Press Enter to use the default dataset, `data/measure.csv`.

### Input CSV Format

The application requires these two columns:

| Column | Description | Unit |
|---|---|---|
| `voltage_V` | Motor supply voltage | Volts |
| `current_A` | Motor current | Amperes |

An optional `rpm` column can be included when actual RPM measurements are available. The application uses it to evaluate predictions; it is not used as a prediction input.

Example:

```csv
voltage_V,current_A,rpm
12,3,1850
12,8,900
24,3,3900
18,5,2600
9,2,1200
```

The example values are illustrative, not verified motor measurements.

### Application Workflow

1. Checks that the required files exist.
2. Reads the selected CSV file.
3. Validates required columns and measurement values.
4. Checks input values against the training dataset's individual feature ranges.
5. Loads the trained regression model.
6. Predicts RPM.
7. Evaluates predictions if actual RPM values are supplied.
8. Saves the results to `output/predictions.csv`.

### Output

The application preserves the input data and adds a new column:

`predicted_RPM`

The output file is:

```text
output/predictions.csv
```

When actual RPM is supplied, the application reports:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Error

## Model Evaluation

The Linear Regression model was evaluated on a held-out test set containing 400 samples.

| Metric | Result |
|---|---:|
| MAE | 24.83 RPM |
| RMSE | 30.78 RPM |
| R² Score | 0.99889 |

The dataset was divided into 80% training data and 20% testing data using `random_state=42`.

These results describe performance on the held-out portion of the generated dataset. They do not establish accuracy on real motors.

## Scientific Limitations

**The current dataset is synthetic.**

It was generated using simplified steady-state brushed DC motor equations and assumed motor parameters. These parameters are educational assumptions, not experimentally measured values or verified manufacturer specifications.

The model therefore learns relationships within this simulated dataset. Its high R² score should not be interpreted as evidence of equivalent accuracy on real motor measurements.

Additional limitations include:

- The model does not account for every real motor operating condition.
- Current and torque are strongly correlated in the generated dataset.
- Individual input range checks do not guarantee that a voltage-current combination is physically realistic.
- Independent experimental measurements are required to evaluate real-world predictive performance.

## Future Improvements

- Evaluate the model using experimentally collected motor data.
- Investigate prediction errors under different operating conditions.
- Improve input validation using physically meaningful constraints.
- Compare additional regression algorithms.
- Assess model performance on independent datasets.

## Author

**Muhammad Ali Haider**

GitHub: [hafizalihaider](https://github.com/hafizalihaider)

Repository: [Motor-RPM-Predictor](https://github.com/hafizalihaider/Motor-RPM-Predictor)
