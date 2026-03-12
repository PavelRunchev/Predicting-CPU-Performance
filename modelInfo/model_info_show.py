from nicegui import ui

def model_info_show (model_name, description_model, image_name, strengths, weaknesses, applications):
    with (ui.expansion(f"{model_name} — информация за модела", icon="info")
            .classes("w-[700px] mx-auto text-lg hover:bg-blue-50 text-[#70A5D5] font-bold border border-[#70A5D5] rounded shadow-sm")
            .props("icon-color=#70A5D5")):

        ui.label("Кратко описание на модела:").classes("font-semibold mt-2 text-gray-800 font-normal")
        for sentence in description_model:
            ui.label(f"{sentence} ").classes("text-gray-800 font-normal")

        ui.image(f"static/{image_name}.png").classes("rounded-xl shadow-lg my-3 mx-auto")

        ui.label("Силни страни:").classes("font-semibold mt-2 text-gray-800 font-normal")
        view_model_loop(strengths)

        ui.label("Слаби страни:").classes("font-semibold mt-2 text-gray-800 font-normal")
        view_model_loop(weaknesses)

        ui.label("Приложение на модела:").classes("font-semibold mt-2 text-gray-800 font-normal")
        view_model_loop(applications)


def view_model_loop(data):
    with ui.column().classes("gap-1"):
        for item in data:
            ui.label(f"• {item}").classes("text-gray-800 font-normal pl-4")