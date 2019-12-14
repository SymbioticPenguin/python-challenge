import os
financials_csv = os.path.join("budget_data.csv")
print(financials_csv)
with open(financials_csv,newline = "") as csvfile:
    reader = csv.reader(csvfile,delimiter = ",")
