import os
from nicegui import ui
import matplotlib

from table import cpu_table
from models.linear_regression import predict_with_linear_regression, get_model_linear_regression
from models.random_forest import predict_with_random_forest, get_model_random_forest
from models.ridge_regression import predict_with_ridge, get_model_Ridge_regression
from models.lasso_regression import predict_with_lasso, get_model_Lasso_regression
from models.polynomial_regression import predict_with_polynomial_regression, get_model_Polynomial_regression
from models.decision_tree import predict_with_decision_tree, get_model_decision_tree
from models.support_vector_regression import predict_with_support_vector_regression, get_model_support_vector_regression
from models.gradient_boosting import predict_with_gradient_boosting, get_model_gradient_boosting
from models.cross_validation import cross_validation

from modelInfo.model_info_random_forest import get_model_info_random_forest
from modelInfo.model_info_linear_regression import get_model_info_linear_regression
from modelInfo.model_info_ridge_regression import get_model_info_ridge_regression
from modelInfo.model_info_lasso_regression import get_model_info_lasso_regression
from modelInfo.model_info_polynomial_regression import get_model_info_polynomial_regression
from modelInfo.model_info_decision_tree import get_model_info_decision_tree
from modelInfo.model_info_support_vector_regression import get_model_info_support_vector_regression
from modelInfo.model_info_gradient_boosting import get_model_info_gradient_boosting

from evaluation.benchmark import run_benchmark
from evaluation.model_categories import show_model_categories
from evaluation.model_comparison_table import get_model_comparison_table

matplotlib.use("Agg")

def build_ui():
    ui.add_head_html("""
    <style>
        :root {
            --primary: #70A5D5;
            --primary-dark: #1d4ed8;
            --primary-light: #3b82f6;
        
            --bg-light: #f8fafc;
            --border: #e5e7eb;
            --text-dark: #1f2937;
        }
        .nicegui-content {
            padding: 0 !important;
        }
    </style>
    """)

    (ui.label("Прогнозиране производителността на процесорите, чрез модели за машинно обучение")
        .classes("text-3xl font-bold text-center mt-6 mb-2 mx-auto").style("color: var(--primary); text-indent: 40px;"))

    ui.label("Преглед на производителността на процесорите").classes("text-2xl font-semibold mt-8 pl-6").style("color: var(--primary); text-indent: 40px;")
    ui.label(
        "Производителността на процесора описва колко ефективно процесорът изпълнява изчислителни задачи. "
        "Зависи от множество хардуерни фактори, като тактова честота, капацитет на паметта, размер на кеша и комуникационна честотна лента. "
        "В това приложение моделите за машинно обучение са обучени да оценяват производителността на процесора. "
        "Въз основа на тези технически параметри, което позволява бързо и автоматизирано прогнозиране на производителността. "
    ).classes("text-base leading-relaxed pl-6").style("text-indent: 40px")

    ui.label("Цел").classes("text-2xl font-semibold mt-8 pl-6").style("color: var(--primary); text-indent: 40px;")
    ui.label(
        "Целта на приложението е да се сравнят различни алгоритми за машинно обучение, които се обучават върху dataset с характеристики на процесори и тяхната производителност, за да се установи кой модел може да предскаже производителността най-точно. "
    ).classes("text-base leading-relaxed pl-6").style("text-indent: 40px")

    ui.label("Описание на данните").classes("text-2xl font-semibold mt-6 pl-6").style("color: var(--primary); text-indent: 40px;")
    ui.label(
        "Наборът от данни съдържа технически спецификации на различни компютърни процесори, включително време на цикъла, размер на паметта, капацитет на кеша и комуникационни канали. "
        "Тези характеристики се използват като входни променливи за обучение на модели за машинно обучение за прогнозиране на производителността на процесора. "
        "Целевата променлива PRP (Публикувана относителна производителност) представлява стандартизиран бенчмарк резултат, описващ реалната изчислителна производителност на всеки процесор. "
    ).classes("text-base leading-relaxed pl-6").style("text-indent: 40px")

    # render table
    cpu_table()

    ui.label("Представяне на алгоритмите за машинно обучение един по-един с данните").classes("text-2xl font-semibold mt-6 pl-6 mx-auto").style("color: var(--primary); text-indent: 40px;")

    # render all models
    linear_regression_result = predict_with_linear_regression()
    get_model_info_linear_regression()

    #Random Forest
    random_forest_result = predict_with_random_forest()
    get_model_info_random_forest()

    #Ridge Regression
    ridge_regression_result = predict_with_ridge()
    get_model_info_ridge_regression()

    #Lasso Regression
    lasso_regression_result = predict_with_lasso()
    get_model_info_lasso_regression()

    #Polynomial Regression
    polynomial_regression_result = predict_with_polynomial_regression()
    get_model_info_polynomial_regression()

    #Decision Tree
    decision_tree_result = predict_with_decision_tree()
    get_model_info_decision_tree()

    #Suppoirt Vector Regression
    support_vector_regression_result = predict_with_support_vector_regression()
    get_model_info_support_vector_regression()

    #Gradient Boosting
    gradient_boosting_result = predict_with_gradient_boosting()
    get_model_info_gradient_boosting()

    ui.label("Кръстосана валидация и защо се използва").classes("text-2xl font-semibold mt-8 pl-6").style("color: var(--primary); text-indent: 40px;")
    ui.html(
        "Кръстосаната валидация <span class='font-bold'>(Cross-Validation)</span> е метод за оценка на качеството на машинно-обучителен модел. "
        "Вместо моделът да се тества само върху една тестова извадка, данните се разделят на няколко части <span class='font-bold'>(folds)</span>. Моделът се обучава многократно, като всеки път се използва различна част от данните за тестване. "
        "По този начин се постига по-надеждна и обективна оценка на представянето на модела. Кръстосаната валидация показва дали моделът се справя стабилно върху различни части от данните и намалява риска от <span class='font-bold'>overfitting</span>. "
        "Това позволява по-коректно сравнение между различните алгоритми за машинно обучение. "
    ).classes("text-base leading-relaxed pl-6").style("text-indent: 40px")

    # cross validation with linear regression
    cross_validation(get_model_linear_regression)
    # cross validation with random forest
    cross_validation(get_model_random_forest)
    # cross validation with redge regression
    cross_validation(get_model_Ridge_regression)
    # cross validation with lasso regression
    cross_validation(get_model_Lasso_regression)
    # cross validation with polynomial regression
    cross_validation(get_model_Polynomial_regression)
    # cross validation with decision tree
    cross_validation(get_model_decision_tree)
    # cross validation with support vector regression
    cross_validation(get_model_support_vector_regression)
    # cross validation with gradient boosting
    cross_validation(get_model_gradient_boosting)

    results = [
        linear_regression_result,
        random_forest_result,
        gradient_boosting_result,
        polynomial_regression_result,
        support_vector_regression_result,
        decision_tree_result,
        ridge_regression_result,
        lasso_regression_result
    ]

    run_benchmark(results)

    show_model_categories()

    get_model_comparison_table()

    # Footer
    with ui.element("footer").classes("w-full text-center mt-16 py-6").style("background-color: rgba(112,165,213,1);"):
        ui.label("© 2026 Всички права запазени").classes("text-sm text-white")
        ui.label("Създаден от Павел Рунчев").classes("text-sm text-white")
        ui.label("Вдъхновен от ТУ - Габрово (Извличане на знания от данни)").classes("text-sm text-white")

build_ui()

port = int(os.environ.get("PORT", 18013))
ui.run(title="Predicting CPU Performance",
       host="0.0.0.0",
       port=port,
       show=False
       )





