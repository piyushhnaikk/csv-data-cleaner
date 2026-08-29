import pandas as pd 
import openpyxl as xl 
from openpyxl.styles import Font, Alignment

def get_reports(filename : str, df_valid, df_invalid,df_summary):
    path = filename

    with pd.ExcelWriter(path) as writer:
        df_valid.to_excel(writer, sheet_name = "Cleaned Data", index = False)
        df_invalid.to_excel(writer, sheet_name = "Flagged Data", index = False)
        df_summary.to_excel(writer, sheet_name = "Summary", index = False )
    
    workbook = xl.load_workbook(path)

    valid_sheet = workbook["Cleaned Data"]
    invalid_sheet = workbook["Flagged Data"]
    summary_sheet = workbook["Summary"]
    
    style_reports(valid_sheet)
    style_reports(invalid_sheet)
    style_reports(summary_sheet)

    workbook.save(path)
    

def df_summary(df, df_valid, df_invalid):
    summary = {
        "Metric": ["Total Orders",
                    "Total Line Item",
                    "Total Cleaned Records",
                    "Total Flagged Records",
                    "Total Valid Sales",
                    "Flagged Potential Value"
                    ],
        "Value":  [
                    len(df["OrderID"].drop_duplicates()),
                    len(df_valid) + len (df_invalid),
                    len(df_valid),
                    len(df_invalid),
                    df_valid["Total"].sum(),
                    df_invalid["Total"].sum()
                    ]
                }

    df_summary = pd.DataFrame(summary)

    return df_summary

def style_reports(sheet):
    for cell in sheet[1]:
        cell.font = Font(bold = True)

    sheet.freeze_panes = "A2"

    for col in sheet.columns:
        largest = 0
        for cell in col:
            if cell.value is not None and len(str(cell.value)) > largest:
                largest = len(str(cell.value))
        sheet.column_dimensions[col[0].column_letter].width = largest + 5
