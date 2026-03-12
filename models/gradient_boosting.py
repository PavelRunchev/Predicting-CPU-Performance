
from sklearn.ensemble import GradientBoostingRegressor
from data.data_loader import load_dataset
from training.training_core import train_model

def predict_with_gradient_boosting():
    X_train, X_test, y_train, y_test = load_dataset()

    model = GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        random_state=42
    )

    return train_model(
        model,
        "Gradient Boosting",
        "gradient_boosting",
        X_train,
        X_test,
        y_train,
        y_test
    )


def get_model_gradient_boosting():
    model = GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        random_state=42
    )

    return model, "Gradient Boosting"