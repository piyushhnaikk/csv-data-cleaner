import pandas as pd 

def clean_data(df):
    df_clean = df.copy()

    df_clean["CustomerName"] = df_clean["CustomerName"].str.strip()
    
    df_clean["Email"] = df_clean["Email"].str.strip()
    
    df_clean["Status"] = df_clean["Status"].str.strip()

    df_clean["OrderDate"] = pd.to_datetime(
                        df_clean["OrderDate"],
                        errors = "coerce",
                        format = "mixed"
                        ).dt.date
    df_clean["Total"] = df_clean["UnitPrice"] * df_clean["Quantity"]

    return df_clean
