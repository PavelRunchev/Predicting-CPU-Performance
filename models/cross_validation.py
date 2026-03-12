import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from data.data_loader import load_full_dataset
from sklearn.model_selection import KFold
from nicegui import ui

def cross_validation(get_model):
    X, y = load_full_dataset()
    model, name = get_model()

    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(model, X, y, cv=cv, scoring='r2')

    mean_score = scores.mean()
    std_score = scores.std()

    ui.label(f"{name} — Кръстосана валидация (Cross-Validation)").classes("text-2xl font-bold section-title mt-6 mx-auto")
    ui.html(f"Средна стойност на R² от кръстосаната валидация: {mean_score:.4f} <span class='font-normal text-gray-500 text-sm'>(по-близо до 1 е най-добре)</span>").classes("text-lg font-semibold mt-2 mx-auto")
    (ui.html(f"Стандартно отклонение: {std_score:.4f} <span class='font-normal text-gray-500 text-sm'>(близо до 0 е най-добре)</span>")
     .classes("text-lg font-semibold mt-2 mx-auto"))
    ui.html(f"Стабилност на модела: {get_model_status(std_score)}").classes("text-lg font-semibold mt-2 mx-auto")

    plt.figure(figsize=(6, 4))
    plt.bar(range(1, len(scores) + 1), scores)
    plt.axhline(mean_score, linestyle='--')

    plt.title(f"{name} — R² при кръстосана валидация")
    plt.xlabel("Итерация (K-Fold)")
    plt.ylabel("Стойност на R²")
    plt.tight_layout()

    plot_path = f"plots/{name}.png"
    plt.savefig(plot_path)
    plt.close()
    ui.image(plot_path).classes("w-[600px] mt-4 mx-auto")

    return mean_score



def get_model_status(std):
    if std < 0.05:
        return '<span style="color: var(--primary)">Много стабилен модел</span>'
    elif std < 0.1:
        return '<span style="color: var(--primary)">Стабилен модел</span>'
    elif std < 0.2:
        return '<span style="color: var(--primary)">Средна стабилност</span>'
    else:
        return '<span style="color: var(--primary)">Нестабилен модел</span>'














    #
    #
    # with ui.pyplot():
    #     plt.figure(figsize=(6, 4))
    #     plt.bar(range(1, len(scores) + 1), scores)
    #     plt.axhline(scores.mean(), linestyle='--', label='Mean', color='red')
    #     plt.title(f"{name} — Cross Validation R²")
    #     plt.xlabel("Fold")
    #     plt.ylabel("R² Score")
    #     plt.legend()
    #     plt.tight_layout()

