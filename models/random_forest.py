from sklearn.ensemble import RandomForestRegressor
from data.data_loader import load_dataset
from training.training_core import train_model

def predict_with_random_forest():
    X_train, X_test, y_train, y_test = load_dataset()

    model = RandomForestRegressor( n_estimators=200, max_depth=12, random_state=42 )

    return train_model(
        model,
        "Random Forest",
        "random_forest",
        X_train,
        X_test,
        y_train,
        y_test
    )

def get_model_random_forest():
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=12,
        random_state=42
    )
    return model, "Random Forest"


