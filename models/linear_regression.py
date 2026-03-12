import matplotlib
from data.data_loader import load_dataset
from sklearn.linear_model import LinearRegression
from training.training_core import train_model

matplotlib.rcParams['font.family'] = 'DejaVu Sans'
matplotlib.rcParams['axes.unicode_minus'] = False

def predict_with_linear_regression():
    X_train, X_test, y_train, y_test = load_dataset()

    model = LinearRegression()

    return train_model(
        model,
        "Linear Regression",
        "linear_regression",
        X_train,
        X_test,
        y_train,
        y_test
    )

def get_model_linear_regression():
    model = LinearRegression()
    return model, "Linear Regression"

