from nicegui import ui
import pandas as pd

def cpu_table():
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
    
               /* Hide top "Rows per page" selector above the table */
               .q-field.q-select {
                   display: none !important;
               }
        
               .q-table thead th {
                 background-color: #70A5D5 !important;
                 color: white !important;
                 font-weight: 600;
               }
        
                /* Under line */
               .section-title {
                 position: relative;
                 display: inline-block;
                 padding-bottom: 6px;
               }
        
               .section-title::after {
                 content: "";
                 position: absolute;
                 left: 0;
                 bottom: 0;
                 width: 100%;
                 height: 4px;
                 background-color: var(--primary);
                 border-radius: 2px;
               }
        
               .q-table td:first-child,
               .q-table th:first-child {
                   padding-left: 12px !important;
                   text-align: left !important;
               }
           </style>
           """)

    ui.label("Таблица на процесорите:").classes("text-xl mt-6 mx-auto text-center")

    rows_selector = ui.select(
        options=[5, 10, 25, 50, 100],
        value=10,
        label="Rows per page"
    )

    sample_df = get_sample_data()
    table = ui.table.from_pandas(sample_df, pagination=rows_selector.value).classes(
        "w-full max-w-5xl mx-auto border border-gray-300 rounded-lg shadow-md bg-white text-sm table-auto divide-y divide-gray-200"
    )

    def update_pagination(e):
        table.pagination = e.args

    rows_selector.on('update:models-value', update_pagination)

    table.props('header-class="bg-[#EEF5FB] text-gray-800 font-semibold"')
    table.props('hide-top-pagination="true"')

def get_sample_data():
    df = pd.read_csv("data/machine.data", header=None)

    df.columns = [
        "Vendor",
        "Model",
        "Cycle (ns)",
        "Min Mem (KB)",
        "Max Mem (KB)",
        "Cache (KB)",
        "Min Ch",
        "Max Ch",
        "PRP",
        "ERP"
    ]

    return df