import os
import matplotlib
matplotlib.use("Agg")   # важно за сървъри (без GUI)

import matplotlib.pyplot as plt
from nicegui import ui


def visual_plot_regression(title: str, y_test, y_pred, r2: float, mae: float, rmse: float, plot_name: str):

    ui.label(title).classes("text-2xl font-bold section-title mt-8 mx-auto").style("color: var(--primary)")

    os.makedirs("plots", exist_ok=True)
    plot_path = f"plots/{plot_name}.png"

    if not os.path.exists(plot_path):

        plt.figure(figsize=(7, 5))

        plt.scatter(y_test, y_pred, alpha=0.7)

        plt.plot(
            [y_test.min(), y_test.max()],
            [y_test.min(), y_test.max()],
            'r--'
        )

        plt.title(f"{title} — Реални срещу Предвидени стойности")
        plt.xlabel("Реални стойности")
        plt.ylabel("Предвидени стойности")

        plt.tight_layout()
        plt.savefig(plot_path)
        plt.close('all')

    ui.label(f"Коефицент на детерминация (R²): {r2:.4f}") \
        .classes("text-lg font-semibold mx-auto")

    ui.label("Диапазон: 0–1 → по-високите стойности показват по-добра производителност на модела") \
        .classes("text-sm text-gray-500 mx-auto")

    ui.label(f"Средна абсолютна грешка (MAE): {mae:.2f}") \
        .classes("text-lg font-semibold mx-auto")

    ui.label("По-ниските стойности показват по-висока точност на прогнозиране") \
        .classes("text-sm text-gray-500 mx-auto")

    ui.label(f"Средна квадратична грешка (RMSE): {rmse:.2f}") \
        .classes("text-lg font-semibold mx-auto")

    ui.label("По-ниските стойности показват по-висока точност на прогнозиране") \
        .classes("text-sm text-gray-500 mx-auto")

    ui.image(plot_path).classes("w-[600px] mt-4 mx-auto")
