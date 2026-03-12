import matplotlib.pyplot as plt
from nicegui import ui
import time

# формула за оценка (Higher = Better)
def calculate_score(r2, cv_mean):
    return round((r2 * 0.6) + (cv_mean * 0.4), 4)

# оценка на R²
def interpret_r2(r2):
    if r2 > 0.9:
        return "Чудесно"
    elif r2 > 0.75:
        return "Много Добре"
    elif r2 > 0.6:
        return "Добре"
    elif r2 > 0.4:
        return "Умерено"
    else:
        return "Лошо"

# Основна функция
def run_benchmark(results: list):
    # Изчисляваме score за всеки модел
    for model in results:
        model["score"] = calculate_score(
            model["r2"],
            model["cv_mean"]
        )

    # Сортираме по score
    ranked_models = sorted(results, key=lambda x: x["score"], reverse=True)
    # Най-добрият модел
    best = ranked_models[0]

    # UI Визуализация
    ui.separator()
    ui.label("🏆 КЛАСИРАНЕ НА МОДЕЛИТЕ").classes("text-3xl font-bold mt-8 mx-auto")

    # показва най-добрия модел
    with ui.card().classes("p-6 mx-auto w-[500px] shadow-xl bg-green-50 mb-6"):
        ui.label("🥇 НАЙ-ДОБЪР МОДЕЛ").classes("text-xl font-bold text-green-700")
        ui.label(best["name"]).classes("text-2xl font-bold mt-2")
        ui.html(f"R²: {best['r2']:.4f} <span class='font-normal text-gray-500 text-sm'> - (1 е най-добре)</span>").classes("font-bold")
        ui.html(f"CV Mean: {best['cv_mean']:.4f} <span class='font-normal text-gray-500 text-sm'> - (1 е най-добре)</span>").classes("font-bold")
        ui.html(f"MAE: {best['mae']:.4f} <span class='font-normal text-gray-500 text-sm'> - (0 е най-добре)</span>").classes("font-bold")
        ui.html(f"RMSE: {best['rmse']:.4f} <span class='font-normal text-gray-500 text-sm'> - (0 е най-добре)</span>").classes("font-bold")
        ui.html(f"Оценка от представянето: <span class='font-bold text-green-700'> {interpret_r2(best['r2'])}</span>").classes("font-bold")
        ui.html(f"Краен резултат: {best['score']:.4f} <span class='font-normal text-gray-500 text-sm'> - (1 е най-добре)</span>").classes("font-bold")

    # Ranking Bar Chart
    ui.label(
        "Диаграмата с правоъгълници (bar chart) показва резултатите от R² за всички модели. "
        "Всеки правоъгълник представлява един модел (по-висок = по-добро представяне). "
        "Това позволява бързо сравнение срещу моделите, лесно идентифициране на най-добрия модел и по-интуитивно разбиране на резултатите. "
    ).classes("text-base leading-relaxed pl-6").style("text-indent: 40px")

    names = [m["name"] for m in ranked_models]
    scores = [m["score"] for m in ranked_models]

    plt.figure(figsize=(8, 4))
    colors = ["green" if m == best else "gray" for m in ranked_models]
    plt.bar(names, scores, color=colors)

    plt.xticks(rotation=45)
    plt.title("Класиране на моделите (по-висока стойност е по-добре)")

    for i, v in enumerate(scores):
        plt.text(i, v, f"{v:.3f}", ha='center', va='bottom')

    plt.tight_layout()

    plot_path = f"plots/model_ranking_{int(time.time())}.png"
    plt.savefig(plot_path)
    plt.close()

    ui.image(plot_path).classes("w-[700px] mx-auto mt-6")

    # Таблица
    ui.separator()

    ui.label(
        "В таблицата са показани резултатите от няколко различни машинно-обучителни модела, които се опитват да предскажат числова стойност на база на даден набор от данни (dataset). "
        "Всеки ред представлява различен модел: Random Forest, Lasso Regression, Ridge Regression, Linear Regression, Gradient Boosting, Polynomial Regression, Decision Tree, Support Vector Regression (SVR). "
    ).classes("text-base leading-relaxed pl-6").style("text-indent: 40px")
    ui.label("Всеки модел се обучава върху тренировъчни данни и след това се тества върху нови данни.").classes("text-base leading-relaxed pl-6").style("text-indent: 40px")

    ui.label("📋 Резултати от моделите").classes("text-2xl font-bold mt-6 mx-auto")

    columns = [
        {"name": "name", "label": "Model", "field": "name"},
        {"name": "r2", "label": "R² ↑", "field": "r2" },
        {"name": "cv_mean", "label": "CV Mean", "field": "cv_mean"},
        {"name": "mae", "label": "MAE ↓", "field": "mae"},
        {"name": "rmse", "label": "RMSE ↓", "field": "rmse"},
        {"name": "score", "label": "Final Score", "field": "score"},
    ]

    ui.table(columns=columns, rows=ranked_models).classes("w-full max-w-5xl mx-auto mt-4")

    with ui.card().classes("p-6 max-w-3xl mx-auto mt-6 mb-5 bg-gray-50 shadow-lg"):

        ui.label("📊 Обяснение на колоните в таблицата").classes("text-xl font-bold mb-3")

        ui.label("📈 Коефицент на детерминация (R²) – показва колко добре моделът обяснява зависимостта между входните данни и предсказаната стойност.")

        ui.label("🔁 Среден резултат от кръстосана валидация (CV Mean) – е средният резултат от кръстосаната валидация.")

        ui.label("📏 Средна абсолютна грешка (MAE) – измерва средната абсолютна разлика между реалните и предсказаните стойности.")

        ui.label("📉 Средна квадратична грешка (RMSE) – показва средната големина на грешката при предсказване.")

        ui.label("🏆 Крайна оценка (Final Score) – е комбинирана оценка на всички метрики.")
