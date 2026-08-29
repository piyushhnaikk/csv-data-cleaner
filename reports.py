import pandas as pd 
import openpyxl as xl 

def get_reports(filename : str, df_valid, df_invalid,df_summary):
    path = "output/" + filename

    with pd.ExcelWriter(path) as writer:
        df_valid.to_excel(writer, sheet_name = "Cleaned Data", index = False)
        df_invalid.to_excel(writer, sheet_name = "Flagged Data", index = False)
        df_summary.to_excel(writer, sheet_name = "Summary", index = False )

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
