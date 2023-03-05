import pandas as pd


df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", index_col=0, decimal=",")

# Head method
print(df.head()) #default 5 rows

print(df.head(8))

# Columns method
print(df.columns) 
print(type(df.columns))  #pandas.core.indexes.base.Index type
print(df.columns.values) #numpy.ndarray type
print(list(df.columns.values)) #list type

# Note that list and array type are not equal
print(type(list(df.columns.values)) == type(df.columns.values))
try:
    df.columns.values.append("Hello")
except AttributeError:
    raise Exception("No append method exists")
finally:
    print("We use finally when we want that this part of code been executed anyway")
    
#Matrix with df values
print(df.values)

# Removing two columns from dataFrame. Data frame still with the same columns as we don't put inplace=True
print(df.drop(columns=["Maths", "Physics"]))
print(df)
print(df.drop(columns=["Maths", "Physics"], inplace=True))
print(df)
df = pd.read_csv(r"../dataFrames/marks.csv", delimiter=";", index_col=0, decimal=",")


