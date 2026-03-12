
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from data.data_loader import load_dataset
from training.training_core import train_model
from sklearn.pipeline import Pipeline

def predict_with_support_vector_regression():
    X_train, X_test, y_train, y_test = load_dataset()

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("svr", SVR(kernel="rbf", C=10, epsilon=0.1))
    ])
    return train_model(
        model,
        "Support Vector Regression (SVR)",
        "support_vector_regression",
        X_train,
        X_test,
        y_train,
        y_test
    )


def get_model_support_vector_regression():
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("svr", SVR(kernel="rbf", C=10, epsilon=0.1))
    ])

    return model, "Support Vector Regression (SVR)"