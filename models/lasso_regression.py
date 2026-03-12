
from sklearn.linear_model import Lasso
from data.data_loader import load_dataset
from training.training_core import train_model

def predict_with_lasso():
    X_train, X_test, y_train, y_test = load_dataset()

    model = Lasso(alpha=1.0, max_iter=10000)

    return train_model(
        model,
        "Lasso Regression",
        "lasso_regression",
        X_train,
        X_test,
        y_train,
        y_test
    )

def get_model_Lasso_regression():
    model = Lasso(alpha=1.0, max_iter=10000)
    return model, "Lasso Regression"