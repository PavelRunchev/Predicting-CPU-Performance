from nicegui import ui


def show_model_categories():

    ui.label("Категории на моделите за машинно обучение").classes("text-2xl font-bold mx-auto").style("color: var(--primary); text-indent: 40px;")

    categories = {
        "Линейни модели": [
            "Linear Regression",
            "Ridge Regression",
            "Lasso Regression"
        ],
        "Нелинейни модели": [
            "Polynomial Regression"
        ],
        "Дървовидни модели": [
            "Decision Tree",
            "Random Forest",
            "Gradient Boosting"
        ],
        "Кернел модели": [
            "Support Vector Machine (SVM)"
        ]
    }

    icons = {
        "Линейни модели": "show_chart",
        "Нелинейни модели": "timeline",
        "Дървовидни модели": "account_tree",
        "Кернел модели": "hub"
    }

    with ui.column().classes("items-center w-full my-6"):

        with ui.grid(columns=2).classes("gap-6 max-w-4xl"):

            for category, models in categories.items():

                with ui.card().classes("p-4 shadow-md w-full hover:shadow-xl transition cursor-pointer"):

                    with ui.row().classes("items-center gap-2"):
                        ui.icon(icons[category]).classes("text-2xl")
                        ui.label(category).classes("text-xl font-semibold")

                    for model in models:
                        ui.label(f"• {model}")