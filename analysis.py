import pandas as pd

df = pd.read_csv("Sale Report.csv")

print("--- PRIMERAS FILAS DEL REPORTE ---")
print(df.head())

print("\n--- STOCK TOTAL POR COLOR ---")
print(df.groupby('Color')['Stock'].sum())

columns_to_keep = ['SKU Code', 'Design No.', 'Stock', 'Category', 'Size', 'Color']
df_clean = df[columns_to_keep]

df_clean.to_excel("Sales_Report_Clean.xlsx", index=False)
print("\n¡Archivo 'Sales_Report_Clean.xlsx' generado con éxito!")