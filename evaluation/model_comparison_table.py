from nicegui import ui

def get_model_comparison_table():
    ui.label("Таблица за сравнение на моделите за машинно обучение.").classes("text-2xl font-bold mx-auto").style("color: var(--primary); text-indent: 40px;")

    columns = [
        {"name": "model", "label": "Модел", "field": "model"},
        {"name": "type", "label": "Тип модел", "field": "type"},
        {"name": "use", "label": "Кога е подходящ", "field": "use"},
        {"name": "advantage", "label": "Основно предимство", "field": "advantage"},
    ]

    rows = [
        {"model": "Linear Regression", "type": "Линеен", "use": "Линейни зависимости", "advantage": "Лесен за интерпретация"},
        {"model": "Polynomial Regression", "type": "Нелинеен", "use": "Криволинейни зависимости", "advantage": "Моделира сложни връзки"},
        {"model": "Ridge Regression", "type": "Линеен (регуларизация)", "use": "Корелирани характеристики", "advantage": "Намалява свръхнапасването"},
        {"model": "Lasso Regression", "type": "Линеен (регуларизация)", "use": "Много характеристики", "advantage": "Избор на функции"},
        {"model": "Decision Tree", "type": "Tree-based", "use": "Сложни зависимости", "advantage": "Лесен за разбиране"},
        {"model": "Random Forest", "type": "Ансамбъл", "use": "По-висока точност", "advantage": "Намалява свръхнапасването"},
        {"model": "Gradient Boosting", "type": "Ансамбъл", "use": "Максимална точност", "advantage": "Много мощен модел"},
        {"model": "Support Vector Regression", "type": "Kernel-based", "use": "Нелинейни зависимости", "advantage": "Работи добре с със сложни модели"},
    ]

    ui.table(columns=columns, rows=rows).classes("w-full max-w-5xl mx-auto shadow-lg rounded-lg")