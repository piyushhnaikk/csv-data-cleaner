import pandas as pd 
def valid_df(df):
    df_valid = df[ (df["CustomerName"].notna()) & 
                    (df["Email"].notna()) & 
                    (df["Quantity"] > 0) & 
                    (df["UnitPrice"] > 0) & 
                    (df["Status"].notna()) &
                    (df["OrderDate"].notna())].copy()

    return df_valid

def invalid_df(df):
    df_invalid = df[ (df["CustomerName"].isna()) |
                    (df["Email"].isna()) |
                    (df["Quantity"] <= 0) |
                    (df["UnitPrice"] <= 0) |
                    (df["Status"].isna()) |
                    (df["OrderDate"].isna())].copy()
    
    reasons_list = []

    for index, row in df_invalid.iterrows():
        reasons = []
        if pd.isna(row["CustomerName"]):
            reasons.append("No Customer Name")

        if pd.isna(row["Email"]):
            reasons.append("No Email")

        if row["Quantity"] <= 0 :
            reasons.append("-ve Quantity")

        if row["UnitPrice"] <= 0:
            reasons.append("-ve Unit Price")

        if pd.isna(row["Status"]):
            reasons.append("No Status")

        if pd.isna(row["OrderDate"]):
            reasons.append("Invalid Date")
    
        reasons_list.append(", ".join(reasons))

    df_invalid["Reasons"] = reasons_list
    return df_invalid

