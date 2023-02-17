import pandas as pd

df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", index_col=0, decimal=",") 
print(df)
