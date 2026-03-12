
from sklearn.linear_model import Ridge
from data.data_loader import load_dataset
from training.training_core import train_model

def predict_with_ridge():
    X_train, X_test, y_train, y_test = load_dataset()

    model = Ridge(alpha=100)

    return train_model(
        model,
        "Ridge Regression",
        "ridge_regression",
        X_train,
        X_test,
        y_train,
        y_test
    )


def get_model_Ridge_regression():
    model = Ridge(alpha=100)
    return model, "Ridge Regression"