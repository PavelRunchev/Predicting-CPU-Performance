import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import cross_val_score
from data.data_loader import load_full_dataset
from evaluation.visual_plot_regression import visual_plot_regression

def train_model(model, name, plot_name, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    X_full, y_full = load_full_dataset()
    scores = cross_val_score(model, X_full, y_full, cv=5, scoring="r2")
    cv_mean = scores.mean()

    visual_plot_regression(
        title=f"{name}",
        y_test=y_test,
        y_pred=y_pred,
        r2=r2,
        mae=mae,
        rmse=rmse,
        plot_name=f"{plot_name}"
    )

    return {
        "name": name,
        "r2": round(float(r2), 4),
        "mae": round(float(mae), 2),
        "rmse": round(float(rmse), 2),
        "cv_mean": round(float(cv_mean), 4)
    }