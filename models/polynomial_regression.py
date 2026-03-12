
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from data.data_loader import load_dataset
from training.training_core import train_model

def predict_with_polynomial_regression():
    X_train, X_test, y_train, y_test = load_dataset()

    model = Pipeline([
        ("poly", PolynomialFeatures(degree=2)),
        ("linear", LinearRegression())
    ])

    return train_model(
        model,
        "Polynomial Regression",
        "polynomial_regression",
        X_train,
        X_test,
        y_train,
        y_test
    )

def get_model_Polynomial_regression():
    model = Pipeline([
        ("poly", PolynomialFeatures(degree=2)),
        ("linear", LinearRegression())
    ])
    return model, "Polynomial Regression"