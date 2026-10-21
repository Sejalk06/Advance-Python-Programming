import pandas as pd

data = pd.read_csv("students.csv")
series = pd.Series(data["Name"].values, index=data["RollNo"])
print("Series created from CSV:")
print(series)
