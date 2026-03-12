
from sklearn.tree import DecisionTreeRegressor
from data.data_loader import load_dataset
from training.training_core import train_model

def predict_with_decision_tree():
    X_train, X_test, y_train, y_test = load_dataset()

    model = DecisionTreeRegressor(
        max_depth=10,
        min_samples_split=5,
        random_state=42
    )

    return train_model(
        model,
        "Decision Tree",
        "decision_tree",
        X_train,
        X_test,
        y_train,
        y_test
    )

def get_model_decision_tree():
    model = DecisionTreeRegressor(
        max_depth=10,
        min_samples_split=5,
        random_state=42
    )

    return model, "Decision Tree"


