import validator as vd 
import pandas as pd 
import cleaner as cl 
import reports as rp 
import ui

print("Copy the csv file into data folder then:\n\n")
filename = input("Enter file name: ")

data_path = ui.get_path(filename)

df_raw = pd.read_csv(data_path)

df = cl.clean_data(df_raw)

df_valid = vd.valid_df(df)
df_invalid = vd.invalid_df(df)
df_summary = rp.df_summary(df, df_valid, df_invalid)

output_filename = input("Enter desired Excel file name:  ")
output_filename = ui.check_Filename(output_filename)

rp.get_reports(output_filename, df_valid, df_invalid, df_summary)